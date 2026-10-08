# 02 · CÂU LỆNH — AGENT FACTORY (KANGNAM)

---

# 1. Hai dạng lệnh

```
TẠO AGENT:     Tạo agent [tư vấn / QC / lead scoring / nhắc lịch] cho [dịch vụ / bối cảnh].
HỎI VẬN HÀNH:  [Mô tả tình huống khách] — trạng thái gì, dùng KB nào, ai xử lý?
```

Không nói rõ → Factory hỏi đúng một câu: *"Bạn muốn mình tạo agent, hay giải thích luồng vận hành?"*

---

# 2. TẠO AGENT

## 2.1 Agent tư vấn cho một dịch vụ
```
Tạo agent tư vấn trực page cho dịch vụ nâng mũi.
```

## 2.2 Agent tư vấn hẹp hơn — theo rào cản
```
Tạo agent tư vấn cho nhóm khách đang ở L6.5 (lo lắng, sợ đau),
dịch vụ hút mỡ. Trọng tâm là gỡ nỗi sợ, chưa chốt.
```

## 2.3 Agent QC
```
Tạo agent QC chấm hội thoại trực page cho line Mắt.
Dùng rubric v1 trong A2, nêu rõ chỗ nào cần Kangnam duyệt trọng số.
```

## 2.4 Agent lead scoring
```
Tạo agent lead scoring chấm cả 2 luồng (hội thoại page + cuộc gọi telesale).
Xếp hạng A/B/C/D.
```

## 2.5 Agent nhắc lịch hậu phẫu
```
Tạo agent nhắc lịch cho khách sau cắt mí.
Nhịp theo phác đồ hậu phẫu trong K4; thiếu thì ghi cần xác minh.
```

## 2.6 Xem trước phiếu 6 ô rồi mới ráp
```
Tạo agent tư vấn cho dịch vụ trẻ hóa da — nhưng đưa phiếu 6 ô cho mình
duyệt trước, chưa ráp system prompt vội.
```

## 2.7 Sửa agent đã sinh
```
Agent A1-Mũi vừa sinh còn thiếu phần xử lý khách so sánh với nơi khác (L6.2).
Bổ sung, chỉ nêu phần thay đổi.
```

---

# 3. HỎI VẬN HÀNH

## 3.1 Tra trạng thái từ tình huống
```
Khách cho SĐT rồi gọi không nghe là trạng thái gì, dùng KB nào, ai xử lý?
```
```
Khách bảo "để em hỏi chồng đã" thì xếp trạng thái nào?
```
```
Khách ở tỉnh không có chi nhánh thì tag gì, có nuôi tiếp không?
```

## 3.2 Tra nhịp chăm sóc
```
Khách ở L6 chưa booking thì nhắc lại theo nhịp nào?
```
```
Khi nào thì ngừng nuôi dưỡng một khách?
```

## 3.3 Tra quy ước KB
```
Nhóm KB nào dùng cho khách chưa cho số? Có bao nhiêu slot?
```

## 3.4 Tra handoff
```
Trước khi chuyển lead cho telesale, mình phải ghi những gì vào Caresoft?
```

## 3.5 Tra bản đồ giai đoạn ↔ trạng thái
```
Khách đang ở giai đoạn "cân nhắc & nỗi sợ" thì tương ứng L-code nào,
agent nào xử lý chính?
```

---

# 4. Prompt tinh chỉnh

```
Phiếu 6 ô ở ô Rules còn sơ sài. Viết lại cho đủ 9 guardrail.
```
```
System prompt vừa sinh dài quá, rút gọn phần quy trình nhưng giữ nguyên
phần KHÔNG được.
```
```
Agent này chưa có KPI đo được. Thêm KPI vào rồi test lại 4 tiêu chí.
```
```
Thay mọi con số ưu đãi bằng ⚠ Cần xác minh từ Kangnam — K7 tháng này
mình chưa cập nhật.
```
```
Agent con đang để AI tự gửi tin cho khách. Sửa về đúng Phase 1:
chỉ gợi ý, NV duyệt.
```

---

# 5. Những gì Factory sẽ TỪ CHỐI hoặc CẢNH BÁO

| Yêu cầu | Phản hồi của Factory |
|---|---|
| "Tạo 1 agent làm hết: tư vấn + QC + nhắc lịch" | **Từ chối gộp**; giải thích "một agent một việc"; đề xuất tách A1 + A2 + A4 |
| "Tạo agent theo phòng ban Marketing" | Cảnh báo tạo theo **công việc**, không theo phòng ban; hỏi cụ thể agent làm việc gì |
| "Ưu đãi tháng này bao nhiêu %?" (K7 hết hạn) | `⚠ Cần xác minh từ Kangnam`; **không dùng số tháng trước** |
| "Lấy giá lần trước bạn nói ấy" | Từ chối; số cũ có thể đã sai — bắt buộc tra K7 hiện hành |
| "Viết nội dung cho slot Take care_KB9" (slot trống) | Nói rõ **⚠ chờ bổ sung**; không tự viết lấp |
| "L2.3 chia cho ai?" (K6 §3 trống) | Nói rõ file gốc để trống; đưa **đề xuất mặc định**, ghi rõ là đề xuất chờ Kangnam chốt |
| "Thêm bác sĩ X cho uy tín" | Kiểm K4; chưa trong danh sách **được duyệt quảng bá** → `⚠ Cần xác minh` |
| "Ghi bác sĩ này đã làm 5000 ca" | Từ chối nếu số ca chưa xác minh — web có hồ sơ tự gắn cờ mâu thuẫn |
| "Cho agent cam kết đẹp 100% cho chắc" | Từ chối; vi phạm guardrail 2 |
| "Agent tự chẩn đoán tình trạng khách qua ảnh" | Từ chối; guardrail 3 — chỉ tư vấn sơ bộ, mời đến bác sĩ |
| "Báo giá cứng luôn cho khách khỏi mất công" | Từ chối nếu chưa xác minh; nêu lý do + hướng đặt lịch (quy tắc vàng #4) |
| "Cho AI trả lời thẳng khách trên Caresoft" | Từ chối ở Phase 1; human-in-the-loop |
| "Gửi hồ sơ bệnh án khách để agent học" | Từ chối; guardrail 5 |
| "Tạo agent tư vấn tiêm PRP khớp gối" | Báo thuộc **Cơ Xương Khớp – Wellness**, agent khác |
| "Xuất luôn đi, khỏi test" | Cảnh báo chưa qua test 4 tiêu chí; agent chưa đạt không nên chạy |
| "Bỏ bớt phần KHÔNG được cho prompt gọn" | Từ chối; mọi agent con phải kế thừa đủ 9 guardrail |
