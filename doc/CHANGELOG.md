# CHANGELOG — AGENT FACTORY (KANGNAM)

## v2.3 — Kịch bản tư vấn đầy đủ + agent A5 tái khai thác

**Ngày:** 2026-10-10

### Nạp kịch bản tư vấn inbox đầy đủ vào `K8 §2`
Trước đây chỉ có khung B1–B5 với câu mẫu cắt cụt. Nay là câu mẫu nguyên văn cả 5 bước từ Playbook Trực Page Tháng 10, kèm:
- B1 yêu cầu **trả lời trong 2 phút** (khớp tiêu chí ① bảng chấm §6)
- B2 hai câu hỏi cụ thể để thu đủ 3 thông tin bắt buộc
- B3 luận điểm *môi trường bệnh viện được Bộ Y tế cấp phép*
- B4 cấm xin số bằng lý do *"để gửi ưu đãi"*
- B5 lối thoát *"bận thì em dời giờ"*
- Bảng 5 lý do từ chối: thêm xử lý **khách tỉnh**, làm rõ *đặt lịch thăm khám chưa phải thực hiện*

**Khái niệm mới:** phân biệt **page Bệnh viện** và **page Local** — cùng khung 5 bước và cùng giới hạn an toàn, khác giọng (page Local nhấn *"đẹp gần nhà"*). Ghi thêm vào `SYSTEM-PROMPT §3`: sinh A1 phải chốt loại page trước khi ráp.

### Thêm agent `A5 — Tái khai thác & Tạo nội dung`
Agent thứ năm, cho team trực page. Khác A4: **không quản lý lịch, không nhắc giờ** — chỉ trả lời *khách này còn chạm lại được không, bằng kênh nào, nói gì*.

Phạm vi: **tệp A** chưa cho số quá 6 ngày · **tệp B** đã cho số quá 6 ngày (đã hết chuỗi T+0→T+7).

Nội dung chính: bảng kênh theo trạng thái (cảnh báo **cửa sổ 24h Messenger**) · 5 lý do liên hệ hợp lệ · 4 nguyên tắc tái khai thác · điều kiện dừng kiểm trước khi soạn.

**4 slot chờ Kangnam chốt** ghi cuối file A5 — quan trọng nhất là kênh chạm tệp A khi cửa sổ 24h đã đóng.

### File đổi
`knowledge/K8-nang-luc-kich-ban-ban-giao.md` · `templates/A5-tai-khai-thac.md` *(mới)* · `SYSTEM-PROMPT.md` · `SYSTEM-PROMPT-NGAN.md` · `README.md` · `doc/01-cai-dat.md`

---

## v2.2 — 08/10/2026 · Nạp K8 (playbook vận hành thật)

**Thêm `knowledge/K8-nang-luc-kich-ban-ban-giao.md`** — nguồn: *Playbook Trực Page Kangnam Tháng 10*. Đây là **bản vận hành thật đang chạy**, khác với các module trước phần lớn là khung và đề xuất.

**Nội dung K8:** năng lực 17 nhân sự theo 3 khâu phễu · kịch bản 5 bước **B1–B5** + 5 lý do từ chối · phân loại **HOT/WARM/COLD** theo 5 tín hiệu · **bảng SLA** gọi theo khung giờ · phân bậc Telesale + cặp cố định · phiếu bàn giao **12 trường** · chuỗi chăm sóc **T+0 → T+7** · **rubric 10 tiêu chí** chuẩn ≥8/10 · kế hoạch đào tạo M1–M5 · **KPI + rủi ro**.

### K8 THAY THẾ một số phần cũ — mâu thuẫn thì K8 thắng

| Nội dung | Bản cũ | Bản dùng |
|---|---|---|
| Phiếu bàn giao | K6 §6 — 8 trường | **K8 §4 — 12 trường** (thêm Zalo, điểm phân loại, link hội thoại, tên trực page) |
| Rubric chấm hội thoại | A2 — "v1 đề xuất" | **K8 §6 — 10 tiêu chí, chuẩn ≥8/10** |
| Tiêu chí chấm lead | A3 — "± v1 đề xuất" | **K8 §3 — 5 tín hiệu → HOT/WARM/COLD** |

Đây là thay đổi quan trọng: trước đây A2 và A3 dùng **bản đề xuất chưa duyệt**. Giờ dùng bản thật — nên agent QC và lead scoring sinh ra mới chấm đúng chuẩn đang áp dụng.

### Hai trục phân loại, không gộp
- **L-code** = *trạng thái vận hành* (L4.1 là **thời điểm** bàn giao)
- **HOT/WARM/COLD** = *mức ưu tiên* (quyết **SLA** và **bậc Telesale** nào nhận)

Một lead mang cả hai: `L4.1 · HOT` → bậc 1, gọi ≤5 phút. **Thiết kế trường dữ liệu phải để hai cột riêng** — gộp là sai từ schema.

### ⚠️ Dữ liệu nhân sự là nội bộ
K8 §1 chứa **đánh giá hiệu suất của 17 người có tên**. Thêm **guardrail 10** và **Rule 6d**: không bao giờ nhúng vào system prompt agent con, không bao giờ xuất hiện trong nội dung gửi khách. Chỉ dùng khi trả lời về **đào tạo** và **định tuyến**.

### Thêm 2 đề bài tích hợp (§11 → 12 đề bài)
- **⑪ Đồng hồ SLA** — tính từ mốc nào, ai bấm giờ, cảnh báo sắp quá hạn ở đâu. Không có thì KPI *"HOT được gọi đúng SLA ≥90%"* vô nghĩa.
- **⑫ Chống lạm phát HOT** — chấm rộng tay thì HOT tràn lan, SLA vỡ. Rủi ro này đã được nhận diện sẵn trong playbook.

### Trang hướng dẫn — thêm nhóm prompt **Công nghệ**
Năm câu mới (05–09) dành riêng cho bộ phận kỹ thuật, trả ra thứ viết thẳng thành schema và pseudo-code:
**Thiết kế schema dữ liệu** · **Logic định tuyến Telesale** (bậc + trần tải + nhánh tràn) · **Đồng hồ SLA: đo và cảnh báo** · **Sự kiện cần log để đo KPI** · **Vòng phản hồi Telesale → Trực page** (webhook/notification).

Tổng 15 câu lệnh: 01–04 tầng hệ thống · **05–09 công nghệ** · 10–15 sản xuất và vận hành.

### Kèm theo
- `SYSTEM-PROMPT.md` → **17.636 ký tự**. `SYSTEM-PROMPT-NGAN.md` → **7.976 ký tự, chỉ dư 24** — đã phải đẩy phần tra cứu được (bảng 16 mã L, chi tiết 12 đề bài, chi tiết lộ trình) về bộ não đầy đủ. **Sửa là phải đếm lại.**
- `README.md` và `doc/01-cai-dat.md` đồng bộ lại: 5 chế độ (không còn 2), K1–K8, số ký tự mới, smoke test đổi sang câu tầng hệ thống.

### 🔶 Cần xác nhận
- Số liệu hiệu suất 17 nhân sự là **bản tháng 10/2026** — cập nhật khi có kỳ đánh giá mới.
- Mốc **show-up** chưa có — cần đặt trước khi đưa vào KPI chính thức.
- **Xác nhận playbook là bản đã duyệt** trước khi dùng rubric để đánh giá nhân sự.

---

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
