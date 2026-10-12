# -*- coding: utf-8 -*-
"""Tach va phan loai hoi thoai -> du lieu cho bieu do nhiet."""
import re, json, unicodedata, collections, io, sys

SRC = r"E:\Dinh_code\Project\Agent\Kangnam-Agent-Factory\output\hoi-thoai-cat-mi-05-10_10-10.md"


def nrm(s):
    """Chi ha chu thuong, GIU NGUYEN DAU.

    Bo dau roi so khop chuoi con la sai: 'khong' chua 'hong', 'gia dinh' trung
    'gia'. Giu dau thi hai tu do khac nhau ro rang.
    """
    return (s or "").lower()


_CACHE = {}


def has(text, kw):
    """So khop co bien tu, de 'giá' khong khop trong 'gia đình'."""
    pat = _CACHE.get(kw)
    if pat is None:
        pat = _CACHE[kw] = re.compile(r"(?<![\wàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệ"
                                      r"ìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữự"
                                      r"ỳýỷỹỵđ])" + re.escape(kw) +
                                      r"(?![\wàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệ"
                                      r"ìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữự"
                                      r"ỳýỷỹỵđ])")
    return bool(pat.search(text))


# --- Van de mat: xet theo thu tu uu tien, dung truoc thi lay
VANDE = [
 ("Làm lại / sửa",      ["sửa lại", "làm lại", "bị hỏng", "mí hỏng", "sửa mí", "hỏng rồi",
                          "đã cắt mí", "cắt mí rồi", "làm ở chỗ khác", "sửa mắt", "bị lỗi"]),
 ("Sụp mí",             ["sụp mí", "sụp mi", "mí sụp", "sa mí", "mắt buồn ngủ"]),
 ("Bọng mỡ / mí dưới",  ["bọng mỡ", "bọng mắt", "mí dưới", "mi dưới", "quầng thâm"]),
 ("Da chùng / lão hóa", ["da chùng", "chùng da", "lão hóa", "da thừa", "da dư", "nhão",
                          "trẻ hóa mắt", "nhăn mắt"]),
 ("Mở góc",             ["mở góc", "khóe mắt", "mở khóe"]),
 ("1 mí / mí lót",      ["1 mí", "một mí", "mí lót", "mi lót", "không có mí"]),
 ("Mí lệch / không đều", ["mí lệch", "lệch mí", "không đều", "không cân", "bên to bên nhỏ"]),
 ("Treo cung mày",      ["treo cung", "cung mày", "chân mày", "nâng cung"]),
 ("Nhấn mí",            ["nhấn mí"]),
]

RAOCAN = [
 ("Hỏi giá",         ["bao nhiêu", "giá", "chi phí", "nhiêu tiền", "hết nhiêu", "mắc không",
                      "đắt không", "giá cả"]),
 ("Ở xa / tỉnh",     ["ở xa", "xa quá", "nước ngoài", "việt kiều", "không có chi nhánh",
                      "ở tỉnh", "quê", "ở đức", "ở mỹ", "ở nhật", "ở hàn", "ở úc"]),
 ("Sợ đau / rủi ro", ["đau không", "có đau", "sợ đau", "biến chứng", "rủi ro", "nguy hiểm",
                      "sợ hỏng", "lo lắng", "sợ lắm"]),
 ("So sánh nơi khác", ["chỗ khác", "nơi khác", "tham khảo", "so sánh", "bên kia", "viện khác"]),
 ("Chưa có thời gian", ["bận quá", "chưa sắp xếp", "chưa có thời gian", "để sau", "khi nào rảnh",
                        "bận lắm"]),
 ("Hỏi người nhà",   ["chồng", "gia đình", "người nhà", "hỏi ý kiến", "bạn trai", "mẹ mình"]),
]

GOC = [
 ("Giáo dục — giải đáp", ["talk", "1001", "không lộ", "tại sao"]),
 ("Giá — ưu đãi",      ["giá rẻ", "giá tốt", "tối ưu giá", "7,2tr", "ưu đãi", "hóa đơn"]),
 ("Tình trạng cụ thể", ["mí già", "trẻ hóa mắt", "combo"]),
 ("Tốc độ hồi phục",   ["hồi phục"]),
 ("Banner thông báo",  ["banner", "công văn"]),
]


def match(text, table, default=None):
    t = nrm(text)
    for label, kws in table:
        if any(has(t, k) for k in kws):
            return label
    return default


def match_all(text, table):
    t = nrm(text)
    return [label for label, kws in table if any(has(t, k) for k in kws)]


def main():
    s = io.open(SRC, encoding="utf-8").read()
    blocks = re.split(r"\n## \d+\. ", s)[1:]
    rows = []
    for idx, b in enumerate(blocks, start=1):
        head = b.split("\n", 1)[0]
        name = head.split(" — ")[0].strip()
        day = head.split(" — ")[1].strip() if " — " in head else ""
        mp = re.search(r"Phụ trách:\s*(.*?)\s*·", b)
        ms = re.search(r"Có SĐT:\s*(\S+)", b)
        mn = re.search(r"Số tin:\s*(\d+)", b)
        phu = mp.group(1) if mp else ""
        sdt = (ms.group(1) if ms else "Không").strip()
        sotin = int(mn.group(1)) if mn else 0

        mt = re.search(r"\[Thẻ:\s*(.*?)\]", b)
        tag = mt.group(1).strip() if mt else ""
        post = tag[len("Inbox từ quảng cáo "):] if tag.startswith("Inbox từ quảng cáo ") else tag
        post = post.split(" – ")[0].strip() if post else "(không có thẻ)"
        if post == "Ưu đãi và thông báo":
            post_kind = "Tin hàng loạt"
        elif post == "(không có thẻ)" or not post:
            post_kind = "Không rõ nguồn"
        else:
            post_kind = "Quảng cáo"
        # gom ban sao
        base = re.sub(r"\s*-\s*Bản sao\s*\d*$", "", post)
        base = re.sub(r"_Group_\d+$", "", base)
        base = re.sub(r"\s*-\s*đã tối ưu$", "", base)
        base = re.sub(r"^QC_Cắt mí_", "", base)
        base = re.sub(r"^Cắt mí_", "", base).strip()

        kh = " ".join(re.findall(r"\*\*[^*]+KH:\*\*\s*(.*)", b))
        co_anh = "[Ảnh]" in kh

        vande = match(kh, VANDE, "Cắt mí (chung)")
        raocan = match_all(kh, RAOCAN)
        goc = match(post, GOC, "Khác / chưa phân loại")

        t = nrm(kh)
        s1 = vande != "Cắt mí (chung)"
        s2 = any(has(t, k) for k in ["hôm nay", "ngày mai", "tuần này", "cuối tuần",
                                      "tháng này", "sớm nhất", "tuần sau", "đặt lịch", "mai"])
        s3 = any(has(t, k) for k in ["đặt lịch", "lịch khám", "bác sĩ", "khám", "mấy giờ",
                                      "địa chỉ", "ở đâu"])
        s4 = co_anh or len(kh) > 300
        s5 = (sdt == "Có")
        bits = [s1, s2, s3, s4, s5]
        diem = sum(bits)
        nong = "HOT" if diem >= 4 else ("WARM" if diem >= 2 else "COLD")

        rows.append(dict(stt=idx, ten=name, ngay=day, phu_trach=phu, sdt=sdt, so_tin=sotin,
                         post=post, post_base=base, post_kind=post_kind, goc=goc,
                         vande=vande, raocan=raocan, bitmask="".join("1" if x else "0" for x in bits),
                         diem=diem, nong=nong,
                         trich=(kh[:300].replace("\n", " ") if kh else "")))
    json.dump(rows, io.open("rows.json", "w", encoding="utf-8"), ensure_ascii=False)

    print("Tong hoi thoai:", len(rows))
    print("\n--- Do nong:", dict(collections.Counter(r["nong"] for r in rows)))
    print("--- Co SDT  :", dict(collections.Counter(r["sdt"] for r in rows)))
    print("\n--- Van de mat:")
    for k, v in collections.Counter(r["vande"] for r in rows).most_common():
        print("   %3d  %s" % (v, k))
    print("\n--- Goc tiep can:")
    for k, v in collections.Counter(r["goc"] for r in rows).most_common():
        print("   %3d  %s" % (v, k))
    print("\n--- Rao can (mot HT co the nhieu):")
    c = collections.Counter()
    for r in rows:
        c.update(r["raocan"])
    for k, v in c.most_common():
        print("   %3d  %s" % (v, k))
    print("\n--- Post goc (sau gom):")
    for k, v in collections.Counter(r["post_base"] for r in rows).most_common():
        print("   %3d  %s" % (v, k[:60]))


if __name__ == "__main__":
    main()
