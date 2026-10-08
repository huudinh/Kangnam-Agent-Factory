# K8 — NĂNG LỰC NHÂN SỰ · KỊCH BẢN · BÀN GIAO TELESALE
Module brand-specific. Nguồn: **Playbook Trực Page Kangnam Tháng 10**. Cập nhật: 2026-10-08.

> **Module này SIÊU VIỆT HƠN một số phần trong K5/K6 và A2/A3** — xem §0 để biết chỗ nào K8 thay thế, chỗ nào bổ sung. Khi mâu thuẫn: **K8 thắng**, vì đây là bản vận hành thật đang chạy.

---

## §0. QUAN HỆ VỚI MODULE KHÁC — ĐỌC TRƯỚC

| Nội dung | Trước ở đâu | Bây giờ |
|---|---|---|
| **Phiếu bàn giao** | K6 §6 — 8 trường | **K8 §4 — 12 trường + link hội thoại + tên trực page.** K8 thay thế |
| **Rubric chấm hội thoại** | A2 — "rubric v1 đề xuất" | **K8 §6 — bảng 10 tiêu chí, chuẩn ≥8/10.** K8 thay thế |
| **Tiêu chí chấm lead** | A3 — "bộ tiêu chí ± v1 đề xuất" | **K8 §3 — 5 tín hiệu → HOT/WARM/COLD.** K8 thay thế |
| **Nhịp chăm sóc** | K5 §7 · K6 nhịp L6 (D+3/D+7/D+15) | **K8 §5 — chuỗi T+0 → T+7.** Hai nhịp khác mục đích: T-series cho **ngay sau khi xin được số**, D-series cho **L6 đã gọi mà chưa booking**. Dùng cả hai, đúng chỗ |
| **Kịch bản tư vấn** | K5 bank kịch bản theo L-code | **K8 §2 — khung 5 bước B1–B5 + 5 lý do từ chối.** K8 là khung chuẩn; K5 là nội dung chi tiết theo dịch vụ |
| **Trạng thái L1–L6** | K6 §2 | **Giữ nguyên.** L-code và HOT/WARM/COLD là **hai trục khác nhau** — xem §3 |

---

## §1. NĂNG LỰC NHÂN SỰ & PHÂN CÔNG

> ⚠️ **DỮ LIỆU NỘI BỘ.** Phần này chứa đánh giá hiệu suất của người có tên. **Tuyệt đối không xuất hiện trong bất kỳ nội dung nào gửi khách**, không đưa vào system prompt của agent tư vấn (A1). Chỉ dùng cho: phân công mentor · thiết kế đào tạo · định tuyến cặp cố định.

Đánh giá **17 nhân viên** qua 3 khâu phễu: **xin số → kết nối → chốt lịch**.

| Nhóm | Đặc điểm | Người | Cần học phần |
|---|---|---|---|
| **A — Hạt nhân (mentor)** | Mạnh, đi dạy lại | **Mai Hải Anh** (chốt lịch 53% — tốt nhất; kết nối 69% cần cải thiện) → mentor **M3** · **Nguyễn Thị Ngọc Hoa** (kết nối 78% — tốt nhất, toàn phễu cân bằng) → mentor **M2** · **Đặng Thị Liên** (ổn định cả 3 khâu) → chuẩn hoá quy trình | — |
| **B — Chốt lịch yếu** | Xin số tốt 42–47%, chốt lịch chỉ 40–45% | Nguyễn Văn Thành · Nguyễn Thị Hoài Linh · Kiều Thị Hương · Đặng Thị Thu Hương · Nguyễn Thị Mai · Trương Mỹ Thùy Linh | **M3** |
| **C — Kết nối yếu** | Kết nối 69–71%, dao động mạnh | Ngô Minh Ngọc · Cà Thị Thắm · Nguyễn Thị Hồng Lương · Trần Mỹ Chung | **M2** (xác thực số) |
| **D — Xin số yếu / tân binh** | Vũ Thị Linh Trang xin số 33% (thấp nhất) · Trương Tuyết Nhi và Hoàng Mỹ Linh là tân binh | | **M1**, tân binh kèm cả **M1–M3** |

> **Hoàng Mỹ Linh:** đánh giá kết thúc thử việc nếu không đạt 11% sau 2 tuần.

**Cách Factory dùng dữ liệu này:** chỉ để trả lời câu hỏi về **thiết kế đào tạo** và **định tuyến**. Khi sinh agent, dữ liệu này **không được nhúng vào system prompt** — agent con không cần biết ai yếu khâu nào.

---

## §2. KỊCH BẢN TƯ VẤN — KHUNG 5 BƯỚC B1–B5

| Bước | Làm gì | Câu mẫu |
|---|---|---|
| **B1 · Mở** | Chào, **gọi đúng tên dịch vụ theo quảng cáo khách vừa bấm** | *"…hỏi chị đang muốn cải thiện điểm nào nhất ạ?"* |
| **B2 · Khám phá** | Thu **đủ 3 thông tin bắt buộc**: tình trạng · mong muốn · thời gian dự kiến | |
| **B3 · Tạo tin cậy** | Nói về quy trình và bác sĩ, **không hứa kết quả** | *"Bác sĩ sẽ thăm khám chọn phương án phù hợp… do bác sĩ chuyên khoa trực tiếp."* Dùng case **đã công bố** |
| **B4 · Xin số** | **Luôn kèm lý do + hỏi khung giờ** | *"Để bác sĩ đánh giá đúng… chị cho em xin số điện thoại (có Zalo) nhé. Chị tiện nghe máy khung giờ nào ạ?"* |
| **B5 · Xác nhận** | **Báo tên Telesale · số gọi · giờ gọi** | *"Khoảng [thời gian], chị [tên Telesale] sẽ gọi chị từ số [hotline]… để ý máy giúp em."* |

> **B5 là bước làm tăng tỷ lệ kết nối nhiều nhất.** Bỏ B5 là mất lead ở khâu đắt nhất — số đã xin được rồi mà không gọi được.

### Xử lý 5 lý do từ chối

| Khách nói | Hướng trả lời |
|---|---|
| *"Giá bao nhiêu?"* | Nêu **khung giá tham khảo**; chi phí cuối phụ thuộc tình trạng sau thăm khám; xin số để bác sĩ báo |
| *"Có đau không?"* | **Trung thực**: có sưng đau trong hồi phục; Kangnam hạn chế sưng đau; mời trao đổi với bác sĩ |
| *"Để sắp xếp đã"* | Đặt lịch **thăm khám** trước, đưa **2 khung giờ cụ thể** |
| *"Hỏi người nhà đã"* | Mời người nhà **đi cùng buổi thăm khám**, gửi thông tin bác sĩ chia sẻ |
| *"Xem thêm vài nơi"* | Gợi **bộ tiêu chí so sánh**: cấp phép · bác sĩ mổ chính · quy trình · tái khám. **Không nêu tên đối thủ** |

### Từ cấm — vi phạm là hội thoại bị tính **0/10**
`cam kết 100%` · `tốt nhất` · `không đau` · `an toàn tuyệt đối`

---

## §3. PHÂN LOẠI HOT / WARM / COLD

**5 tín hiệu, mỗi tín hiệu 1 điểm:**
① Nêu **dịch vụ cụ thể** (*"nâng mũi"*, không phải *"tư vấn làm đẹp"*) · ② Thời gian dự kiến **≤14 ngày** · ③ Hỏi lịch, bác sĩ, hoặc **chi phí theo tình trạng của mình** · ④ Gửi ảnh / mô tả rõ tình trạng · ⑤ Đồng ý nhận cuộc gọi **trong khung giờ cụ thể**

| Mức | Điểm | Nghĩa | Ai nhận |
|---|---|---|---|
| **HOT** | 4–5 | Sẵn sàng đặt lịch | **Ưu tiên tuyệt đối** — Telesale giỏi nhất |
| **WARM** | 2–3 | Quan tâm rõ, chưa có thời gian / đang so sánh | Cần tư vấn sâu |
| **COLD** | 0–1 | Hỏi tham khảo, thời gian >60 ngày | Nuôi dưỡng bằng chuỗi chạm |

### ⚠️ HOT/WARM/COLD và L-code là HAI TRỤC KHÁC NHAU
- **L-code** = *trạng thái vận hành* của lead (đang ở đâu trong luồng). L4.1 là **thời điểm** bàn giao.
- **HOT/WARM/COLD** = *mức ưu tiên* khi bàn giao (quyết định SLA và bậc Telesale nào nhận).

Một lead có **cả hai**: vd `L4.1 · HOT` → chuyển Telesale bậc 1, gọi trong ≤5 phút.
Khi thiết kế trường dữ liệu: đây là **hai cột riêng**, không gộp.

---

## §4. BÀN GIAO TELESALE

**Luồng:** xin số + **xác thực Zalo** → chấm HOT/WARM/COLD → **phiếu bàn giao trên CRM** → định tuyến đúng Telesale → gọi theo SLA.

### Phiếu bàn giao — 12 trường bắt buộc
`Họ tên` · `SĐT` · `Zalo` · `Dịch vụ` · `Tình trạng` · `Mong muốn` · `Mối lo chính` · `Thời gian dự kiến` · `Khung giờ tiện` · `Điểm phân loại` · `Link hội thoại` · `Tên trực page`

> Thiếu trường nào thì Telesale gọi điện sẽ phải hỏi lại khách từ đầu — khách khó chịu và mất lợi thế.

### SLA gọi — theo khung giờ nhận số

| Khung giờ nhận số | HOT | WARM | COLD |
|---|---|---|---|
| **8h–12h · 13h30–17h30** | ≤ 5' | ≤ 30' | Nhắn Zalo ≤2h, gọi trong ngày |
| **12h–13h30** (trưa) | ≤ 15' | Gọi trước 14h | Gọi trong ngày |
| **17h30–21h** (cao điểm) | ≤ 10' | ≤ 60' hoặc đúng giờ hẹn | Hàng đợi sáng hôm sau |
| **21h–8h** | Nếu khách đồng ý tối: ≤15' | 8h30–10h | 10h–12h |

**Giới hạn tải:** mỗi Telesale ~**8 số HOT/giờ**. Vượt → chuyển sang người **cùng bậc** đang rảnh.

### Bậc Telesale & định tuyến
- **Bậc 1** — HOT dịch vụ **phẫu thuật**
- **Bậc 2** — HOT dịch vụ khác · WARM phẫu thuật
- **Bậc 3 / mới** — WARM còn lại · COLD · danh sách tái khai thác

**Cặp cố định:** mỗi page có **1 trực page + 1–2 Telesale** phụ trách chính, để hai bên **cùng chịu chỉ số** kết nối và booking.

### Vòng phản hồi Telesale → Trực page

| Trạng thái | Cập nhật trong | Trực page làm tiếp |
|---|---|---|
| **Đã booking** | Ngay | Nhắn xác nhận · gửi địa chỉ · nhắc 1 ngày trước |
| **Kết nối, chưa booking** (kèm lý do) | ≤ 30' | Nhắn theo **đúng lý do** trong 24h |
| **Không nghe máy** | ≤ 30' | Nhắn hỏi lại khung giờ (T+30') |
| **Hẹn gọi lại** | Ngay | Nhắc khách **15' trước** |

---

## §5. CHUỖI CHĂM SÓC SAU XIN SỐ — T+0 → T+7

| Mốc | Việc |
|---|---|
| **T+0 ≤ 2'** | Nhắn xác nhận: tên Telesale · số sẽ gọi · giờ gọi |
| **T+30'** | Kiểm tra phản hồi. Chưa nghe máy → *"Chị tiện nghe máy khung giờ nào để em báo bác sĩ sắp xếp ạ?"* |
| **T+2h** | Gửi nội dung giá trị (bác sĩ · quy trình), hỏi lại khung giờ |
| **T+24h** | Telesale gọi lần 2. Trực page **nhắn nhắc 15 phút trước** |
| **T+72h** | Mời sự kiện / chương trình, kèm lời mời đặt lịch |
| **T+7 ngày** | **Lần chạm cuối.** Không phản hồi → chuyển nhóm nuôi dưỡng dài hạn |

> **Trần số lần nhắn: tối đa 6 lần / 7 ngày. Khách từ chối → dừng ngay.**

---

## §6. BẢNG CHẤM HỘI THOẠI — 10 TIÊU CHÍ

Chuẩn đạt: **≥ 8/10**.

Mười tiêu chí: ① phản hồi trong 2' · ② gọi đúng tên dịch vụ · ③ thu đủ 3 thông tin · ④ tạo tin cậy · ⑤ xin số **có lý do** · ⑥ xác thực số/Zalo · ⑦ phân loại HOT/WARM/COLD · ⑧ lập phiếu bàn giao · ⑨ **không dùng từ cấm** · ⑩ nêu rõ bước tiếp theo.

> **Tiêu chí ⑨ vi phạm → toàn hội thoại 0 điểm**, bất kể 9 tiêu chí kia.

---

## §7. KẾ HOẠCH ĐÀO TẠO 4 TUẦN

| Học phần | Nội dung | Người học | Mentor |
|---|---|---|---|
| **M1** Mở hội thoại | Phản hồi 2' · chào theo dịch vụ · 3 câu khám phá nhu cầu | Linh Trang · Tuyết Nhi · Mỹ Linh · Thùy Linh | Thành |
| **M2** Xin số & xác thực | Xin **có lý do** · kiểm tra Zalo · hỏi khung giờ · nhắn xác nhận | Nhóm C, D + Hải Anh | Ngọc Hoa |
| **M3** Chốt lịch | Xử lý 5 lý do từ chối · đưa **2 khung giờ cụ thể** | Nhóm B + Lương, Chung, Tuyết Nhi, Mỹ Linh | Hải Anh |
| **M4** Chăm sóc sau xin số | Chuỗi chạm T+0 → T+7 | Toàn team | Trưởng team |
| **M5** Phân loại & bàn giao | HOT/WARM/COLD · phiếu · theo dõi phản hồi | Toàn team + Telesale | Trưởng team + Trưởng Telesale |

---

## §8. KPI & RỦI RO

**KPI vận hành:**
| Chỉ số | Mục tiêu |
|---|---|
| Số được phân loại + có phiếu đủ | **≥ 95%** |
| HOT được gọi **đúng SLA** | **≥ 90%** |
| Booking / HOT | **≥ 60%** |
| Booking / WARM | **≥ 35%** |
| Kết nối / SĐT | **≥ 78%** |
| Booking / Kết nối | **≥ 50%** |
| Điểm chấm hội thoại | **≥ 8/10** |
| Tỷ lệ khách đến cửa (show-up) | *(theo dõi, chưa đặt mốc)* |

**Mục tiêu tháng 10:** inbox → booking từ **13,7% → 16,5%**, nếu đạt cả 3 đòn bẩy: quy trình bàn giao · đào tạo theo khâu hổng · chăm sóc sau xin số.

**Rủi ro đã nhận diện:**
- **HOT tràn lan** (chấm rộng tay) → đối chiếu tỷ lệ booking **hằng tuần**
- **Telesale quá tải giờ cao điểm** → bố trí thêm ca tối
- **Nhắn quá nhiều** → trần 6 lần/7 ngày, dừng khi khách từ chối
- **Vi phạm từ ngữ** → chỉ dùng **câu mẫu đã duyệt**

---

## §9. CÁCH CÁC AGENT DÙNG K8

| Agent | Dùng phần nào |
|---|---|
| **A1** Tư vấn | §2 khung B1–B5 + 5 lý do từ chối + từ cấm · §5 chuỗi T+0→T+7 · §3 để gợi ý phân loại. **KHÔNG nạp §1** |
| **A2** QC | §6 bảng 10 tiêu chí (thay rubric v1) · §2 để biết bước nào thiếu · §4 kiểm phiếu đủ trường |
| **A3** Lead Scoring | §3 năm tín hiệu → HOT/WARM/COLD (thay tiêu chí v1) · §4 để biết SLA và bậc nào nhận |
| **A4** Nhắc lịch | §5 chuỗi T+0→T+7 · §4 vòng phản hồi Telesale |
| **Factory** | §1 để trả lời về đào tạo và định tuyến · §8 để trả lời về KPI và rủi ro |

## 🔶 Cần xác nhận
- Số liệu hiệu suất 17 nhân sự là **bản tháng 10/2026** — cần cập nhật khi có kỳ đánh giá mới.
- Mốc show-up chưa có — cần đặt trước khi đưa vào KPI chính thức.
- Nguồn: Playbook Trực Page Kangnam Tháng 10. **Xác nhận đây là bản đã duyệt** trước khi dùng để đánh giá nhân sự.
