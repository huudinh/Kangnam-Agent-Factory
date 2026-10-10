#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KHU DINH DANH HOI THOAI CARESOFT
=================================

Nhan file xuat tho tu Caresoft -> tra ve file da khu dinh danh, an toan de
dua ra ngoai phuc vu cham QC / dung bo mau vang.

CHAY TAI CHO. Du lieu goc khong roi khoi may ban, script khong goi mang.

Phu thuoc: chi can openpyxl (de doc/ghi .xlsx).
    pip install openpyxl
File .csv thi khong can gi them.

Dung nhanh:
    python khu-dinh-danh.py -i xuat-caresoft.xlsx

Sinh ra 3 file:
    <ten>-an-danh.xlsx           <- GUI RA NGOAI DUOC
    <ten>-BANG-TRA-NOI-BO.xlsx   <- GIU LAI, TUYET DOI KHONG GUI
    <ten>-bao-cao-khu.txt        <- thong ke da xoa nhung gi

Kiem tra lai truoc khi gui:
    python khu-dinh-danh.py --verify xuat-caresoft-an-danh.xlsx
"""

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from collections import Counter, OrderedDict

HAVE_XLSX = True
try:
    from openpyxl import Workbook, load_workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
except ImportError:
    HAVE_XLSX = False


# ===========================================================================
# 1. NHAN DIEN COT -- Caresoft dat ten cot khac nhau tuy ban, nen do day
# ===========================================================================

COLUMN_HINTS = OrderedDict([
    ("ma_hoi_thoai", ["conversation id", "ma hoi thoai", "ticket id", "ticket",
                      "thread id", "id hoi thoai", "session id", "chat id",
                      "ma phien", "conversationid", "threadid", "ma ticket"]),
    ("thoi_gian",    ["thoi gian", "time", "timestamp", "created at", "ngay gio",
                      "sent at", "datetime", "ngay tao", "thoi diem", "gio gui"]),
    ("nguoi_gui",    ["nguoi gui", "sender", "direction", "from", "loai tin",
                      "chieu", "sender type", "role", "vai tro"]),
    ("ten_khach",    ["ten khach", "khach hang", "customer", "customer name",
                      "ho ten", "ho va ten", "full name", "fb name",
                      "ten facebook", "nguoi dung", "ten"]),
    ("sdt_khach",    ["sdt", "so dien thoai", "phone", "mobile", "dien thoai",
                      "phone number", "zalo"]),
    ("ma_nhan_vien", ["nhan vien", "agent", "staff", "tu van vien", "truc page",
                      "nguoi phu trach", "assignee", "agent name", "employee", "cskh"]),
    ("noi_dung",     ["noi dung", "message", "content", "text", "tin nhan", "body",
                      "noi dung tin nhan", "chat content", "hoi thoai", "transcript"]),
    ("dich_vu",      ["dich vu", "service", "san pham", "nhom dich vu", "page",
                      "fanpage", "chuyen muc"]),
])

# Cot bi loai hoan toan khoi file dau ra
DROP_HINTS = [
    "email", "profile", "link", "url", "facebook", "fb", "avatar", "anh dai dien",
    "zalo id", "psid", "user id", "uid", "cccd", "cmnd", "dia chi", "address",
    "ngay sinh", "dob", "birthday", "nam sinh", "attachment", "file dinh kem",
    "hinh anh", "image", "photo",
]


def _norm(s):
    """Bo dau, ha chu thuong -- de so khop ten cot va tu khoa."""
    if s is None:
        return ""
    s = unicodedata.normalize("NFD", str(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("đ", "d").replace("Đ", "D")
    return re.sub(r"[^a-zA-Z0-9]+", " ", s).strip().lower()


def detect_columns(headers, overrides=None):
    overrides = overrides or {}
    found, used = {}, set()
    norm = {h: _norm(h) for h in headers}
    for role, hints in COLUMN_HINTS.items():
        if role in overrides:
            if overrides[role] not in headers:
                sys.exit("Cot '%s' ban chi dinh cho '%s' khong co trong file.\n"
                         "Cac cot dang co: %s" % (overrides[role], role, ", ".join(headers)))
            found[role] = overrides[role]
            used.add(overrides[role])
            continue
        nh = [_norm(x) for x in hints]
        for h in headers:                      # khop chinh xac truoc
            if h not in used and norm[h] in nh:
                found[role] = h
                used.add(h)
                break
        if role in found:
            continue
        for h in headers:                      # roi moi khop chua
            if h in used:
                continue
            if any(x and x in norm[h] for x in nh):
                found[role] = h
                used.add(h)
                break
    return found


def columns_to_drop(headers, keep):
    out = []
    for h in headers:
        if h in keep:
            continue
        nh = _norm(h)
        if any(_norm(x) in nh for x in DROP_HINTS):
            out.append(h)
    return out


# ===========================================================================
# 2. MAU DINH DANH CAN XOA TRONG NOI DUNG
# ===========================================================================

PHONE_RE = re.compile(r"(?<![\w])((?:\+?84|0)(?:[\s.\-_]?\d){8,10})(?![\w])")
EMAIL_RE = re.compile(r"(?<![\w.])[\w.+-]+@[\w-]+\.[\w.]{2,}", re.I)
URL_RE = re.compile(
    r"(?:https?://|www\.)[^\s<>\"']+"
    r"|(?:(?:m|web|www)\.)?(?:facebook|fb|zalo|messenger|instagram|tiktok|prnt)"
    r"\.(?:com|me|sc|vn)/[^\s<>\"']*",
    re.I,
)
ID_RE = re.compile(
    r"(?:cccd|cmnd|cmt|căn cước|chứng minh|số định danh)"
    r"\D{0,12}(\d[\d\s.\-]{7,16}\d)", re.I)
DOB_RE = re.compile(
    r"(?:ngày sinh|năm sinh|sinh năm|sinh ngày|dob)"
    r"\D{0,10}((?:\d{1,2}[/\-.]){0,2}(?:19|20)\d{2})", re.I)
HONORIFIC_RE = re.compile(
    r"\b(chị|anh|em|cô|bác|bạn|mình|khách)\s+"
    r"([A-ZÀ-Ỹ][a-zà-ỹ]+(?:\s+[A-ZÀ-Ỹ][a-zà-ỹ]+){0,2})\b")

NOT_A_NAME = {_norm(w) for w in [
    "Kangnam", "Zalo", "Facebook", "Messenger", "TikTok", "Instagram", "Caresoft",
    "Plasma", "Idol", "Surgiform", "Nanoform", "Vline", "Thermage", "Botox", "Filler",
    "Picosure", "Profhilo", "Vaser", "Lipo", "Implant", "Meso", "Nano", "Gold",
    "Han Quoc", "Han", "Viet Nam", "Ha Noi", "Sai Gon", "Nguyen Trai",
    "Bac", "Bac Si", "Tro Ly", "Benh Vien", "Tham My", "Em", "Chi", "Anh", "Minh",
    "Da", "Vang", "Cam On", "Xin", "Chao", "Ok", "Oke", "Alo", "Shop",
    "Mat", "Mui", "Ham", "Nguc", "Mi", "Cam", "Moi", "Mo",
    "Thang", "Ngay", "Gio", "Sang", "Trua", "Chieu", "Toi",
    "Thu", "Hai", "Ba", "Tu", "Nam", "Sau", "Bay", "Nhat", "Thoi",
    # Ho va chu dem pho bien: dung mot minh thi khong dinh danh ai ca,
    # ma thay le te se pha hong ten day du cua nguoi khac.
    "Thi", "Van", "Nguyen", "Tran", "Le", "Pham", "Hoang", "Huynh", "Phan",
    "Vu", "Vo", "Dang", "Bui", "Do", "Ho", "Ngo", "Duong", "Ly", "Dinh",
    "Truong", "Luong", "Ma", "Ca", "Kieu",
]}

TOKEN_PHONE, TOKEN_EMAIL, TOKEN_URL = "[SDT]", "[EMAIL]", "[LINK]"
TOKEN_ID, TOKEN_DOB, TOKEN_NAME = "[GIAY-TO]", "[NGAY-SINH]", "[TEN]"


def _digits(s):
    return re.sub(r"\D", "", s or "")


def name_variants(full):
    """'Mai Hai Anh' -> ['Mai Hai Anh', 'Hai Anh', 'Mai', 'Hai'].

    Bo qua tu don nam trong NOT_A_NAME: 'Anh', 'Minh', 'Chi'... vua la ten
    vua la dai tu thong dung, thay le te se an nham ca cau noi binh thuong.
    """
    full = (full or "").strip()
    if len(full) < 2:
        return []
    parts = full.split()
    out = [full]
    if len(parts) >= 3:
        out.append(" ".join(parts[-2:]))          # ten goi: 2 tu cuoi
    for p in parts:
        if len(p) >= 2 and _norm(p) not in NOT_A_NAME:
            out.append(p)
    seen, uniq = set(), []
    for v in out:
        if v.lower() not in seen:
            seen.add(v.lower())
            uniq.append(v)
    return uniq


def collapse_tokens(t):
    """'[NV01] [NV01]' -> '[NV01]'; '[TEN] [TEN]' -> '[TEN]'."""
    return re.sub(r"(\[[A-Z0-9\-]+\])(?:\s+\1)+", r"\1", t)


class Scrubber:
    def __init__(self, hotlines=None, staff_map=None, customer_names=None,
                 redact_honorific=True):
        self.hotlines = {_digits(h) for h in (hotlines or []) if _digits(h)}
        self.staff_map = staff_map or {}
        # Gop ten nhan vien va ten khach vao MOT danh sach, sap xep dai truoc.
        # Neu tach lam hai luot, mot manh ngan cua ben nay (vd chu dem "Thi")
        # se cat doi ten day du cua ben kia truoc khi no kip khop.
        rules = {}
        for real, code in self.staff_map.items():
            for v in name_variants(real):
                rules.setdefault(v, ("[%s]" % code, "Ten nhan vien -> ma NV"))
        for nm in (customer_names or []):
            for v in name_variants(nm):
                rules.setdefault(v, (TOKEN_NAME, "Ten khach (tu cot ten)"))
        self.name_rules = sorted(rules.items(), key=lambda kv: -len(kv[0]))
        self.redact_honorific = redact_honorific
        self.stats = Counter()
        self.samples = {}

    def _note(self, kind, sample):
        self.stats[kind] += 1
        self.samples.setdefault(kind, [])
        if len(self.samples[kind]) < 3:
            s = str(sample)
            self.samples[kind].append(s if len(s) <= 4 else s[:2] + "***" + s[-2:])

    def _sub_phone(self, m):
        raw = m.group(1)
        d = _digits(raw)
        if d in self.hotlines or d.lstrip("0") in {h.lstrip("840") for h in self.hotlines}:
            return raw                       # so tong dai cong ty -> giu nguyen
        if not (9 <= len(d) <= 12):
            return raw
        self._note("So dien thoai", d)
        return TOKEN_PHONE

    def _sub_honorific(self, m):
        hon, name = m.group(1), m.group(2)
        if all(_norm(p) in NOT_A_NAME for p in name.split()):
            return m.group(0)
        self._note("Ten rieng sau xung ho", name)
        return "%s %s" % (hon, TOKEN_NAME)

    def scrub(self, text):
        if text is None:
            return text
        t = str(text)
        if not t.strip():
            return t

        def _u(m):
            self._note("Duong dan", m.group(0)[:14])
            return TOKEN_URL
        t = URL_RE.sub(_u, t)

        def _e(m):
            self._note("Email", m.group(0))
            return TOKEN_EMAIL
        t = EMAIL_RE.sub(_e, t)

        def _i(m):
            self._note("So giay to", m.group(1))
            return m.group(0).replace(m.group(1), TOKEN_ID)
        t = ID_RE.sub(_i, t)

        def _d(m):
            self._note("Ngay sinh", m.group(1))
            return m.group(0).replace(m.group(1), TOKEN_DOB)
        t = DOB_RE.sub(_d, t)

        t = PHONE_RE.sub(self._sub_phone, t)

        # Ten da biet -> token. Ten day du khop khong phan biet hoa thuong;
        # tu don phai dung chu hoa (tranh an nham "thao luan" vs ten "Thao").
        for text, (token, kind) in self.name_rules:
            flags = re.I if " " in text else 0
            t, n = re.subn(r"(?<!\[)\b%s\b" % re.escape(text), token, t, flags=flags)
            if n:
                self.stats[kind] += n

        if self.redact_honorific:
            t = HONORIFIC_RE.sub(self._sub_honorific, t)
        return collapse_tokens(t)


# ===========================================================================
# 3. DOC / GHI
# ===========================================================================

def read_table(path):
    """Tra ve (headers, rows) voi rows la list cac list chuoi."""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        for enc in ("utf-8-sig", "utf-8", "cp1258", "latin-1"):
            try:
                with open(path, newline="", encoding=enc) as f:
                    rd = list(csv.reader(f))
                if not rd:
                    sys.exit("File CSV rong.")
                return rd[0], [r + [""] * (len(rd[0]) - len(r)) for r in rd[1:]]
            except UnicodeDecodeError:
                continue
        sys.exit("Khong doc duoc CSV. Luu lai dang UTF-8 roi thu lai.")
    if ext in (".xlsx", ".xlsm"):
        if not HAVE_XLSX:
            sys.exit("Can openpyxl de doc .xlsx. Chay: pip install openpyxl")
        wb = load_workbook(path, data_only=True, read_only=True)
        ws = wb.active
        rows = []
        for r in ws.iter_rows(values_only=True):
            rows.append(["" if v is None else str(v) for v in r])
        wb.close()
        if not rows:
            sys.exit("File Excel rong.")
        head = rows[0]
        width = len(head)
        return head, [r + [""] * (width - len(r)) for r in rows[1:] if any(x for x in r)]
    if ext == ".json":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list) or not data:
            sys.exit("JSON phai la mot danh sach cac doi tuong.")
        head = list(data[0].keys())
        return head, [["" if row.get(k) is None else str(row.get(k)) for k in head]
                      for row in data]
    sys.exit("Chi ho tro .xlsx, .csv, .json -- file ban dua: %s" % (ext or "(khong ro)"))


def write_xlsx(path, sheets):
    """sheets: list cac (ten_sheet, headers, rows)."""
    if not HAVE_XLSX:
        sys.exit("Can openpyxl de ghi .xlsx. Chay: pip install openpyxl")
    wb = Workbook()
    wb.remove(wb.active)
    for name, head, rows in sheets:
        ws = wb.create_sheet(name[:31])
        ws.append(head)
        for c in range(1, len(head) + 1):
            cell = ws.cell(row=1, column=c)
            cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="3A1425")
            cell.alignment = Alignment(vertical="center", wrap_text=True)
        for r in rows:
            ws.append(list(r))
        for i, h in enumerate(head, start=1):
            longest = max([len(str(h))] + [len(str(r[i - 1])) for r in rows[:400]] or [10])
            ws.column_dimensions[get_column_letter(i)].width = min(70, max(12, longest + 2))
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.font = Font(name="Arial", size=10)
                cell.alignment = Alignment(vertical="top", wrap_text=True)
        ws.freeze_panes = "A2"
    wb.save(path)


# ===========================================================================
# 4. LUONG CHINH
# ===========================================================================

def run_anonymise(a):
    headers, rows = read_table(a.input)
    print("Doc xong: %d dong du lieu, %d cot" % (len(rows), len(headers)))

    overrides = json.loads(a.cols) if a.cols else {}
    cols = detect_columns(headers, overrides)
    idx = {role: headers.index(c) for role, c in cols.items()}

    print("\nNHAN DIEN COT")
    for role in COLUMN_HINTS:
        print("  %-14s -> %s" % (role, cols.get(role, "(khong thay)")))

    if "noi_dung" not in cols:
        sys.exit("\nKhong tim thay cot noi dung tin nhan.\n"
                 "Cac cot dang co: %s\n"
                 "Chi dinh thang, vi du:\n"
                 "  --cols '{\"noi_dung\":\"Message\",\"thoi_gian\":\"Time\"}'"
                 % ", ".join(headers))
    if "thoi_gian" not in cols:
        print("\n  CANH BAO: khong thay cot thoi gian. Tieu chi QC 'phan hoi trong\n"
              "  2 phut' se khong cham duoc. Nen xin ban xuat co dau thoi gian tung tin.")

    drops = columns_to_drop(headers, set(cols.values()))
    if drops:
        print("\nLOAI BO cac cot chua dinh danh truc tiep:")
        for c in drops:
            print("  - %s" % c)

    # bang tra noi bo: nhan vien
    staff_map, staff_rows = {}, []
    if "ma_nhan_vien" in cols:
        names = sorted({r[idx["ma_nhan_vien"]].strip() for r in rows
                        if r[idx["ma_nhan_vien"]].strip()})
        for i, nm in enumerate(names, start=1):
            staff_map[nm] = "NV%02d" % i
            staff_rows.append(["NV%02d" % i, nm])
        print("\nMa hoa %d nhan vien -> NV01..NV%02d" % (len(names), len(names)))

    # bang tra noi bo: hoi thoai
    conv_map, conv_rows = {}, []
    if "ma_hoi_thoai" in cols:
        seen = OrderedDict()
        for r in rows:
            v = r[idx["ma_hoi_thoai"]].strip()
            if v and v not in seen:
                seen[v] = "HT%04d" % (len(seen) + 1)
        conv_map = dict(seen)
        conv_rows = [[c, o] for o, c in seen.items()]
        print("Ma hoa %d hoi thoai -> HT0001..HT%04d" % (len(seen), len(seen)))

    # ten khach de doi chieu trong text
    customer_names = set()
    if "ten_khach" in cols:
        for r in rows:
            s = r[idx["ten_khach"]].strip()
            if 1 < len(s) < 60:
                customer_names.add(s)
                for part in s.split():
                    if len(part) > 2 and _norm(part) not in NOT_A_NAME:
                        customer_names.add(part)

    hotlines = [h.strip() for h in (a.hotline or "").split(",") if h.strip()]
    sc = Scrubber(hotlines, staff_map, customer_names, not a.giu_ten_xung_ho)

    # dung bang dau ra
    out_head, getters = [], []
    if "ma_hoi_thoai" in cols:
        out_head.append("ma_hoi_thoai")
        getters.append(lambda r: conv_map.get(r[idx["ma_hoi_thoai"]].strip(), ""))
    if "thoi_gian" in cols:
        out_head.append("thoi_gian")
        getters.append(lambda r: r[idx["thoi_gian"]])        # GIU NGUYEN
    if "nguoi_gui" in cols:
        out_head.append("nguoi_gui")
        getters.append(lambda r: r[idx["nguoi_gui"]])
    if "ma_nhan_vien" in cols:
        out_head.append("ma_nhan_vien")
        getters.append(lambda r: staff_map.get(r[idx["ma_nhan_vien"]].strip(), ""))
    if "dich_vu" in cols:
        out_head.append("dich_vu")
        getters.append(lambda r: r[idx["dich_vu"]])
    out_head.append("noi_dung")
    getters.append(lambda r: sc.scrub(r[idx["noi_dung"]]))

    handled = set(cols.values()) | set(drops)
    for h in headers:
        if h in handled:
            continue
        j = headers.index(h)
        out_head.append("khac__" + h)
        getters.append(lambda r, j=j: sc.scrub(r[j]))

    out_rows = [[g(r) for g in getters] for r in rows]

    base = os.path.splitext(a.input)[0]
    out_path = a.output or (base + "-an-danh.xlsx")
    map_path = a.map or (base + "-BANG-TRA-NOI-BO.xlsx")
    rep_path = base + "-bao-cao-khu.txt"

    if a.dry_run:
        print("\n--dry-run: khong ghi file. 4 dong dau sau khi khu:\n")
        ci = out_head.index("noi_dung")
        for r in out_rows[:4]:
            print("  %s | %s" % (" | ".join(r[:ci]) or "-", r[ci][:150]))
        return 0

    write_xlsx(out_path, [("Hoi thoai an danh", out_head, out_rows)])
    write_xlsx(map_path, [
        ("Nhan vien", ["ma_nhan_vien", "ten_that"], staff_rows or [["", ""]]),
        ("Hoi thoai", ["ma_hoi_thoai", "id_goc"], conv_rows or [["", ""]]),
    ])

    leftovers = scan_rows(out_head, out_rows, hotlines)
    L = ["BAO CAO KHU DINH DANH", "=" * 62,
         "File goc : %s" % a.input,
         "File ra  : %s" % out_path,
         "So dong  : %d" % len(out_rows), "",
         "DA XOA / THAY THE"]
    if sc.stats:
        for k, v in sc.stats.most_common():
            ex = sc.samples.get(k)
            L.append("  %-28s %5d%s" % (k, v, ("   vd: " + ", ".join(ex)) if ex else ""))
    else:
        L.append("  (khong phat hien dinh danh nao -- kiem tra lai cot noi dung)")
    L += ["", "COT DA LOAI BO"]
    L += ["  - %s" % c for c in drops] or ["  (khong co)"]
    L += ["", "QUET LAI FILE DAU RA"]
    if leftovers:
        L.append("  CON SOT -- PHAI XU LY TRUOC KHI GUI:")
        for kind, hits in leftovers.items():
            L.append("    %s: %d cho" % (kind, len(hits)))
            for r, c in hits[:5]:
                L.append("      dong %s, cot %s" % (r, c))
    else:
        L.append("  Sach. Khong con mau dinh danh may doc duoc.")
    L += ["", "LUU Y",
          "  - %s : GUI RA NGOAI DUOC" % os.path.basename(out_path),
          "  - %s : GIU LAI NOI BO, TUYET DOI KHONG GUI" % os.path.basename(map_path),
          "  - May khong tu phat hien duoc dia chi va mot so ten rieng.",
          "    Nen mo file an danh doc luot vai chuc dong truoc khi gui.",
          "  - Neu heuristic ten rieng bat nham qua nhieu tu thuong, chay lai voi",
          "    --giu-ten-xung-ho roi tu ra soat bang tay."]
    report = "\n".join(L)
    with open(rep_path, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n" + report)
    print("\nDa ghi:\n  %s\n  %s\n  %s" % (out_path, map_path, rep_path))
    return 2 if leftovers else 0


# ===========================================================================
# 5. CHE DO KIEM TRA LAI
# ===========================================================================

VERIFY_PATTERNS = OrderedDict([
    ("So dien thoai", PHONE_RE),
    ("Email", EMAIL_RE),
    ("Duong dan", URL_RE),
])


def scan_rows(headers, rows, hotlines=None):
    """Quet lai bang da xu ly. So tong dai trong hotlines duoc bo qua."""
    allow = {_digits(h) for h in (hotlines or []) if _digits(h)}
    hits = OrderedDict()
    for kind, pat in VERIFY_PATTERNS.items():
        found = []
        for ri, row in enumerate(rows, start=2):
            for ci, v in enumerate(row):
                if not v:
                    continue
                for m in pat.finditer(str(v)):
                    if kind == "So dien thoai":
                        d = _digits(m.group(0))
                        if not (9 <= len(d) <= 12) or d in allow:
                            continue
                    found.append((ri, headers[ci] if ci < len(headers) else ci))
                    break
                else:
                    continue
                break
        if found:
            hits[kind] = found
    return hits


def run_verify(path, hotlines=None):
    headers, rows = read_table(path)
    print("Quet %s -- %d dong, %d cot\n" % (path, len(rows), len(headers)))
    hits = scan_rows(headers, rows, hotlines)
    if not hits:
        print("SACH. Khong tim thay so dien thoai, email hay duong dan nao.")
        print("Luu y: may khong tu phat hien duoc ten rieng va dia chi -- van nen doc luot.")
        return 0
    print("CON SOT DINH DANH:")
    for kind, found in hits.items():
        print("  %s: %d cho" % (kind, len(found)))
        for r, c in found[:10]:
            print("    dong %s, cot %s" % (r, c))
        if len(found) > 10:
            print("    ... va %d cho nua" % (len(found) - 10))
    print("\nXu ly xong hay gui.")
    return 2


def main():
    # Console Windows mac dinh cp1252/cp437 -> in ten tieng Viet se vo.
    # Ep UTF-8, ky tu nao khong in duoc thi thay bang '?' thay vi bao loi.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    p = argparse.ArgumentParser(
        description="Khu dinh danh file xuat hoi thoai Caresoft truoc khi dua ra ngoai.",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    p.add_argument("--input", "-i", help="File xuat tho tu Caresoft (.xlsx / .csv / .json)")
    p.add_argument("--output", "-o", help="File ra (mac dinh: <ten>-an-danh.xlsx)")
    p.add_argument("--map", help="Bang tra noi bo (mac dinh: <ten>-BANG-TRA-NOI-BO.xlsx)")
    p.add_argument("--cols", help="Chi dinh cot thang, vd: '{\"noi_dung\":\"Message\"}'")
    p.add_argument("--hotline", help="So tong dai cong ty, cach nhau bang dau phay. "
                                     "Nhung so nay duoc GIU chu khong xoa")
    p.add_argument("--giu-ten-xung-ho", action="store_true",
                   help="Khong tu xoa ten rieng sau xung ho (chi/anh/em...)")
    p.add_argument("--dry-run", action="store_true", help="Chay thu, khong ghi file")
    p.add_argument("--verify", help="Chi quet mot file xem con sot dinh danh khong")
    a = p.parse_args()

    if a.verify:
        sys.exit(run_verify(a.verify,
                             [h.strip() for h in (a.hotline or '').split(',') if h.strip()]))
    if not a.input:
        p.print_help()
        sys.exit(1)
    if not os.path.exists(a.input):
        sys.exit("Khong thay file: %s" % a.input)
    sys.exit(run_anonymise(a))


if __name__ == "__main__":
    main()
