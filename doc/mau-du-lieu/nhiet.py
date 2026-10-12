# -*- coding: utf-8 -*-
"""Dung file Excel bieu do nhiet cho team Ads."""
import json, io, re, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule

OUT = (r"E:\Dinh_code\Project\Agent\Kangnam-Agent-Factory\output"
       r"\Kangnam_Ads_BieuDoNhiet_CatMi_T10.xlsx")
rows = json.load(io.open("rows.json", encoding="utf-8"))

# Tin hieu (1) chinh la "neu van de cu the". Ma bang nay lai phan nhom THEO van de
# -> cot %HOT bi lap vong: nhom nao co van de cu the thi duong nhien cong san 1 diem.
# Nen tinh them diem KHONG ke tin hieu (1), de so sanh cong bang giua cac nhom.
for _r in rows:
    _r["diem4"] = sum(int(x) for x in _r["bitmask"][1:])   # chi (2)(3)(4)(5)
    _r["nong4"] = "HOT*" if _r["diem4"] >= 3 else ("WARM*" if _r["diem4"] >= 1 else "COLD*")

BAND = "3A1425"; SOFT = "F7EBE6"; LINE = "D6BDB8"; GOLD = "F9ECD2"
th = Side(style="thin", color=LINE)
BD = Border(left=th, right=th, top=th, bottom=th)
HF = PatternFill("solid", fgColor=BAND)
HFONT = Font(name="Arial", size=10, bold=True, color="FFFFFF")
B = Font(name="Arial", size=10)
BB = Font(name="Arial", size=10, bold=True)
SUB = Font(name="Arial", size=10, italic=True, color="7A5560")
H1 = Font(name="Arial", size=14, bold=True, color=BAND)
H2 = Font(name="Arial", size=11, bold=True, color=BAND)
T = Alignment(vertical="top", wrap_text=True)
C = Alignment(vertical="center", horizontal="center", wrap_text=True)

# thang mau nhiet: trang -> vang -> do
SCALE = ColorScaleRule(start_type="min", start_color="FFFFFF",
                       mid_type="percentile", mid_value=50, mid_color="FFD28A",
                       end_type="max", end_color="D94A3D")

wb = Workbook()


def hdr(ws, row, labels, widths=None):
    for i, h in enumerate(labels, start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.fill = HF; c.font = HFONT; c.alignment = C; c.border = BD
        if widths:
            ws.column_dimensions[get_column_letter(i)].width = widths[i - 1]
    ws.row_dimensions[row].height = 38


def title(ws, t, sub, n):
    ws["A1"] = t; ws["A1"].font = H1
    ws["A2"] = sub; ws["A2"].font = SUB; ws["A2"].alignment = T
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=n)
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=n)
    ws.row_dimensions[1].height = 24
    ws.row_dimensions[2].height = 30


def heat(ws, r0, rowlabels, collabels, grid, lbl_w=28, extra=None):
    """Ve bang nhiet. extra = list (ten_cot, list gia tri) ghep them ben phai."""
    hdr(ws, r0, [""] + collabels + [e[0] for e in (extra or [])],
        [lbl_w] + [11] * len(collabels) + [12] * len(extra or []))
    for i, rl in enumerate(rowlabels):
        rr = r0 + 1 + i
        c = ws.cell(row=rr, column=1, value=rl); c.font = BB; c.alignment = T; c.border = BD
        c.fill = PatternFill("solid", fgColor=SOFT)
        for j in range(len(collabels)):
            cc = ws.cell(row=rr, column=2 + j, value=grid[i][j])
            cc.font = B; cc.alignment = C; cc.border = BD
        for k, (_, vals) in enumerate(extra or []):
            cc = ws.cell(row=rr, column=2 + len(collabels) + k, value=vals[i])
            cc.font = BB; cc.alignment = C; cc.border = BD
            cc.fill = PatternFill("solid", fgColor=GOLD)
        ws.row_dimensions[rr].height = 26
    a = "%s%d:%s%d" % (get_column_letter(2), r0 + 1,
                       get_column_letter(1 + len(collabels)), r0 + len(rowlabels))
    ws.conditional_formatting.add(a, SCALE)
    return r0 + len(rowlabels) + 1


def order(counter, keys=None):
    if keys:
        return keys
    return [k for k, _ in counter.most_common()]


NONG = ["HOT", "WARM", "COLD"]
vande_c = collections.Counter(r["vande"] for r in rows)
goc_c = collections.Counter(r["goc"] for r in rows)
post_c = collections.Counter(r["post_base"] for r in rows)
raocan_c = collections.Counter()
for r in rows:
    raocan_c.update(r["raocan"])

VANDE = order(vande_c)
GOC = order(goc_c)
RAOCAN = order(raocan_c)
POST = [k for k, v in post_c.most_common()]

# ==================================================== 1. Cach doc
ws = wb.active; ws.title = "Cách đọc"
title(ws, "BIỂU ĐỒ NHIỆT — KHÁCH HÀNG THEO VẤN ĐỀ",
      "Nguồn: 100 hội thoại inbox Cắt mí (05–10/10/2026), Caresoft · Dành cho team Ads", 4)
r = 4
for h, lines in [
 ("BIỂU ĐỒ NHIỆT ĐỌC THẾ NÀO", [
   "Ô càng ĐỎ = càng nhiều hội thoại rơi vào ô đó. Ô trắng = không có ca nào.",
   "Màu so sánh TRONG CÙNG MỘT BẢNG, không so giữa các bảng khác nhau.",
   "Cột vàng bên phải là tổng hoặc %, không tô nhiệt — đọc bằng số.",
 ]),
 ("BỐN BẢNG NHIỆT DÙNG VÀO VIỆC GÌ", [
   "① Vấn đề × Độ nóng — vấn đề nào ra khách nóng. Dùng để chọn vấn đề nên đẩy quảng cáo.",
   "② Góc tiếp cận × Vấn đề — mỗi góc quảng cáo kéo về nhóm vấn đề nào. Dùng để viết content.",
   "   Lưu ý ở bảng ①: cột %HOT bị lặp vòng, phải đọc cột %HOT* thay thế. Giải thích ngay dưới bảng đó.",
   "③ Vấn đề × Rào cản — mỗi nhóm vấn đề vướng gì. Dùng để chuẩn bị kịch bản và sửa thông điệp.",
   "④ Post × Độ nóng — post cụ thể nào hiệu quả. Dùng để quyết tăng ngân sách hay tắt.",
 ]),
 ("⚠ BA ĐIỀU PHẢI BIẾT TRƯỚC KHI DÙNG SỐ NÀY", [
   "1. MẪU ĐÃ BỊ LỌC. 100 hội thoại này được chọn từ 520, 'ưu tiên hội thoại dài'. Hội thoại",
   "   dài nghĩa là khách tương tác nhiều, tức đã thiên về phía nóng. Con số ở đây KHÔNG dùng",
   "   để quyết ngân sách — muốn vậy phải xin toàn bộ hội thoại trong kỳ, không lọc.",
   "2. PHÂN LOẠI LÀ TỰ ĐỘNG. Vấn đề mắt, rào cản và độ nóng do máy đọc tin khách rồi suy ra",
   "   theo từ khoá. Đây là bản rà đầu tiên, cần người đọc lại ít nhất 20 ca để hiệu chỉnh.",
   "3. Ô DƯỚI 10 CA KHÔNG KẾT LUẬN ĐƯỢC. Nhìn màu để thấy xu hướng, nhưng đừng rút kết luận",
   "   từ một ô chỉ có 2–3 ca.",
 ]),
 ("ĐỘ NÓNG TÍNH THẾ NÀO", [
   "Chấm 5 tín hiệu, mỗi tín hiệu 1 điểm:",
   "   ① nêu vấn đề mắt cụ thể (không phải 'cắt mí' chung chung)",
   "   ② có nhắc mốc thời gian gần (hôm nay, tuần này, đặt lịch…)",
   "   ③ hỏi lịch / bác sĩ / địa chỉ / khám",
   "   ④ gửi ảnh, hoặc mô tả dài và rõ",
   "   ⑤ đã để lại số điện thoại",
   "→ HOT 4–5 điểm · WARM 2–3 · COLD 0–1",
 ]),
]:
    ws.cell(row=r, column=1, value=h).font = H2; r += 1
    for line in lines:
        c = ws.cell(row=r, column=1, value=line)
        c.font = BB if line.startswith(("1.", "2.", "3.", "→")) else B
        c.alignment = T
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
        r += 1
    r += 1
ws.column_dimensions["A"].width = 100

# ==================================================== 2. Van de x Do nong
ws = wb.create_sheet("① Vấn đề × Độ nóng")
title(ws, "① VẤN ĐỀ MẮT × ĐỘ NÓNG",
      "Vấn đề nào kéo về khách sẵn sàng nhất. ĐỌC CỘT %HOT* — xem ghi chú bên dưới bảng.", 8)
grid, tong, pct, pct4, psdt = [], [], [], [], []
for v in VANDE:
    sub = [r for r in rows if r["vande"] == v]
    g = [sum(1 for r in sub if r["nong"] == n) for n in NONG]
    grid.append(g); tong.append(len(sub))
    pct.append(round(100 * g[0] / len(sub)) if sub else 0)
    pct4.append(round(100 * sum(1 for r in sub if r["diem4"] >= 3) / len(sub)) if sub else 0)
    psdt.append(round(100 * sum(1 for r in sub if r["sdt"] == "Có") / len(sub)) if sub else 0)
r = heat(ws, 4, VANDE, NONG, grid, 30,
         [("Tổng HT", tong), ("% HOT", pct), ("% HOT*", pct4), ("% cho số", psdt)])
ws.cell(row=r + 1, column=1, value="Đọc nhanh:").font = H2
ichung = VANDE.index("Cắt mí (chung)")
_oth = [i for i in range(len(VANDE)) if i != ichung]
_tb = sum(tong[i] for i in _oth)
pct4_oth = round(sum(pct4[i] * tong[i] for i in _oth) / max(1, _tb))
notes = [
 "⚠ CỘT '% HOT' BỊ LẶP VÒNG — ĐỪNG DÙNG ĐỂ SO SÁNH GIỮA CÁC NHÓM. Tín hiệu ① của thang"
 " chấm chính là 'khách nêu vấn đề cụ thể'. Bảng này lại chia nhóm theo vấn đề, nên mọi"
 " nhóm khác 'Cắt mí (chung)' đã được cộng sẵn 1 điểm. Cao hơn là đương nhiên, không"
 " phải phát hiện.",
 "✔ CỘT '% HOT*' mới là cột so sánh được: chấm lại chỉ bằng 4 tín hiệu còn lại"
 " (mốc thời gian · hỏi lịch-bác sĩ · gửi ảnh hoặc mô tả rõ · đã cho số), đạt ≥3/4 tính HOT*.",
 "",
 "KẾT QUẢ SAU KHI BỎ LẶP VÒNG — NGƯỢC VỚI TRỰC GIÁC:",
 "   · 'Cắt mí (chung)' — %d ca, %d%% HOT*" % (tong[ichung], pct4[ichung]),
 "   · Các nhóm nêu vấn đề cụ thể — %d ca, %d%% HOT* (bình quân có trọng số)" % (_tb, pct4_oth),
 "→ Khách KHÔNG tự nói rõ tình trạng %s khách có nói rõ. Nói cách khác, dữ liệu này"
 " KHÔNG chứng minh được rằng quảng cáo nêu tình trạng cụ thể lọc ra khách nóng hơn."
 % ("nóng ngang, thậm chí nhỉnh hơn" if pct4[ichung] >= pct4_oth else "nguội hơn"),
 "",
 "VIỆC CẦN LÀM: chênh lệch %d%% so với %d%% nằm trong sai số ở cỡ mẫu này, và mẫu lại đã"
 " bị lọc theo độ dài. Đừng đổi hướng content dựa trên bảng này. Muốn kết luận thật thì"
 " xin TOÀN BỘ hội thoại trong kỳ rồi chạy lại." % (pct4[ichung], pct4_oth),
]
for n in notes:
    r += 1
    c = ws.cell(row=r + 1, column=1, value=n); c.font = B; c.alignment = T
    ws.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1, end_column=7)

# ==================================================== 3. Goc x Van de
ws = wb.create_sheet("② Góc tiếp cận × Vấn đề")
title(ws, "② GÓC TIẾP CẬN × VẤN ĐỀ MẮT",
      "Mỗi góc quảng cáo kéo về nhóm vấn đề nào. Dùng để chọn góc khi viết content mới.", 2 + len(VANDE))
grid, tong, pct = [], [], []
for g in GOC:
    sub = [r for r in rows if r["goc"] == g]
    grid.append([sum(1 for r in sub if r["vande"] == v) for v in VANDE])
    tong.append(len(sub))
    pct.append(round(100 * sum(1 for r in sub if r["nong"] == "HOT") / len(sub)) if sub else 0)
heat(ws, 4, GOC, VANDE, grid, 26, [("Tổng HT", tong), ("% HOT", pct)])

# ==================================================== 4. Van de x Rao can
ws = wb.create_sheet("③ Vấn đề × Rào cản")
title(ws, "③ VẤN ĐỀ MẮT × RÀO CẢN",
      "Mỗi nhóm vấn đề thường vướng gì. Một hội thoại có thể có nhiều rào cản.", 2 + len(RAOCAN))
grid, tong = [], []
for v in VANDE:
    sub = [r for r in rows if r["vande"] == v]
    grid.append([sum(1 for r in sub if rc in r["raocan"]) for rc in RAOCAN])
    tong.append(len(sub))
heat(ws, 4, VANDE, RAOCAN, grid, 30, [("Tổng HT", tong)])

# ==================================================== 5. Post x Do nong
ws = wb.create_sheet("④ Post × Độ nóng")
title(ws, "④ POST × ĐỘ NÓNG",
      "Post nào ra khách nóng. Post dưới 10 hội thoại đánh dấu ⚠ — không xếp hạng.", 8)
grid, tong, pct, psdt, du = [], [], [], [], []
for p in POST:
    sub = [r for r in rows if r["post_base"] == p]
    g = [sum(1 for r in sub if r["nong"] == n) for n in NONG]
    grid.append(g); tong.append(len(sub))
    pct.append(round(100 * g[0] / len(sub)) if sub else 0)
    psdt.append(round(100 * sum(1 for r in sub if r["sdt"] == "Có") / len(sub)) if sub else 0)
    du.append("Đủ" if len(sub) >= 10 else "⚠ chưa đủ")
heat(ws, 4, POST, NONG, grid, 34,
     [("Tổng HT", tong), ("% HOT", pct), ("% cho số", psdt), ("Đủ mẫu?", du)])

# ==================================================== 6. Mau hoi thoai
ws = wb.create_sheet("Mẫu hội thoại thực tế")
title(ws, "MẪU HỘI THOẠI THỰC TẾ — THEO TỪNG VẤN ĐỀ",
      "Trích lời khách, mỗi nhóm vấn đề tối đa 3 ca. Số điện thoại đã che.", 6)
hdr(ws, 4, ["Vấn đề", "HT#", "Độ nóng", "Có SĐT", "Post", "Trích lời khách"],
    [26, 7, 11, 10, 30, 95])
PHONE = re.compile(r"(?<!\d)((?:\+?84|0)(?:[\s.\-]?\d){8,10})(?!\d)")
r = 5
for v in VANDE:
    sub = sorted([x for x in rows if x["vande"] == v],
                 key=lambda x: (-x["diem"], -len(x["trich"])))[:3]
    for x in sub:
        tx = PHONE.sub("[SĐT]", x["trich"])
        for i, val in enumerate([v, x["stt"], x["nong"], x["sdt"], x["post_base"], tx], start=1):
            c = ws.cell(row=r, column=i, value=val)
            c.border = BD; c.alignment = T
            c.font = BB if i == 1 else B
            if i == 3:
                c.fill = PatternFill("solid", fgColor={"HOT": "F7D4D1", "WARM": "FBE4C7",
                                                        "COLD": "DCE6F5"}[x["nong"]])
        ws.row_dimensions[r].height = 58
        r += 1
ws.freeze_panes = "A5"

# ==================================================== 7. Du lieu tho
ws = wb.create_sheet("Dữ liệu thô")
title(ws, "DỮ LIỆU THÔ — 100 HỘI THOẠI", "Để kiểm chứng lại mọi con số ở các bảng nhiệt.", 10)
hdr(ws, 4, ["HT#", "Ngày", "Có SĐT", "Số tin", "Post (đã gom)", "Góc tiếp cận",
            "Vấn đề mắt", "Rào cản", "Tín hiệu ①②③④⑤", "Độ nóng"],
    [6, 14, 9, 8, 32, 22, 24, 34, 14, 10])
r = 5
for x in rows:
    vals = [x["stt"], x["ngay"], x["sdt"], x["so_tin"], x["post_base"], x["goc"],
            x["vande"], " · ".join(x["raocan"]), "[%s]" % x["bitmask"], x["nong"]]
    for i, val in enumerate(vals, start=1):
        c = ws.cell(row=r, column=i, value=val); c.border = BD; c.alignment = T; c.font = B
        if i == 10:
            c.fill = PatternFill("solid", fgColor={"HOT": "F7D4D1", "WARM": "FBE4C7",
                                                    "COLD": "DCE6F5"}[x["nong"]])
            c.alignment = C
    ws.row_dimensions[r].height = 22
    r += 1
ws.freeze_panes = "A5"

wb.save(OUT)
print("Da ghi:", OUT)
print("Sheet:", wb.sheetnames)
