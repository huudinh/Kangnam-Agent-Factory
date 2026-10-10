# tools/ — Khử định danh hội thoại Caresoft

Công cụ chạy **tại chỗ** để làm sạch dữ liệu khách trước khi đưa file hội thoại ra ngoài —
phục vụ chấm QC, dựng bộ mẫu vàng, hoặc gửi cho bên thứ ba phân tích.

> **Vì sao cần bước này.** Hội thoại Caresoft chứa tên, số điện thoại, Zalo, link Facebook,
> mô tả tình trạng cơ thể, có ca kèm ảnh. Đề bài #8 trong `SYSTEM-PROMPT.md §11` quy định
> rõ: dữ liệu định danh khách **không được nạp lên công cụ công cộng**, và đề bài đó
> **chưa đóng**. Script này là cách lấy được dữ liệu để làm việc mà không vi phạm.

---

## Cài đặt

```bash
pip install openpyxl
```

Chỉ cần đúng một thư viện, và chỉ khi file là `.xlsx`. File `.csv` thì không cần gì thêm.
Script **không gọi mạng** — dữ liệu gốc không rời khỏi máy bạn.

## Dùng

```bash
python khu-dinh-danh.py -i xuat-caresoft.xlsx --hotline 02873066499,02873066466,02473088885
```

Sinh ra 3 file cạnh file gốc:

| File | Xử lý thế nào |
|---|---|
| `<tên>-an-danh.xlsx` | **Gửi ra ngoài được** |
| `<tên>-BANG-TRA-NOI-BO.xlsx` | **Giữ lại máy nội bộ. Tuyệt đối không gửi** — đây là bảng tra mã nhân viên và mã hội thoại về tên thật |
| `<tên>-bao-cao-khu.txt` | Thống kê đã xoá những gì, còn sót gì |

Kiểm tra lại trước khi gửi:

```bash
python khu-dinh-danh.py --verify xuat-caresoft-an-danh.xlsx --hotline 02873066499
```

Thoát mã `0` là sạch, `2` là còn sót — xem báo cáo rồi xử lý trước khi gửi.

## Các tuỳ chọn

| Tuỳ chọn | Dùng khi |
|---|---|
| `--hotline 028...,024...` | Số tổng đài công ty — **giữ lại**, không xoá. Không khai báo thì số tổng đài cũng bị xoá như số khách |
| `--cols '{"noi_dung":"Message"}'` | Script đoán sai tên cột. Chạy thử một lần để xem nó nhận diện ra sao rồi chỉ định thẳng |
| `--dry-run` | Xem thử kết quả, không ghi file |
| `--giu-ten-xung-ho` | Tắt phần đoán tên riêng sau xưng hô, khi nó bắt nhầm từ thường quá nhiều |

---

## Xoá những gì, giữ những gì

**Xoá hoặc thay bằng ký hiệu:**

| Loại | Thành |
|---|---|
| Số điện thoại (kể cả viết cách quãng `09 12 34 56 78`) | `[SDT]` |
| Email | `[EMAIL]` |
| Link Facebook, Zalo, ảnh, mọi URL | `[LINK]` |
| Số CCCD/CMND (khi có từ khoá đi kèm) | `[GIAY-TO]` |
| Ngày sinh, năm sinh | `[NGAY-SINH]` |
| Tên khách | `[TEN]` |
| Tên nhân viên | `[NV01]`, `[NV02]`… |
| Cột email, link, địa chỉ, ảnh | loại bỏ cả cột |

**Giữ nguyên — vì chấm QC cần:**

- **Dấu thời gian từng tin nhắn.** Tiêu chí ① chấm "phản hồi trong 2 phút"; mất timestamp là mất một tiêu chí.
- **Mã nhân viên.** Vẫn chấm và gom lỗi theo từng người được, chỉ là theo mã thay vì theo tên.
- **Mã hội thoại.** Vẫn nhóm các tin trong cùng một hội thoại được.
- Toàn bộ nội dung tư vấn, giá, tên dịch vụ, số tổng đài công ty.

Nói cách khác: **cả 10 tiêu chí trong bảng chấm đều chấm được trên dữ liệu đã khử định danh.**

---

## Giới hạn — đọc trước khi tin tưởng hoàn toàn

Script bắt tốt những thứ có khuôn dạng rõ ràng. Có hai thứ nó **không** làm được:

1. **Địa chỉ nhà.** Không có khuôn dạng cố định, máy không nhận ra được.
2. **Tên riêng không xuất hiện trong cột tên.** Ví dụ khách nhắc tên người thân, hoặc
   tên khách viết sai chính tả so với cột tên.

Phần đoán tên sau xưng hô (`chị Lan`, `anh Minh`) là **heuristic** — có thể bỏ sót, cũng có
thể bắt nhầm. Script đã loại trừ sẵn tên thương hiệu, tên công nghệ, họ và chữ đệm phổ biến
(`Thị`, `Văn`, `Nguyễn`…) để giảm bắt nhầm.

**Vì vậy: luôn mở file đã khử định danh, đọc lướt vài chục dòng trước khi gửi.** Lệnh
`--verify` chỉ xác nhận không còn số điện thoại, email và link — nó không thay được mắt người.

---

## Quy trình đề xuất

1. Người có quyền xuất dữ liệu từ Caresoft, lọc theo dịch vụ và khoảng thời gian cần.
   **Yêu cầu bản xuất có dấu thời gian từng tin nhắn.**
2. Chạy script trên máy nội bộ.
3. Đọc báo cáo `-bao-cao-khu.txt`, xem số liệu có hợp lý không
   (ví dụ: 100 hội thoại mà chỉ xoá 3 số điện thoại là đáng ngờ — có thể nhận nhầm cột).
4. Mở file `-an-danh.xlsx` đọc lướt.
5. Chạy `--verify` lần cuối.
6. Gửi **chỉ** file `-an-danh.xlsx`. File `-BANG-TRA-NOI-BO.xlsx` ở lại.

---

## Ghi chú kỹ thuật

- Thông báo ra màn hình cố tình viết **không dấu**, vì console Windows mặc định dùng
  bảng mã cp1252 và sẽ lỗi khi in tiếng Việt. Dữ liệu trong file xuất ra thì giữ nguyên
  tiếng Việt có dấu.
- Hỗ trợ đầu vào `.xlsx`, `.csv`, `.json`.
- Tên cột được nhận diện tự động theo từ khoá tiếng Việt và tiếng Anh. Chạy lần đầu,
  nhìn bảng "NHAN DIEN COT" in ra để kiểm tra nó đoán đúng chưa.
