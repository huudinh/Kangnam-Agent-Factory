# MẪU — DANH SÁCH POST QUẢNG CÁO

Bản markdown của [`MAU_Danh-sach-post-quang-cao.xlsx`](MAU_Danh-sach-post-quang-cao.xlsx). Dùng bản nào cũng được — Excel dễ điền hàng loạt, markdown dễ dán thẳng vào chat.

Đi kèm prompt [`doc/06-prompt-phan-tang-quang-cao.md`](../06-prompt-phan-tang-quang-cao.md).

---

## Cần điền những gì

| Cột | Mức | Giải thích |
|---|---|---|
| **Mã post** | Bắt buộc | Tự đặt: `P01`, `P02`… để tra cứu giữa các sheet |
| **Tên post đúng như trong thẻ Caresoft** | Bắt buộc | **Khoá nối — cột quan trọng nhất.** Sai một ký tự là không nối được |
| **Dịch vụ** | Bắt buộc | Mắt · Mũi · Hàm · Cắt mí… |
| **Nội dung / headline** | Bắt buộc | Câu chính hiển thị trên quảng cáo |
| **Từ ngày · Đến ngày** | Bắt buộc | `DD/MM/YYYY`. Còn chạy thì để trống ô "Đến ngày" |
| **Gom vào post gốc** | Nên có | Bản sao thì ghi mã post gốc. Post gốc để trống |
| **Định dạng** | Nên có | Ảnh đơn · Video · Carousel · Banner |
| **Góc tiếp cận** | Nên có | Để trống được, AI tự suy. Điền sẵn thì chính xác hơn |
| **Trạng thái** | Nên có | Đang chạy · Đã tắt |
| **Chi tiêu** | Tuỳ chọn | Chỉ cần nếu muốn tính *chi phí trên một lead HOT* |
| **Số inbox (FB báo)** | Tuỳ chọn | Để đối chiếu với số hội thoại đếm từ Caresoft |
| **Reach** | Tuỳ chọn | |

**Không cần điền:** số hội thoại, HOT/WARM/COLD, tỷ lệ có SĐT, rào cản — AI tự đếm từ file hội thoại.

**Sáu giá trị của cột "Góc tiếp cận":** Giá - ưu đãi · Tốc độ hồi phục · Tình trạng cụ thể · Giáo dục - giải đáp lo lắng · Chuyên môn - bác sĩ · Banner thông báo.

---

## Cách lấy "Tên post đúng như trong thẻ Caresoft"

Đây là cột quyết định cả bài phân tích chạy được hay không.

1. Mở một hội thoại bất kỳ trong Caresoft, xem **tin nhắn đầu tiên**
2. Tin đó có dạng: `[Thẻ: Inbox từ quảng cáo <TÊN POST> – <headline>]`
3. Copy đúng phần `<TÊN POST>` — nằm giữa `Inbox từ quảng cáo ` và dấu `–` đầu tiên
4. Hoặc lấy từ Facebook Ads Manager (ad name). Hai bên phải trùng khớp

Sai một ký tự, hoặc thiếu tiền tố `QC_`, là AI không nối được post với hội thoại.

---

## Gom bản sao về post gốc

Facebook hay nhân bản quảng cáo và thêm hậu tố `- Bản sao`, `- Bản sao 2`, `_Group_1`. Các bản sao thường cùng một nội dung, phải gom lại mới đủ mẫu.

Ví dụ thật từ dữ liệu cắt mí tháng 10 — ba dòng này là **cùng một creative**:

| Tên trong thẻ | Số hội thoại |
|---|---|
| `QC_Cắt mí_nhanh hồi phục` | 28 |
| `cắt mí nhanh hồi phục - Bản sao` | 13 |
| `cắt mí nhanh hồi phục - Bản sao 2` | 5 |

Gom lại **46 hội thoại** — đủ mẫu kết luận. Để riêng thì bản sao 2 chỉ có 5, không nói lên gì.

→ Post gốc cho mã `P01`; hai bản sao ghi `P01` vào cột *Gom vào post gốc*.

---

## Bảng để điền

Copy bảng dưới, xoá 3 dòng ví dụ, điền dữ liệu thật.

```markdown
| Mã post | Tên post đúng như trong thẻ Caresoft | Dịch vụ | Nội dung / headline | Từ ngày | Đến ngày | Gom vào post gốc | Định dạng | Góc tiếp cận | Trạng thái | Chi tiêu | Số inbox (FB báo) | Reach |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | QC_Cắt mí_nhanh hồi phục | Cắt mí | 💕Cắt mí ĐẸP MĨ MÃN, hồi phục cấp tốc x2 lần / 7 ngày là đẹp | 01/10/2026 |  |  | Video | Tốc độ hồi phục | Đang chạy |  |  |  |
| P01b | cắt mí nhanh hồi phục - Bản sao | Cắt mí | Cắt mí hồi phục nhanh x2 lần - Giá tốt nhất. Inbox tư vấn>> | 03/10/2026 |  | P01 | Video | Tốc độ hồi phục | Đang chạy |  |  |  |
| P02 | QC_Cắt mí_Banner combo mí già | Cắt mí | Hết sụp mí, bọng mỡ - Trẻ ra 5 tuổi. Inbox tư vấn! | 01/10/2026 |  |  | Banner | Tình trạng cụ thể | Đang chạy |  |  |  |
```

---

## File hội thoại đi kèm phải có gì

Phân tích chỉ **đo thật** được khi có file hội thoại cùng kỳ. File đó cần:

- Mỗi hội thoại một khối, mở đầu bằng `## <STT>. <Tên KH> — <DD/MM HH:MM>`
- Dòng tóm tắt: `- Phụ trách: … · Có SĐT: Có|Không · Số tin: …`
- Từng tin: `- **<DD/MM HH:MM> KH:** …` hoặc `- **<DD/MM HH:MM> NV (<tên>):** …`
- **Giữ nguyên thẻ `[Thẻ: Inbox từ quảng cáo …]` ở tin đầu** — mất thẻ là mất khoá nối
- **Toàn bộ hội thoại trong kỳ, không lọc theo độ dài** — xem cảnh báo trong `doc/06`

Không có file hội thoại thì AI chỉ chạy được chế độ dự đoán, kết quả là giả thuyết chứ không phải đo đạc.
