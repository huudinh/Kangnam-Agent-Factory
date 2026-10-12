# 06 — PROMPT: POST QUẢNG CÁO → PHÂN TẦNG HOT / WARM / COLD

Trả lời câu hỏi: **post nào kéo về khách nóng, post nào chỉ kéo về người hỏi dạo.**

Đầu ra một file: `output/Kangnam_PhanTang_QuangCao_<KỲ>.xlsx`

---

## Hai chế độ — chọn đúng chế độ trước khi chạy

| Chế độ | Khi nào | Độ tin cậy |
|---|---|---|
| **A · ĐO THẬT** | Có cả danh sách post **và** file hội thoại cùng kỳ | Cao — đếm kết quả thật |
| **B · DỰ ĐOÁN** | Chỉ có post, chưa có hội thoại (post mới, hoặc kỳ cũ không còn log) | Thấp — chỉ là giả thuyết |

**Luôn ưu tiên chế độ A.** Hội thoại xuất từ Caresoft có sẵn thẻ nguồn ở tin đầu:

```
[Thẻ: Inbox từ quảng cáo QC_Cắt mí_nhanh hồi phục – 💕Cắt mí ĐẸP MĨ MÃN, hồi phục cấp tốc x2 lần…]
```

Thẻ này là **khoá nối** giữa post và hội thoại. Có nó thì không cần đoán.

Chạy chế độ A cho kỳ có dữ liệu trước, rút ra quy luật, rồi mới dùng chế độ B cho kỳ không có dữ liệu.

---

## ⚠ Đọc trước khi tin kết quả

**Mẫu phải là toàn bộ, không được lọc.** File hội thoại tháng 10 hiện có là **100 hội thoại chọn từ 520, ưu tiên hội thoại dài**. Hội thoại dài nghĩa là khách tương tác nhiều — tức là đã thiên về phía nóng. Dùng mẫu này để so sánh post sẽ **thổi phồng chất lượng của mọi post**, và thổi không đều nhau.

→ Muốn so sánh post cho ra quyết định ngân sách, phải xin **toàn bộ hội thoại trong kỳ**, không lọc theo độ dài.

**Mẫu nhỏ không kết luận được.** Trong 100 hội thoại tháng 10, 15 post chia nhau: post nhiều nhất 32 hội thoại, nhưng có post chỉ 1–3. Dưới 10 hội thoại thì con số % không nói lên gì. Prompt bắt đánh dấu `⚠ chưa đủ mẫu` cho các post này.

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
Phân tầng các post quảng cáo theo chất lượng khách mà chúng kéo về.
Sinh ra ĐÚNG 1 file: `output/Kangnam_PhanTang_QuangCao_{{KỲ}}.xlsx`

Viết script Python dùng openpyxl. Ghi ra file thật, không trả bảng trong chat.

# ĐẦU VÀO
- Danh sách post đang quảng cáo: {{FILE POST}}
- File hội thoại cùng kỳ (nếu có): {{FILE HỘI THOẠI}}
- Dịch vụ: {{DỊCH VỤ}}   — ví dụ: Mắt, Mũi, Hàm
- Kỳ: {{KỲ}}             — ví dụ: 01-10/10/2026

Chế độ chạy:
- Có file hội thoại  → CHẾ ĐỘ A (đo thật). Bắt buộc dùng chế độ này.
- Không có           → CHẾ ĐỘ B (dự đoán). Ghi rõ trên mọi sheet rằng đây là giả thuyết.

# CHẾ ĐỘ A — ĐO THẬT

## A1. Nối post với hội thoại
Mỗi hội thoại có thẻ nguồn ở tin đầu dạng:
  [Thẻ: Inbox từ quảng cáo <TÊN POST> – <HEADLINE>]
Tách `<TÊN POST>` làm khoá nối. Chuẩn hoá trước khi gom:
- Bỏ hậu tố nhân bản: "- Bản sao", "- Bản sao 2", "_Group_1"… → gom về post gốc,
  NHƯNG giữ cột riêng ghi rõ đã gom những biến thể nào.
- Thẻ không phải quảng cáo (ví dụ "Ưu đãi và thông báo" = tin nhắn hàng loạt)
  → tách thành nhóm nguồn riêng, không xếp chung với post quảng cáo.
- Hội thoại không có thẻ → nhóm "Không rõ nguồn".

Báo ngay: tổng hội thoại · số nối được · số không nối được · số post duy nhất.

## A2. Chấm từng hội thoại (5 tín hiệu — giống doc/05)
① nêu dịch vụ cụ thể · ② mốc thời gian ≤14 ngày · ③ hỏi lịch/bác sĩ/chi phí theo
tình trạng mình · ④ gửi ảnh hoặc mô tả rõ · ⑤ để lại liên hệ và đồng ý nhận tư vấn
→ HOT 4–5 · WARM 2–3 · COLD 0–1.
Nếu đã chạy doc/05 cho cùng kỳ, DÙNG LẠI kết quả chấm đó, không chấm lại.

## A3. Tính cho từng post
- Số hội thoại
- Tỷ lệ có SĐT (%)        ← chỉ số quan trọng nhất, bám KPI xin số của trực page
- Số và tỷ lệ HOT / WARM / COLD
- Điểm tín hiệu trung bình (0–5)
- Tầng chủ đạo = tầng chiếm tỷ lệ cao nhất
- Rào cản nổi bật: đếm các dấu hiệu trong hội thoại thuộc post đó —
  hỏi giá ngay · ở xa/không chi nhánh · sợ đau · so sánh nơi khác ·
  chưa tài chính · hỏi người nhà · chỉ Zalo/không nghe máy
- Đủ mẫu? ≥10 hội thoại = Đủ · <10 = ⚠ chưa đủ mẫu, không kết luận

# CHẾ ĐỘ B — DỰ ĐOÁN TỪ NỘI DUNG
Chỉ dùng khi không có hội thoại. Chấm từng post theo 5 đặc trưng, mỗi cái 1 điểm:
① Nêu TÌNH TRẠNG CỤ THỂ để khách tự nhận ra mình (sụp mí, bọng mỡ, mí lệch)
   thay vì nói chung chung "làm đẹp"
② Nhắm ĐÚNG MỘT NHÓM khách (trung niên, khách sửa lại, người bận) thay vì nhắm tất cả
③ Nói về CHUYÊN MÔN (bác sĩ, quy trình, bệnh viện) thay vì chỉ nói giá
④ Có yếu tố GIẢM LO (giải đáp nỗi sợ, minh bạch quy trình)
⑤ CTA dẫn tới trao đổi tình trạng, thay vì chỉ "inbox nhận giá"

→ 4–5 điểm: dự đoán kéo HOT · 2–3: WARM · 0–1: COLD
Ghi rõ đây là DỰ ĐOÁN, phải đối chiếu lại khi có hội thoại thật.

# CẤU TRÚC FILE EXCEL — 7 sheet, đúng thứ tự

1. **Tổng quan**
   Kỳ · dịch vụ · chế độ chạy (A hay B) · nguồn dữ liệu · ngày lập.
   Số post · số hội thoại · số nối được · số không rõ nguồn.
   Phân bố HOT/WARM/COLD toàn kỳ.
   **Khối cảnh báo phương pháp**, ghi rõ:
   - mẫu có phải toàn bộ hội thoại trong kỳ không, hay đã bị lọc
   - nếu đã lọc (ví dụ "ưu tiên hội thoại dài") → ghi rõ kết quả bị thiên về phía nóng,
     chỉ dùng tham khảo, KHÔNG dùng để quyết ngân sách
   - số post chưa đủ mẫu
   3 kết luận chính, mỗi cái một dòng, có số kèm theo.

2. **Chú giải ký hiệu**
   Giải nghĩa: HOT/WARM/COLD và 5 tín hiệu · tỷ lệ có SĐT · điểm tín hiệu TB ·
   tầng chủ đạo · ⚠ chưa đủ mẫu · góc tiếp cận · các loại rào cản · quy ước màu.

3. **Phân tầng theo post** — một dòng mỗi post, cột đúng thứ tự:
   Mã post | Tên post (chuẩn hoá) | Biến thể đã gom | Dịch vụ | Thông điệp chính |
   Góc tiếp cận | Số HT | Tỷ lệ có SĐT | HOT | WARM | COLD | % HOT |
   Điểm TB | Tầng chủ đạo | Đủ mẫu? | Rào cản nổi bật
   → Sắp xếp theo % HOT giảm dần, nhưng đẩy mọi dòng ⚠ chưa đủ mẫu xuống cuối.

4. **Xếp hạng & khuyến nghị** — cột:
   Hạng | Mã post | % HOT | Tỷ lệ có SĐT | Khuyến nghị | Lý do | Việc cần làm
   Khuyến nghị chọn trong 4 mức:
   - TĂNG NGÂN SÁCH — %HOT và tỷ lệ có SĐT đều trên trung bình kỳ
   - GIỮ NGUYÊN — quanh mức trung bình
   - SỬA THÔNG ĐIỆP — kéo được nhiều hội thoại nhưng tầng thấp, nêu sửa gì cụ thể
   - XEM XÉT TẮT — vừa ít hội thoại vừa tầng thấp
   Post ⚠ chưa đủ mẫu → khuyến nghị bắt buộc là "CHỜ THÊM DỮ LIỆU".

5. **Góc tiếp cận → tầng** — quy luật rút ra được, cột:
   Góc tiếp cận | Post đại diện | Số HT gộp | % HOT gộp | Tầng thường kéo về |
   Vì sao | Dùng khi nào
   Các góc tiếp cận cần phân biệt:
   - Giá / ưu đãi ("giá tốt nhất", nêu con số giá)
   - Tốc độ hồi phục ("hồi phục nhanh x2", "7 ngày là đẹp")
   - Tình trạng cụ thể ("hết sụp mí, bọng mỡ", "trẻ ra 5 tuổi")
   - Giáo dục / giải đáp lo lắng ("1001 điều lo lắng", "tại sao đẹp không lộ")
   - Chuyên môn / bác sĩ / bệnh viện
   - Banner thông báo chương trình
   → Chỉ kết luận khi tổng hội thoại của góc đó ≥10. Chưa đủ thì ghi ⚠.

6. **Rào cản theo post** — post nào đẻ ra rào cản gì, cột:
   Mã post | Rào cản | Số ca | % trên tổng HT của post | Hàm ý cho thông điệp |
   Kịch bản cần chuẩn bị (mã S3.x / X.x)
   → Dùng để biết post nào cần sửa thông điệp từ gốc, post nào chỉ cần
     trang bị trước kịch bản xử lý cho trực page.

7. **Dữ liệu thô** — để kiểm chứng lại, cột:
   STT HT | Tên KH | Ngày | Thẻ nguồn gốc (nguyên văn) | Mã post sau chuẩn hoá |
   Có SĐT | Bitmask tín hiệu | Độ nóng
   → Bắt buộc có sheet này. Không có thì không ai kiểm được con số ở sheet 3.

# KHI CHẠY NHIỀU KỲ
Nếu được cho từ 2 kỳ trở lên (ví dụ tháng 7 và tháng 10), thêm sheet cuối:
**So sánh kỳ** — cột: Góc tiếp cận | % HOT kỳ 1 | % HOT kỳ 2 | Chênh lệch | Nhận định
→ Chỉ so sánh ở mức GÓC TIẾP CẬN, không so sánh từng post, vì post thường đổi
  tên và nhân bản giữa các kỳ nên không khớp 1-1.
→ Nêu rõ hai kỳ có cùng cách lấy mẫu không. Khác cách lấy mẫu thì không so sánh được.

# QUY TẮC
- Mọi con số phải đếm được từ dữ liệu. Không ước lượng, không làm tròn đẹp.
- Post dưới 10 hội thoại: ghi ⚠ chưa đủ mẫu, KHÔNG xếp hạng, KHÔNG khuyến nghị.
- Không suy ra hiệu quả quảng cáo từ nội dung post khi đã có dữ liệu thật.
- Không đưa số điện thoại hay thông tin định danh khách vào file.
- Chỉ số ưu đãi/giá xuất hiện trong post thì trích nguyên văn và gắn ⚠.

# TRÌNH BÀY
Font Arial · freeze dòng tiêu đề · wrap text cột dài · tiêu đề nền đậm chữ trắng.
Màu: đỏ nhạt HOT · cam WARM · xanh dương nhạt COLD · vàng mọi ô ⚠ ·
xanh lá nhạt khuyến nghị TĂNG NGÂN SÁCH · xám dòng chưa đủ mẫu.

# CÁCH LÀM — theo thứ tự
1. Đọc dữ liệu. Báo: số post · số hội thoại · số nối được qua thẻ · số không rõ nguồn.
2. Liệt kê danh sách post sau chuẩn hoá, kèm các biến thể đã gom vào.
   DỪNG LẠI cho tôi xác nhận việc gom có đúng không.
3. Chấm và tính chỉ số từng post.
4. In bảng tóm tắt: post · số HT · %HOT · tỷ lệ có SĐT · đủ mẫu chưa.
   DỪNG LẠI cho tôi xác nhận con số.
5. Ghi file Excel.
6. Tự kiểm và báo: tổng HT ở sheet 3 có bằng tổng ở sheet 7 không ·
   có post nào <10 HT mà vẫn bị xếp hạng không · còn số nào chưa gắn ⚠ không.
````

## Đến đây

---

## Chuẩn bị dữ liệu đầu vào

Danh sách post nên có tối thiểu: **tên post đúng như hiển thị trong thẻ Caresoft** (đây là khoá nối, sai tên là không nối được) · nội dung/headline · dịch vụ · thời gian chạy. Có thêm chi tiêu, reach, số inbox thì tốt — nhưng không bắt buộc, vì prompt này đo chất lượng lead chứ không đo chi phí.

Muốn ra được **chi phí trên một lead HOT** thì cần thêm cột chi tiêu từng post. Nói tôi bổ sung phần đó vào prompt.

## Chạy cho tháng 7

Tháng 7 chỉ chạy được **chế độ A** nếu còn log hội thoại tháng 7 trong Caresoft. Nếu không còn, chế độ B chỉ cho ra giả thuyết — và giả thuyết về một kỳ đã qua thì không dùng được việc gì. Nên kiểm tra khả năng xuất hội thoại tháng 7 trước khi bắt đầu.

Nếu có cả hai kỳ, so sánh ở mức **góc tiếp cận** chứ đừng so từng post: post hay bị nhân bản và đổi tên giữa các kỳ (`- Bản sao`, `- Bản sao 2`, `_Group_1`) nên không khớp 1-1 được.
