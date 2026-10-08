# K6 — LUỒNG VẬN HÀNH & TRẠNG THÁI (Kangnam)
Module brand-specific. Đây là **xương sống** của cả hệ: mọi agent đọc trạng thái L-code từ đây.
Nguồn: file "Trực page – Tối ưu kịch bản" (sheet 1, 2, 4). Cập nhật: 2026-10-08.

---

## 1. LUỒNG VẬN HÀNH ĐẦU–CUỐI (hiện tại)

```
KH nhắn Fanpage (FB/Zalo/Web/TikTok)
  → Trực page đọc & trả lời trên Caresoft (CS)       [A1 gợi ý nội dung]
  → KH cho SĐT
  → Trực page tạo Lead, gửi Telesale qua CS          [A3 chấm Luồng 1]
  → Telesale gọi tư vấn qua CS                         [A3 chấm Luồng 2]
  → KH đồng ý → Telesale chuyển booking → ERP Kangnam
  → Hậu phẫu/chăm sóc                                  [A4 nhắc lịch]
  (xuyên suốt: A2 QC đọc hội thoại, chấm điểm, phân loại, báo lỗi NV)
```

Phần mềm lõi: **Caresoft (CS)** cho page + telesale; **ERP** cho booking. AI **không** thao tác trực tiếp trên CS/ERP ở Phase 1 — NV copy hội thoại/dữ liệu cho agent, agent trả gợi ý, NV dán lại (human-in-the-loop).

---

## 2. TAXONOMY TRẠNG THÁI L1–L6 (máy đọc được)

Đây là "state" chuẩn. QC gán L-code → Lead Scoring chấm theo L-code → A1 chọn kịch bản theo L-code → A4 lên nhịp theo L-code.

| Level | Mã | Định nghĩa | Nhiệt |
|---|---|---|---|
| **L1 Tương tác mới** | L1.1 | KH lần đầu nhắn qua FB/Zalo/Web/TikTok, chưa tư vấn. Thoại tự động tạo ticket. | Cold |
| **L2 Đang tư vấn** | L2.1 Tiềm năng | Có nhu cầu thật, chủ động/hợp tác cung cấp thông tin, có khả năng lên L4 sau khi lấy SĐT. | Warm |
| | L2.3 Chưa phản hồi | Đã tư vấn nhưng chưa phản hồi sau lần liên hệ gần nhất (chưa rõ DV quan tâm). | Warm |
| | L2.4 Hẹn nhắn lại sau | KH chủ động hẹn thời gian trao đổi sau. | Warm |
| | L2.5 Không có/xa chi nhánh | KH từ chối do địa phương không có CN / quá xa. | Cool |
| **L4 Cơ hội mới** | L4.1 | KH cung cấp **SĐT + DV quan tâm** hoặc chủ động gọi hotline → chuyển Sales. | Hot |
| **L5 Đang kết nối** | L5.3 Không nghe máy | Agent gọi nhưng KH không bắt máy sau nhịp quy định. | Hot |
| | L5.4 Không muốn nghe ĐT | KH từ chối cuộc gọi, yêu cầu trao đổi bằng tin nhắn. | Hot |
| | L5.5 Hẹn gọi lại sau | KH hẹn thời điểm gọi lại cụ thể. | Hot |
| | L5.6 Chỉ nhắn Zalo | KH cho SĐT nhưng chỉ tư vấn qua Zalo, không gọi. | Hot |
| **L6 Cơ hội tiềm năng ≤30 ngày** | L6.1 Tiềm năng | Có nhu cầu, Agent chưa xác định rào cản cụ thể. | Warm→Hot |
| | L6.2 So sánh nơi khác | Đang tham khảo nhiều đơn vị. | Warm→Hot |
| | L6.3 Chưa có tài chính | Có nhu cầu, chưa đủ/chưa sẵn ngân sách. | Warm→Hot |
| | L6.4 Chưa có thời gian | Muốn làm nhưng chưa sắp xếp được. | Warm→Hot |
| | L6.5 Lo lắng/sợ đau | E ngại đau, gây mê, rủi ro, hồi phục. | Warm→Hot |
| | L6.6 Hỏi ý kiến người thân | Cần người thân tham gia quyết định. | Warm→Hot |

**Nhịp theo dõi L6 (chưa Booking):** D+3 → D+7 → D+15 (nhận tin nhưng chưa phản hồi/booking thì đẩy nhịp kế).

---

## 3. ROUTING / CHIA DỮ LIỆU (sheet "Vận hành xử lý dữ liệu")

| Trạng thái | Trigger | Chia dữ liệu | Chia cho ai | Thời gian |
|---|---|---|---|---|
| L1.1 | Thoại tự động tạo ticket | — | Agent chăm sóc & phân loại tag → L2 | ngay |
| L2.1 | Chưa có SĐT, KH không phản hồi hoặc phản hồi rồi im lặng | Sau 1 ngày, trong vòng 7 ngày | All nhân sự online | 9h (ca sáng) & 15h (ca chiều) |

> Các dòng routing khác (L2.3/L2.4/L5/L6) hiện để trống trong file gốc → **slot ⚠ chờ Kangnam cấp quy tắc chia**. Mặc định đề xuất: L5/L6 chia về đúng NV telesale đã chạm; L2.3/L2.4 vào hàng chờ chung theo ca.

---

## 4. QUY ƯỚC ĐẶT TÊN KB (sheet "Cài đặt KB lên hệ thống")

Kịch bản nạp lên hệ thống theo 4 nhóm trạng thái, mỗi nhóm slot KB1–KB16:

| Nhóm | Mã KB | Trạng thái tương ứng |
|---|---|---|
| NHÓM 1 — Chưa có SĐT | `No Number_KB{1..16}` | L2.x (đang tư vấn, chưa lấy số) |
| Hẹn giờ gọi lại | `Call-back_KB{1..16}` | L5.5 |
| NHÓM 2 — Đã có SĐT, gọi không nghe | `Missed call_KB{1..16}` | L5.3 |
| NHÓM 3 — Đã gọi tư vấn, chưa Booking | `Take care_KB{1..16}` | L6.x |

→ Nội dung từng KB nằm ở **K5**. File gốc sheet 1 mới có tên slot; K5 đã map nội dung thực vào đúng slot (phần nào còn trống = ⚠ chờ bổ sung).

---

## 5. ĐIỀU KIỆN THOÁT (Exit condition) — khi nào ngừng nuôi dưỡng

- KH **Booking** → chuyển ERP, thoát luồng nuôi.
- KH **từ chối dứt khoát** ("không có nhu cầu") → tag đóng, dừng.
- **Hết cửa sổ 24h** (Messenger) mà chưa phản hồi → ngừng nhắn tự do; có SĐT thì chuyển sale, chưa có thì tag chờ KH quay lại.
- **Quá 30 ngày** ở L6 không tiến triển → hạ nhiệt về tệp remarketing.

---

## 6. HANDOFF PAYLOAD (Page → Telesale/Sales, khi lên L4)

Trước khi đóng chat, ghi chú đầy đủ cho sale trên Caresoft (dùng cho A3 Lead Scoring):
**Chân dung · Dịch vụ quan tâm · Chỉ số/tình trạng (ảnh, vùng) · Nỗi đau chính · Số lần hỏi giá · Khung giờ tiện · Kênh ưu tiên (gọi/Zalo) · L-code hiện tại.**

---

## 7. LIÊN KẾT MODULE
[[K3-hanh-vi-trang-thai]] (map 6 giai đoạn ↔ L1–L6) · [[K5-kich-ban]] (nội dung KB) · [[K7-chien-dich-thang]] (ưu đãi hiện hành).
