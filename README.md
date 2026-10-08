# 🏭 AGENT FACTORY — Meta-agent sinh agent CSKH (Kangnam)

> Version 2.0 · **Một meta-agent sinh ra 4 agent CSKH**, dùng chung bộ module thương hiệu. Ngoài việc tạo agent, nó còn **trả lời câu hỏi về luồng vận hành** — trạng thái L-code, routing, quy ước KB, handoff.

Theo công thức HCI **R·M·K·W·O (+Rules)**. Kiến trúc **lõi brand-neutral** ([`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md)) + **module thương hiệu** ([`knowledge/K1–K7`](knowledge/)) + **template agent con** ([`templates/A1–A4`](templates/)) → **đổi brand = đổi module K, không sửa lõi**.

---

## Nguyên tắc tối thượng

> **Một agent = một vai trò chuyên sâu. Càng hẹp càng giỏi.**

Tạo agent **theo CÔNG VIỆC, không theo phòng ban**. Một agent ôm "tư vấn + chấm điểm + nhắc lịch" sẽ làm cả ba đều tệ — tách thành A1, A2, A4 thì mỗi cái mới đủ sâu.

> **Agent chỉ GỢI Ý, người duyệt trước khi gửi khách.**

AI **không** thao tác trực tiếp trên Caresoft/ERP ở Phase 1: nhân viên copy hội thoại cho agent → agent trả gợi ý → nhân viên dán lại.

---

## Bốn agent sinh ra được

| Agent | Việc | Module nạp |
|---|---|---|
| **A1 Tư vấn** (trực page) | Gợi ý nội dung trả lời khách | K1 · K2 · K3 · K4 · K5 · K6 · K7 |
| **A2 QC** | Chấm điểm, phân loại Hot/Warm, báo lỗi NV, action plan đào tạo | K3 · K5 · K6 (+ rubric trong A2) |
| **A3 Lead Scoring** | Chấm 2 luồng (hội thoại + cuộc gọi), xếp hạng A/B/C/D | K3 · K5 · K6 (+ tiêu chí trong A3) |
| **A4 Nhắc lịch** | Sinh lịch nhắc & chăm sóc theo nhịp | K3 (Existing/LTV) · K4 · K5 §7 · K6 |

---

## Hai chế độ

| Mode | Khi nào dùng | Đầu ra |
|---|---|---|
| **TẠO AGENT** | *"Tạo agent tư vấn cho dịch vụ nâng mũi"* | Phiếu 6 ô + system prompt agent con chạy được + bảng test 4 tiêu chí |
| **HỎI VẬN HÀNH** | *"Khách cho số rồi gọi không nghe là trạng thái gì?"* | Trả lời ngắn + trích đúng **L-code** và **mã KB** |

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
3. **Knowledge:** upload 7 module trong [`knowledge/`](knowledge/) + 4 template trong [`templates/`](templates/).
4. Ra lệnh tạo agent, hoặc hỏi thẳng câu vận hành.

**Câu lệnh mẫu:**
```
Tạo agent tư vấn cho dịch vụ nâng mũi.
```
```
Khách cho SĐT rồi gọi không nghe là trạng thái gì, dùng KB nào, ai xử lý?
→ L5.3 · Missed call_KB · A4 nhắc + A3 chấm Luồng 2
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

## Tài liệu

| File | Nội dung | Trạng thái |
|---|---|---|
| [SYSTEM-PROMPT.md](SYSTEM-PROMPT.md) | Bộ não meta-agent — 15 mục · **10.226 ký tự** | ✅ |
| [SYSTEM-PROMPT-NGAN.md](SYSTEM-PROMPT-NGAN.md) | Bản ngắn **6.765 ký tự** — chỉ cho **ChatGPT** (ô Instructions giới hạn 8.000) | ✅ |
| [knowledge/K1-thuong-hieu.md](knowledge/K1-thuong-hieu.md) | Thương hiệu Kangnam — trích yếu cho agent | ✅ |
| [knowledge/K2-khach-hang.md](knowledge/K2-khach-hang.md) | Chân dung · insight cảm xúc · key tâm lý theo nhóm | ✅ |
| [knowledge/K3-hanh-vi-trang-thai.md](knowledge/K3-hanh-vi-trang-thai.md) | **Bản đồ 6 giai đoạn ↔ L1–L6 ↔ agent** | ✅ |
| [knowledge/K4-dich-vu.md](knowledge/K4-dich-vu.md) | Dịch vụ · USP · 22 hồ sơ bác sĩ · bảng giá | ⚠ xem §Việc còn treo |
| [knowledge/K5-kich-ban.md](knowledge/K5-kich-ban.md) | Bank kịch bản · 8 lỗi cấm · 8 quy tắc vàng · luồng 7 bước | ⚠ một số slot KB còn trống |
| [knowledge/K6-van-hanh.md](knowledge/K6-van-hanh.md) | **Xương sống** — L1–L6 · routing · KB · handoff · điều kiện thoát | ⚠ routing L2.3/L2.4/L5/L6 còn trống |
| [knowledge/K7-chien-dich-thang.md](knowledge/K7-chien-dich-thang.md) | **HOT-SWAP** — bản hiện tại T10/2026 | 🔄 thay mỗi tháng |
| [templates/A1-tu-van-truc-page.md](templates/A1-tu-van-truc-page.md) | Template agent tư vấn | ✅ |
| [templates/A2-qc.md](templates/A2-qc.md) | Template agent QC + **Rubric v1** | ⚠ rubric chờ duyệt |
| [templates/A3-lead-scoring.md](templates/A3-lead-scoring.md) | Template agent lead scoring + **bộ tiêu chí ± v1** | ⚠ tiêu chí chờ duyệt |
| [templates/A4-nhac-lich.md](templates/A4-nhac-lich.md) | Template agent nhắc lịch | ✅ |
| [doc/01-cai-dat.md](doc/01-cai-dat.md) | Tên & mô tả · cài 3 nền tảng · smoke test · xử lý sự cố | ✅ |
| [doc/02-cau-lenh.md](doc/02-cau-lenh.md) | Câu lệnh 2 mode · prompt mẫu · điều Agent sẽ từ chối | ✅ |
| [doc/03-output-mau.md](doc/03-output-mau.md) | Output mẫu cả 2 mode · dấu hiệu đúng/sai | ✅ |
| [doc/04-prompt-nguoi-moi.md](doc/04-prompt-nguoi-moi.md) | 10 prompt cho nhân viên vận hành | ✅ |
| [doc/CHANGELOG.md](doc/CHANGELOG.md) | Lịch sử · việc còn treo | ✅ |
| [doc/v1-ban-goc-brain.md](doc/v1-ban-goc-brain.md) | Bản gốc `00-FACTORY.md` v1.0 — lưu đối chiếu, **không dùng để cài** | 📦 |

> **Quy ước:** mã `K1–K7` và `A1–A4` là **từ vựng vận hành**, được tham chiếu khắp các module và trong hội thoại hàng ngày — **không đổi tên**.

---

## Ranh giới

Human-in-the-loop · không cam kết kết quả tuyệt đối ("đẹp 100%", "an toàn tuyệt đối", "tương thích 100%") · không chẩn đoán/kê đơn · không báo giá cứng chưa xác minh · kiểm chứng mọi con số từ K7 · không bịa bác sĩ/ca bệnh/giải thưởng/case · chỉ nêu bác sĩ **đã được duyệt quảng bá**, không trích số ca chưa xác minh · không nạp CCCD/hồ sơ bệnh án/ảnh khách lên công cụ công cộng · **nhóm khách có thể là vị thành niên** → nội dung phù hợp lứa tuổi, hướng có giám hộ.

**Yêu cầu về cơ xương khớp / bảo tồn khớp** thuộc thương hiệu riêng **Cơ Xương Khớp – Wellness**, có agent riêng [`Agent-CoXuongKhop`](../Agent-CoXuongKhop/) — không sinh agent CSKH thẩm mỹ cho line đó.

Mọi agent sinh ra là **bản đề xuất**, phải qua người duyệt trước khi chạy thật.
