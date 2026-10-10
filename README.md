# 🏭 AGENT FACTORY — Meta-agent sinh agent CSKH (Kangnam)

> Version 2.2 · **Meta-agent dựng hệ 5 agent CSKH.** Nó trả lời ở **tầng hệ thống** — hệ làm được gì · vận hành thế nào · phát triển tới đâu · phải giải đề bài nào để tích hợp — và sinh ra system prompt cho agent con.
>
> **Không xử lý tình huống của một khách cụ thể** — đó là việc của agent con mà nó sinh ra.

Theo công thức HCI **R·M·K·W·O (+Rules)**. Kiến trúc **lõi brand-neutral** ([`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)) + **module thương hiệu** ([`knowledge/K1–K8`](knowledge/)) + **template agent con** ([`templates/A1–A5`](templates/)) → **đổi brand = đổi module K, không sửa lõi**.

---

## Nguyên tắc tối thượng

> **Một agent = một vai trò chuyên sâu. Càng hẹp càng giỏi.**

Tạo agent **theo CÔNG VIỆC, không theo phòng ban**. Một agent ôm "tư vấn + chấm điểm + nhắc lịch" sẽ làm cả ba đều tệ — tách thành A1, A2, A4 thì mỗi cái mới đủ sâu.

> **Agent chỉ GỢI Ý, người duyệt trước khi gửi khách.**

AI **không** thao tác trực tiếp trên Caresoft/ERP ở Phase 1: nhân viên copy hội thoại cho agent → agent trả gợi ý → nhân viên dán lại.

---

## Năm agent sinh ra được

| Agent | Việc | Module nạp |
|---|---|---|
| **A1 Tư vấn** (trực page) | Gợi ý nội dung trả lời khách | K1–K7 · **K8 trừ §1** |
| **A2 QC** | Chấm hội thoại theo **rubric 10 tiêu chí**, báo lỗi NV, action plan đào tạo | K3 · K5 · K6 · **K8 §6 §2 §4** |
| **A3 Lead Scoring** | Chấm **5 tín hiệu → HOT/WARM/COLD**, gắn SLA tương ứng | K3 · K5 · K6 · **K8 §3 §4** |
| **A4 Nhắc lịch** | Sinh lịch nhắc theo **chuỗi T+0→T+7** | K3 · K4 · K6 · **K8 §5 §4** |
| **A5 Tái khai thác** | Sinh nội dung chạm lại **tệp nguội** — chưa cho số, hoặc đã cho số quá 6 ngày. **Không quản lý lịch** | K2 · K3 · K4 · K5 · K6 · K7 · **K8 §2 §5 (trừ §1)** |

---

## Năm chế độ

| Mode | Hỏi gì | Nhận lại |
|---|---|---|
| **NĂNG LỰC** | *"Hệ này làm được gì?"* | Bản đồ năng lực + ranh giới + agent con nào phụ trách việc nào |
| **KIẾN TRÚC** | *"Hệ vận hành thế nào?"* | 5 lớp · state machine L1–L6 · luồng đầu–cuối · **điểm tích hợp** |
| **LỘ TRÌNH** | *"Phát triển tới đâu?"* | Bảng 4 phase + **điều kiện mở khoá** từng phase |
| **ĐỀ BÀI** | *"Cần giải gì để tích hợp?"* | 12 bài toán + mức chặn + người sở hữu |
| **SINH AGENT** | *"Tạo agent [loại] cho [X]"* | Phiếu 6 ô → module đã nạp → system prompt → bảng test 4 tiêu chí |

**Bốn mode đầu là lý do Factory tồn tại.** Câu hỏi về một khách cụ thể → Factory chỉ rõ agent con nào phụ trách rồi dừng.

---

## Xương sống: trạng thái L1–L6

QC gán L-code → Lead Scoring chấm theo L-code → A1 chọn kịch bản theo L-code → A4 lên nhịp theo L-code.
**Sai L-code là sai toàn bộ dây chuyền.**

| Level | Mã | Nghĩa | Nhiệt |
|---|---|---|---|
| **L1** Tương tác mới | L1.1 | Lần đầu nhắn, chưa tư vấn | Cold |
| **L2** Đang tư vấn | L2.1 · L2.3 · L2.4 · L2.5 | Tiềm năng · chưa phản hồi · hẹn nhắn lại · xa chi nhánh | Warm → Cool |
| **L4** Cơ hội mới | L4.1 | **Có SĐT + dịch vụ quan tâm** → chuyển Sales | Hot |
| **L5** Đang kết nối | L5.3 · L5.4 · L5.5 · L5.6 | Không nghe máy · không muốn nghe · hẹn gọi lại · chỉ Zalo | Hot |
| **L6** Cơ hội ≤30 ngày | L6.1 … L6.6 | Chưa rõ rào cản · so sánh · chưa có tiền · chưa có thời gian · sợ đau · hỏi người thân | Warm→Hot |

**Nhịp theo dõi L6 (chưa booking): D+3 → D+7 → D+15.**

**Quy ước KB:** `No Number_KB` → L2.x · `Call-back_KB` → L5.5 · `Missed call_KB` → L5.3 · `Take care_KB` → L6.x

---

## Quy trình tạo agent — 5 bước

```
① Phiếu 6 ô  →  ② Chọn template A  →  ③ Nạp module K  →  ④ Ráp instruction
                                                              ↓
                                    ⑤ Test 4 tiêu chí: có logic · có KPI
                                       · có timeline/nhịp · có action plan
                                              chưa đạt → sửa → test lại
```

**Chưa đạt 4 tiêu chí thì không xuất.**

---

## Quick start (4 bước)

1. Tạo 1 Project / GPT / Gem mới. Tên và mô tả ngắn: xem [`doc/01-cai-dat.md` §0](doc/01-cai-dat.md).
2. **Instructions:** dán khối ▼▲ trong [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) — riêng **ChatGPT** dùng [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md).
3. **Knowledge:** upload 8 module trong [`knowledge/`](knowledge/) + 4 template trong [`templates/`](templates/).
4. Ra lệnh tạo agent, hoặc hỏi thẳng câu vận hành.

**Câu lệnh mẫu:**
```
Để tích hợp hệ này vào vận hành thật, cần giải những đề bài nào?
Xếp theo mức chặn, nói rõ ai sở hữu từng cái.
```
```
Tạo agent tư vấn cho dịch vụ nâng mũi. Đưa phiếu 6 ô cho mình duyệt trước.
```

---

## ⚠️ K7 là module HOT-SWAP — thay mỗi tháng

**Mọi con số ưu đãi · giá · ngày · số suất · hotline lấy từ `K7` bản hiện hành.** K7 có hạn sử dụng.

**Bảo trì cuối mỗi tháng:**
1. Đổi tên bản cũ → `K7-2026-10.md`
2. Tạo `K7-chien-dich-thang.md` mới cho tháng sau
3. **Không đụng K5 / lõi**

Agent chỉ đọc bản hiện hành → không chào nhầm ưu đãi cũ.

**Lỗi quá khứ phải chống:** giá mâu thuẫn (6tr ≠ 3tr) · số cơ sở mâu thuẫn (7 ≠ 10) · sai ngày chương trình.

**Bổ sung K5:** nhồi nội dung vào đúng slot `No Number / Call-back / Missed call / Take care_KB{n}`.

---

## ⚠️ K8 thay thế một số phần cũ

`K8` là **playbook vận hành thật đang chạy**, nên khi mâu thuẫn với module cũ thì **K8 thắng**:

| Nội dung | Bản cũ | Bản dùng |
|---|---|---|
| Phiếu bàn giao | K6 §6 — 8 trường | **K8 §4 — 12 trường** |
| Rubric chấm hội thoại | A2 — "v1 đề xuất" | **K8 §6 — 10 tiêu chí, chuẩn ≥8/10** |
| Tiêu chí chấm lead | A3 — "± v1 đề xuất" | **K8 §3 — 5 tín hiệu → HOT/WARM/COLD** |

**Hai trục phân loại, không gộp:** `L-code` = *trạng thái* (L4.1 là thời điểm bàn giao) · `HOT/WARM/COLD` = *mức ưu tiên* (quyết SLA + bậc Telesale). Một lead mang cả hai — thiết kế dữ liệu phải để **hai cột riêng**.

> 🔒 **K8 §1 là dữ liệu nhân sự nội bộ** — đánh giá hiệu suất của người có tên. **Không bao giờ** nhúng vào agent con hay nội dung gửi khách. Chỉ dùng khi trả lời về **đào tạo** và **định tuyến**.

---

## Tài liệu

| File | Nội dung | Trạng thái |
|---|---|---|
| [SYSTEM-PROMPT.md](SYSTEM-PROMPT.md) | Bộ não meta-agent — **17 mục** · **17.636 ký tự** | ✅ |
| [SYSTEM-PROMPT-NGAN.md](SYSTEM-PROMPT-NGAN.md) | Bản ngắn **7.976 ký tự** — chỉ cho **ChatGPT** · ⚠ **chỉ dư 24 ký tự, sửa phải đo lại** | ✅ |
| [knowledge/K1-thuong-hieu.md](knowledge/K1-thuong-hieu.md) | Thương hiệu Kangnam — trích yếu cho agent | ✅ |
| [knowledge/K2-khach-hang.md](knowledge/K2-khach-hang.md) | Chân dung · insight cảm xúc · key tâm lý theo nhóm | ✅ |
| [knowledge/K3-hanh-vi-trang-thai.md](knowledge/K3-hanh-vi-trang-thai.md) | **Bản đồ 6 giai đoạn ↔ L1–L6 ↔ agent** | ✅ |
| [knowledge/K4-dich-vu.md](knowledge/K4-dich-vu.md) | Dịch vụ · USP · 22 hồ sơ bác sĩ · bảng giá | ⚠ xem §Việc còn treo |
| [knowledge/K5-kich-ban.md](knowledge/K5-kich-ban.md) | Bank kịch bản · 8 lỗi cấm · 8 quy tắc vàng · luồng 7 bước | ⚠ một số slot KB còn trống |
| [knowledge/K6-van-hanh.md](knowledge/K6-van-hanh.md) | **Xương sống** — L1–L6 · routing · KB · handoff · điều kiện thoát | ⚠ routing L2.3/L2.4/L5/L6 còn trống |
| [knowledge/K7-chien-dich-thang.md](knowledge/K7-chien-dich-thang.md) | **HOT-SWAP** — bản hiện tại T10/2026 | 🔄 thay mỗi tháng |
| [knowledge/K8-nang-luc-kich-ban-ban-giao.md](knowledge/K8-nang-luc-kich-ban-ban-giao.md) | **Playbook vận hành thật** — kịch bản B1–B5 · HOT/WARM/COLD · SLA bàn giao · chuỗi T+0→T+7 · rubric 10 tiêu chí · KPI · năng lực nhân sự | ⚠ §1 là dữ liệu nội bộ |
| [templates/A1-tu-van-truc-page.md](templates/A1-tu-van-truc-page.md) | Template agent tư vấn | ✅ |
| [templates/A2-qc.md](templates/A2-qc.md) | Template agent QC | ⚠ rubric v1 **đã bị K8 §6 thay thế** |
| [templates/A3-lead-scoring.md](templates/A3-lead-scoring.md) | Template agent lead scoring | ⚠ tiêu chí v1 **đã bị K8 §3 thay thế** |
| [templates/A4-nhac-lich.md](templates/A4-nhac-lich.md) | Template agent nhắc lịch | ✅ |
| [doc/01-cai-dat.md](doc/01-cai-dat.md) | Tên & mô tả · cài 3 nền tảng · smoke test · xử lý sự cố | ✅ |
| [doc/02-cau-lenh.md](doc/02-cau-lenh.md) | Câu lệnh 2 mode · prompt mẫu · điều Agent sẽ từ chối | ✅ |
| [doc/03-output-mau.md](doc/03-output-mau.md) | Output mẫu cả 2 mode · dấu hiệu đúng/sai | ✅ |
| [doc/04-prompt-nguoi-moi.md](doc/04-prompt-nguoi-moi.md) | Prompt mẫu | ✅ |
| [doc/CHANGELOG.md](doc/CHANGELOG.md) | Lịch sử · việc còn treo | ✅ |
| [doc/v1-ban-goc-brain.md](doc/v1-ban-goc-brain.md) | Bản gốc `00-FACTORY.md` v1.0 — lưu đối chiếu, **không dùng để cài** | 📦 |

> **Quy ước:** mã `K1–K8` và `A1–A5` là **từ vựng vận hành**, được tham chiếu khắp các module và trong hội thoại hàng ngày — **không đổi tên**.

---

## Ranh giới

Human-in-the-loop · không cam kết kết quả tuyệt đối ("đẹp 100%", "an toàn tuyệt đối", "tương thích 100%") · không chẩn đoán/kê đơn · không báo giá cứng chưa xác minh · kiểm chứng mọi con số từ K7 · không bịa bác sĩ/ca bệnh/giải thưởng/case · chỉ nêu bác sĩ **đã được duyệt quảng bá**, không trích số ca chưa xác minh · không nạp CCCD/hồ sơ bệnh án/ảnh khách lên công cụ công cộng · **nhóm khách có thể là vị thành niên** → nội dung phù hợp lứa tuổi, hướng có giám hộ.

**Yêu cầu về cơ xương khớp / bảo tồn khớp** thuộc thương hiệu riêng **Cơ Xương Khớp – Wellness**, có agent riêng [`Agent-CoXuongKhop`](../Agent-CoXuongKhop/) — không sinh agent CSKH thẩm mỹ cho line đó.

Mọi agent sinh ra là **bản đề xuất**, phải qua người duyệt trước khi chạy thật.
