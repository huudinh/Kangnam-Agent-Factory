# 04 · 10 PROMPT CHO NHÂN VIÊN VẬN HÀNH

Dành cho bạn nếu **chưa thuộc mã L-code và mã KB**. Cứ mô tả tình huống bằng lời thường — Factory tự tra và **giải thích mã nghĩa là gì**, không bắt bạn học thuộc trước.

---

# Mẫu điền chỗ trống

```
Khách [LÀM GÌ / NÓI GÌ]. Giờ mình nên làm sao?
```
hoặc
```
Tạo cho mình một trợ lý làm việc [VIỆC GÌ] cho dịch vụ [DỊCH VỤ NÀO].
```

---

# 10 PROMPT

## 1 · Khách im lặng, không biết xếp vào đâu
> Khách nhắn hỏi giá rồi im luôn, mình nhắn lại không trả lời. Giờ tính là trạng thái gì, mình nên làm gì tiếp?

**Nhận được:** mã trạng thái + giải thích mã đó nghĩa gì + nhóm kịch bản nên dùng + nhịp nhắn lại.

---

## 2 · Khách cho số rồi gọi không nghe
> Khách cho số điện thoại rồi mà gọi mãi không bắt máy. Xếp vào đâu, ai xử lý tiếp?

**Nhận được:** `L5.3` · nhóm `Missed call_KB` · A4 lên nhịp nhắc, A3 chấm cuộc gọi.

---

## 3 · Khách nói để hỏi người nhà
> Khách bảo "để em hỏi chồng đã rồi báo lại". Mình nên nhắn gì, bao lâu thì nhắn lại?

**Nhận được:** `L6.6` + hướng xử lý **không ép chốt** — đưa thứ khách mang về bàn với người nhà, kèm nhịp D+3 → D+7 → D+15.

---

## 4 · Khách ở xa, không có chi nhánh
> Khách ở tỉnh không có chi nhánh mình. Có nên nuôi tiếp không hay bỏ?

**Nhận được:** `L2.5` + hướng xử lý và điều kiện khi nào thì dừng nuôi.

---

## 5 · Bao giờ thì ngừng chăm khách
> Khách nào thì mình ngừng nhắn tin chăm sóc? Mình đang không biết lúc nào nên dừng.

**Nhận được:** 4 điều kiện thoát — booking · từ chối dứt khoát · hết cửa sổ 24h Messenger · quá 30 ngày không tiến triển.

---

## 6 · Chuyển khách cho telesale cần ghi gì
> Trước khi chuyển khách cho bạn telesale, mình phải ghi những gì vào Caresoft?

**Nhận được:** đủ 8 mục handoff — thiếu mục nào thì bạn telesale gọi điện sẽ hỏi lại khách từ đầu, khách khó chịu.

---

## 7 · Nhờ làm trợ lý trả lời khách
> Làm cho mình một trợ lý gợi ý câu trả lời khách hỏi về **nâng mũi**. Mình trực page, cần câu trả lời nhanh mà đúng.

**Nhận được:** phiếu tóm tắt để bạn duyệt trước, rồi tới bản hướng dẫn đầy đủ nạp vào máy được.

---

## 8 · Nhờ làm trợ lý chấm điểm
> Làm cho mình một trợ lý **chấm điểm hội thoại** của nhân viên, chỉ ra ai sai ở đâu để đào tạo.

**Nhận được:** agent QC kèm rubric chấm. Factory sẽ nói rõ rubric này **đang là bản đề xuất, cần Kangnam duyệt trọng số**.

---

## 9 · Ưu đãi tháng này
> Tháng này đang có chương trình gì, giảm bao nhiêu?

**Nhận được:** số lấy từ module chiến dịch tháng hiện hành. **Nếu module đã hết hạn, Factory sẽ báo cần xác minh chứ không đọc số tháng trước** — đây là lỗi đã từng xảy ra (giá 6tr ≠ 3tr, 7 ≠ 10 cơ sở).

---

## 10 · Cho AI trả lời khách luôn được không
> Mình bận quá, cho AI trả lời thẳng khách trên Caresoft được không?

**Nhận được:** **không** ở giai đoạn này. AI chỉ gợi ý, bạn đọc và duyệt rồi mới dán cho khách. Lý do: đây là nội dung y tế, sai một câu là rủi ro thật.

---

# 3 điều bạn KHÔNG cần lo

| Bạn lo | Thực tế |
|---|---|
| "Không thuộc mã L1, L2, L5, L6" | Cứ mô tả tình huống, Factory tự tra và giải thích mã nghĩa là gì. |
| "Không biết dùng kịch bản nào" | Factory chỉ đúng nhóm KB và nói nội dung nằm ở đâu. |
| "Sợ nói sai câu vi phạm" | Mọi agent sinh ra đều có sẵn phần "KHÔNG được" — 9 điều cấm. |

---

# 3 điều bạn PHẢI kiểm

**① `⚠ Cần xác minh từ Kangnam` là chỗ thiếu dữ liệu thật** — thường là giá, ưu đãi, tên bác sĩ. Đừng tự điền, hỏi quản lý.

**② Mọi câu trả lời phải bạn duyệt trước khi gửi khách.** AI chỉ gợi ý. Đây là nội dung y tế.

**③ Số ưu đãi phải khớp chương trình đang chạy.** Nếu thấy Factory đọc ra con số mà bạn ngờ là của tháng trước — dừng lại, báo người quản lý module chiến dịch tháng.

---

# Nếu câu trả lời khó hiểu

```
Nói đơn giản thôi, mình không rành mấy mã này.
```
```
Mã đó nghĩa là gì vậy?
```
```
Cho mình ví dụ câu nhắn cụ thể luôn đi.
```
```
Ngắn gọn thôi, mình đang trực page gấp.
```
