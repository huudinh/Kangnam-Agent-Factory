# CHANGELOG — AGENT FACTORY (KANGNAM)

## v2.1 — 08/10/2026 · Nâng Factory lên tầng hệ thống

**Vấn đề của bản 2.0:** Factory có mode *"Hỏi vận hành"* dùng để tra cứu tình huống lẻ — *"khách cho số rồi gọi không nghe là mã gì"*. Đó là **việc của agent con** A1/A2 đã sinh ra. Factory sa vào đó thì vừa làm thay việc agent con, vừa loãng mất thứ nó giỏi nhất: **nhìn toàn hệ**.

**Bản 2.1 định nghĩa lại phạm vi.** Factory trả lời ở **TẦNG HỆ THỐNG** cho kỹ sư dựng hệ, quản lý sản phẩm, người quyết ngân sách — bốn câu hỏi nó phải luôn trả lời được:

| # | Câu hỏi | Mục |
|---|---|---|
| ① | Hệ này **làm được gì, không làm gì** | §5 |
| ② | Hệ **vận hành thế nào** — kiến trúc, state machine, luồng, điểm tích hợp | §7–§9 |
| ③ | **Đích đến phát triển** tới đâu | **§10 MỚI** |
| ④ | **Phải giải đề bài nào** để tích hợp được | **§11 MỚI** |

**§5 đổi từ 2 chế độ thành 5:** `NĂNG LỰC` · `KIẾN TRÚC` · `LỘ TRÌNH` · `ĐỀ BÀI` · `SINH AGENT`. Bốn mode đầu là lý do Factory tồn tại.

**§10 MỚI — Đích đến & lộ trình.** Bảng 4 phase kèm **điều kiện mở khoá** từng phase:

| Phase | Làm được gì | Mở khoá khi |
|---|---|---|
| **1 Trợ lý rời** *(hiện tại)* | Agent gợi ý, người copy/dán | Đang chạy |
| **2 Đọc tự động** | Agent đọc hội thoại từ Caresoft, tự gán L và chấm điểm | Có API đọc · chốt nguồn sự thật của L-code · có routing đầy đủ |
| **3 Ghi có kiểm soát** | Agent ghi tag/điểm ngược vào Caresoft, người duyệt ngoại lệ | P2 ổn định + có benchmark + có rollback |
| **4 Nhân bản brand** | Dùng lại lõi, chỉ thay module K | Xác nhận lõi thật brand-neutral |

> **Chỉ Phase 1 là đã chốt.** Phase 2–4 là **đề xuất chờ duyệt** — Rule 6c bắt Agent phải nói rõ điều này mỗi lần trình bày, không được nói như việc đã quyết.

**§11 MỚI — 10 đề bài phải giải để tích hợp.** Đây là **danh sách bài toán, không phải danh sách tính năng** — mỗi đề bài nêu vấn đề · vì sao chặn · ai sở hữu. Gồm: nguồn sự thật của L-code · routing còn trống · nội dung KB trống · chống ảo giác số liệu · pháp lý nội dung · đo lường · hạ tầng & quyền · bảo mật dữ liệu khách · lõi có thật brand-neutral · quản trị phiên bản K7.

Mục **Việc còn treo** dưới đây giờ là dữ liệu thiếu; **§11 là bài toán thiết kế** — hai thứ khác nhau, đừng lẫn.

**Thay đổi kèm theo**
- §1: thêm khối **NGOÀI PHẠM VI** — câu hỏi về một khách cụ thể thì chỉ rõ agent con nào phụ trách rồi **dừng**. Đối tượng đổi từ *"người vận hành"* sang *"kỹ sư dựng hệ, quản lý sản phẩm, người quyết ngân sách"*.
- §14 định dạng đầu ra: thêm khuôn xuất cho 4 mode mới.
- §16 Rules: thêm **6b** (không xử lý tình huống khách lẻ) và **6c** (không trình bày Phase 2–4 như đã chốt).
- `SYSTEM-PROMPT-NGAN.md` viết lại theo khung mới — **7.983 ký tự**, chỉ dư 17 so với hạn mức ChatGPT. **Sửa là phải đếm lại.**
- Trang hướng dẫn: Bước 2 mở đầu bằng bảng **4 câu hỏi + ranh giới ngoài phạm vi**; 12 câu lệnh bám 5 chế độ, 6 câu đầu ở tầng hệ thống.

---

## v2.0 — 08/10/2026 · Áp khuôn gói chuẩn

Nội dung chuyên môn **giữ nguyên hoàn toàn**. Gói này vốn đã có `knowledge/` và `templates/` nên chỉ thiếu lớp vỏ: bộ não dạng khối ▼▲, bản ngắn cho ChatGPT, và tài liệu vận hành.

**Cấu trúc mới**

```
Kangnam-Agent-Factory/
├── README.md               ← cổng vào
├── SYSTEM-PROMPT.md        ← bộ não 15 mục, khối ▼▲ (10.226 ký tự)
├── SYSTEM-PROMPT-NGAN.md   ← bản ngắn cho ChatGPT (6.765 ký tự)
├── knowledge/              ← 7 module K1–K7 · GIỮ NGUYÊN
├── templates/              ← 4 template A1–A4 · GIỮ NGUYÊN
└── doc/                    ← tài liệu vận hành, KHÔNG upload
```

**Quyết định: giữ nguyên tên thư mục `Kangnam-Agent-Factory`** — khớp với repo `github.com/huudinh/Kangnam-Agent-Factory` đã tạo. Hai gói Ads Optimize đổi được sang quy ước `Agent-*` vì lúc đó chưa có repo; gói này đã có nên giữ để không phải đổi remote.

**Quyết định: KHÔNG đổi tên file trong `knowledge/` và `templates/`**

Khác với các gói trước (nơi tôi đổi `K1_HO_SO_DICH_VU.md` → `cxk-ho-so-dich-vu.md`), ở đây mã **K1–K7** và **A1–A4** là **từ vựng vận hành**, không phải tên file tình cờ:

| Mã | Số lần được tham chiếu |
|---|---|
| K5 | 36 |
| K7 | 33 |
| K6 | 21 |
| A1 | 17 |
| K4 · A4 | 15 |
| K3 · A3 | 14 |
| A2 | 13 |
| K1 · K2 | 9 |

Người vận hành nói *"nạp K1–K7"*, *"nội dung nằm ở K5 §7"*, *"K6 §3 còn trống"* trong hội thoại hàng ngày. Đổi tên file sẽ phá vỡ ~180 tham chiếu chéo và cả vốn từ đang dùng, đổi lại không được gì.

**`00-FACTORY.md` → `SYSTEM-PROMPT.md`**, viết lại thành **15 mục** có đánh số §, bọc trong khối ▼▲ để dán thẳng vào Instructions. Bản gốc giữ tại `doc/v1-ban-goc-brain.md`.

| Mục bản v1.0 | Đi về đâu |
|---|---|
| ROLE · MISSION | §1 |
| KNOWLEDGE + bản đồ nạp module | §2 |
| WORKFLOW 5 bước | §6 |
| OUTPUT | §12 |
| RULES 8 điều | §11 (thành 9 điều) |
| Ví dụ lệnh → hành động | `doc/02-cau-lenh.md` · `doc/03-output-mau.md` |
| README §1 cấu trúc · §2 bảng 4 agent · §4 bảo trì | `README.md` viết lại |
| README §5 danh sách cần xác minh | mục **Việc còn treo** dưới đây |

**Mục mới trong bộ não** — bản v1.0 không có, nay bổ sung:

| Mục | Vì sao thêm |
|---|---|
| **§3 Định danh thương hiệu** + ranh giới hệ sinh thái | Bản cũ không chặn việc sinh agent cho line **cơ xương khớp** — đó là thương hiệu riêng (Cơ Xương Khớp – Wellness), có agent riêng |
| **§4 Nguyên tắc tối thượng** | Nâng *"1 agent = 1 vai trò, càng hẹp càng giỏi"* và *"agent chỉ gợi ý"* từ ghi chú trong WORKFLOW thành nguyên tắc đứng đầu |
| **§5 Hai chế độ** | Bản cũ có 2 việc (tạo agent / hỏi vận hành) nhưng không khai báo thành mode, nên Agent dễ trả lời lẫn kiểu |
| **§7 Trạng thái L1–L6** đưa thẳng vào bộ não | Trước nằm hẳn trong K6 — nhưng đây là thứ Agent cần ở mọi câu trả lời, để trong bộ não thì không phải tra |
| **§8 Quy ước KB** · **§9 Luồng + handoff** · **§10 Điều kiện thoát** | Cùng lý do trên — tra K6 mỗi lần làm chậm và dễ sót |
| **§10 K7 là dữ liệu động** | Nâng thành mục riêng, có luật **cấm dùng số của tháng trước** và nêu đích danh 3 lỗi quá khứ (6tr≠3tr · 7≠10 cơ sở · sai ngày) |
| **§12 Định dạng đầu ra** 5 phần | Bản cũ chỉ nói "system prompt + phiếu 6 ô"; nay thêm **MODULE ĐÃ NẠP** (nói rõ lọc phần nào) và **BẢNG TEST 4 TIÊU CHÍ** thành phần xuất bắt buộc |
| **§13 Thiếu dữ liệu & người dùng không chuyên** | Nhân viên trực page không thuộc mã L — Agent phải giải thích mã chứ không chỉ ném mã ra |
| **§14 Rules 8 điều** cấp Factory | Phân biệt với §11 (9 guardrail cho agent **con**) — trước đây lẫn làm một |

**Guardrail tăng từ 8 → 9.** Thêm: *chỉ nêu bác sĩ **đã được duyệt quảng bá**, không trích số ca chưa xác minh* — tách ra thành điều riêng vì web đang tự gắn cờ vài hồ sơ bác sĩ "chưa duyệt / ảnh bằng cấp placeholder / năm KN & số ca mâu thuẫn".

**Tài liệu vận hành mới (`doc/`)**
- `01-cai-dat.md` — tên & mô tả · cài 3 nền tảng · **bảng file nào upload file nào không** · **10 smoke test** · bảo trì K7 hàng tháng · **11 ca xử lý sự cố**.
- `02-cau-lenh.md` — câu lệnh cho cả 2 mode · prompt tinh chỉnh · **16 yêu cầu Factory sẽ từ chối**.
- `03-output-mau.md` — output mẫu đủ 5 phần cho mode TẠO AGENT (phiếu 6 ô → module đã nạp → system prompt → bảng test → ghi chú xác minh), 2 ví dụ mode HỎI VẬN HÀNH · 4 dấu hiệu đúng / 4 dấu hiệu sai.
- `04-prompt-nguoi-moi.md` — 10 prompt cho nhân viên **chưa thuộc mã L-code**, mô tả tình huống bằng lời thường.

---

## v1.0 — 08/10/2026 · bản gốc

Hệ **1 meta-agent sinh 4 agent CSKH** dùng chung bộ Knowledge Module. Công thức HCI **R·M·K·W·O (+Rules)**, kiến trúc lõi brand-neutral + module thương hiệu.

- `00-FACTORY.md` — brain: sinh agent + trả lời luồng vận hành.
- `knowledge/K1–K7` — module thương hiệu Kangnam; K3 nối 6 giai đoạn hành vi với L1–L6; K5 bank kịch bản + 8 lỗi cấm + 8 quy tắc vàng + luồng 7 bước; K6 xương sống trạng thái/routing/KB/handoff; K7 hot-swap theo tháng.
- `templates/A1–A4` — template agent brand-neutral; A2 kèm Rubric QC v1, A3 kèm bộ tiêu chí ± v1.

---

## Việc còn treo — cần Kangnam xác minh trước khi chạy

| # | Hạng mục | Ảnh hưởng |
|---|---|---|
| 1 | **Giá & % ưu đãi, ngày chương trình, số suất** (K7) | **Chặn cứng** — đây là nguồn của 3 lỗi mâu thuẫn đã xảy ra: 6tr ≠ 3tr · 7 ≠ 10 cơ sở · sai ngày |
| 2 | **Hotline** 02873066499 / 466 / 02473088885 (K7) | Agent chưa biết số nào là số chính thức cho campaign nào |
| 3 | **Cách nói số cơ sở** thống nhất (3 BV + 7 viện vs "7 cơ sở") | Hai cách nói cùng tồn tại → khách bắt được mâu thuẫn |
| 4 | **Bảng giá** (K4 §5) — giá niêm yết tham khảo 09/2026 | ⚠ cần xác nhận giá cắt mí Plasma (8tr vs 7.2tr) và đồng bộ khi web đổi |
| 5 | **Danh sách bác sĩ được duyệt quảng bá** (KF-02 / "10 bác sĩ") + CCHN còn hiệu lực | Đã trích đủ 22 hồ sơ từ sitemap, nhưng web tự gắn cờ vài hồ sơ *chưa duyệt / chưa trong KF-02 / ảnh bằng cấp placeholder / năm KN & số ca mâu thuẫn* → agent chỉ được nêu người đã duyệt |
| 6 | **Phác đồ hậu phẫu** từng dịch vụ (K4/A4) | A4 chưa lên được nhịp nhắc chính xác theo dịch vụ |
| 7 | **Link before-after & video** quy trình/hành trình (K5 §6) | Cần verify còn sống trước khi agent gửi cho khách |
| 8 | **Nội dung chi tiết KB1–16** (sheet "Cài đặt KB") | Mới có tên slot; nhiều slot `Take care_KB` còn trống → agent phải báo ⚠ thay vì trả lời |
| 9 | **Quy tắc routing** cho L2.3/L2.4/L5/L6 (K6 §3) | File gốc để trống → agent đang dùng **đề xuất mặc định**, chưa phải quy tắc chính thức |
| 10 | **Rubric QC v1 & bộ tiêu chí Lead Scoring v1** (A2/A3) | Bản đề xuất — cần duyệt/điều chỉnh trọng số trước khi chấm thật và dùng để đánh giá nhân sự |
