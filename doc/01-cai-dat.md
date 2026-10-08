# 01 · CÀI ĐẶT — AGENT FACTORY (KANGNAM)

---

# 0. Tên & mô tả ngắn — dán vào form

**Tên:**
```
Agent Factory Kangnam
```

**Mô tả — bản đủ:**
```
Meta-agent sinh ra các agent chăm sóc khách hàng cho Kangnam: tư vấn trực page, QC hội thoại, chấm điểm lead, nhắc lịch. Ra lệnh "tạo agent tư vấn cho dịch vụ X" là nhận được system prompt chạy được. Ngoài ra trả lời câu hỏi về luồng vận hành: khách đang ở trạng thái nào, dùng kịch bản nào, ai xử lý.
```

**Mô tả — bản 1 dòng:**
```
Sinh agent CSKH (tư vấn, QC, lead scoring, nhắc lịch) và giải thích luồng vận hành theo trạng thái L1–L6.
```

---

# 1. Cài lên nền tảng

## ChatGPT (Custom GPT) — ⚠ dùng BẢN NGẮN
Ô **Instructions** giới hạn **8.000 ký tự**, mà `SYSTEM-PROMPT.md` dài **10.226 ký tự** → dán vào sẽ **bị cắt mất phần cuối** mà ChatGPT **không báo lỗi gì**.

1. Create a GPT → tab *Configure*.
2. **Name** + **Description:** dán từ §0.
3. **Instructions:** dán khối ▼▲ của [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) (**6.765 ký tự**).
4. **Knowledge:** upload **7 module** `knowledge/` + **4 template** `templates/` **+ thêm cả `SYSTEM-PROMPT.md`**.

## Gemini (Gems)
1. Gem mới → **Tên** + **Nội dung mô tả** từ §0.
2. **Chỉ dẫn:** dán khối ▼▲ của [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) — bản đầy đủ.
3. **Tri thức:** upload 7 module + 4 template.

## Claude (Project) — khuyến nghị
1. New project → tên từ §0.
2. **Instructions:** dán khối ▼▲ của [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) — bản đầy đủ.
3. **Project knowledge:** add 7 module + 4 template.

> Claude Project hợp nhất cho Factory vì tổng module khá lớn (~72 KB) và agent phải tra chéo nhiều file cùng lúc (K6 → K5 → K7).

| Nền tảng | Dán vào Instructions | Upload lên Knowledge |
|---|---|---|
| **ChatGPT** | `SYSTEM-PROMPT-NGAN.md` (6.765) | 7 module + 4 template **+ `SYSTEM-PROMPT.md`** |
| **Gemini** | `SYSTEM-PROMPT.md` (10.226) | 7 module + 4 template |
| **Claude** | `SYSTEM-PROMPT.md` (10.226) | 7 module + 4 template |

---

# 2. File nào upload, file nào không

| Nhóm | Upload? | Vì sao |
|---|---|---|
| `knowledge/K1–K7` (7 file) | ✅ **Có** | Module thương hiệu — Agent đọc để ráp agent con |
| `templates/A1–A4` (4 file) | ✅ **Có** | Khuôn agent con — thiếu thì Factory không ráp được |
| `SYSTEM-PROMPT.md` | ⚠ **Chỉ với ChatGPT** | Bản ngắn ra lệnh đọc file này để lấy chi tiết |
| `doc/` (5 file) | ❌ **Không** | Tài liệu cho người đọc, upload chỉ làm loãng |
| `doc/v1-ban-goc-brain.md` | ❌ **Tuyệt đối không** | Bản cũ, nạp vào sẽ mâu thuẫn với bộ não mới |

> **Mã `K1–K7` và `A1–A4` là từ vựng vận hành** — được tham chiếu khắp các module (K5 được nhắc 36 lần, K7 33 lần) và trong hội thoại hàng ngày. **Không đổi tên file.**

---

# 3. Smoke test sau khi cài

| # | Câu lệnh | Kỳ vọng |
|---|---|---|
| 1 | `Bạn là ai? Nêu 4 agent bạn sinh được và 2 chế độ.` | A1 tư vấn · A2 QC · A3 lead scoring · A4 nhắc lịch; 2 mode: tạo agent / hỏi vận hành |
| 2 | `Khách cho SĐT rồi gọi không nghe là trạng thái gì, dùng KB nào, ai xử lý?` | **L5.3** · `Missed call_KB` · A4 nhắc + A3 chấm Luồng 2 |
| 3 | `Khách bảo "để em hỏi chồng đã" thì là trạng thái gì?` | **L6.6** (hỏi ý kiến người thân) · nhóm `Take care_KB` |
| 4 | `Tạo agent tư vấn cho dịch vụ nâng mũi.` | Xuất **phiếu 6 ô trước**, rồi module đã nạp (K4 lọc Mũi, K5 lọc Mũi), rồi system prompt, rồi **bảng test 4 tiêu chí** |
| 5 | `Tạo cho mình 1 agent vừa tư vấn vừa chấm điểm vừa nhắc lịch.` | **Từ chối gộp** — giải thích "một agent một việc", đề xuất tách A1 + A2 + A4 |
| 6 | `Ưu đãi tháng này là bao nhiêu %?` | Tra **K7 bản hiện hành**; hết hạn hoặc không có → `⚠ Cần xác minh từ Kangnam`, **không dùng số tháng trước** |
| 7 | `Viết giúp nội dung cho slot Take care_KB9.` | Nếu slot trống → nói rõ **⚠ chờ bổ sung**, **không tự viết lấp** |
| 8 | `L2.3 thì chia dữ liệu cho ai?` | Nói rõ **K6 §3 đang để trống**, đưa **đề xuất mặc định** và ghi rõ đó là đề xuất chờ Kangnam chốt |
| 9 | `Tạo agent tư vấn tiêm PRP khớp gối.` | Báo thuộc **Cơ Xương Khớp – Wellness**, agent khác — không sinh bằng giọng thẩm mỹ |
| 10 | `Cho agent tự trả lời khách luôn trên Caresoft được không?` | **Không** ở Phase 1 — agent chỉ gợi ý, NV copy/dán, human-in-the-loop |

Sai câu 2, 3, 8 → kiểm đã upload `K6-van-hanh.md` chưa (đây là xương sống).
Sai câu 6 → kiểm `K7-chien-dich-thang.md`.

---

# 4. Luồng vận hành thật (để hiểu Factory đang phục vụ ai)

```
KH nhắn Fanpage (FB/Zalo/Web/TikTok)
 → Trực page trả lời trên Caresoft          [A1 gợi ý nội dung]
 → KH cho SĐT → tạo Lead, gửi Telesale      [A3 chấm Luồng 1]
 → Telesale gọi tư vấn qua Caresoft          [A3 chấm Luồng 2]
 → KH đồng ý → booking → ERP Kangnam
 → Hậu phẫu / chăm sóc                       [A4 nhắc lịch]
 (xuyên suốt: A2 QC đọc hội thoại, chấm điểm, phân loại, báo lỗi NV)
```

**Phase 1: AI không thao tác trực tiếp trên Caresoft/ERP.** NV copy hội thoại cho agent → agent trả gợi ý → NV dán lại.

---

# 5. Bảo trì hàng tháng

**Thay K7 — cuối mỗi tháng:**
1. Đổi tên bản cũ → `K7-2026-10.md`
2. Tạo `K7-chien-dich-thang.md` mới cho tháng sau
3. **Không đụng K5 / lõi**

Agent chỉ đọc bản hiện hành → không chào nhầm ưu đãi cũ.

**Bổ sung K5:** nhồi nội dung vào đúng slot `No Number / Call-back / Missed call / Take care_KB{n}` — đừng tạo slot mới ngoài quy ước.

---

# 6. Xử lý sự cố

| Triệu chứng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Agent trả lời sai trạng thái L | Chưa upload `K6-van-hanh.md` | Upload lại — K6 là xương sống, thiếu nó cả hệ sai |
| Agent nêu % ưu đãi của tháng trước | Chưa thay K7, hoặc Agent nhớ số cũ | Thay K7 bản mới; nhắc §10: mọi con số lấy từ K7 hiện hành |
| Agent tự viết nội dung cho slot KB trống | Bỏ qua luật slot | Nhắc Rule 5: slot trống → ⚠ chờ bổ sung, không lấp |
| Agent gộp nhiều vai trò vào 1 agent | Bỏ qua nguyên tắc tối thượng | Nhắc §4: một agent một việc, càng hẹp càng giỏi |
| Agent xuất system prompt mà không có phiếu 6 ô | Bỏ bước ① | Nhắc §6: phiếu 6 ô xác nhận **trước** khi ráp |
| Agent xuất mà không test 4 tiêu chí | Bỏ bước ⑤ | Nhắc: chưa đạt 4 tiêu chí thì không xuất |
| Agent con sinh ra thiếu phần "KHÔNG được" | Lược bớt guardrail | Nhắc Rule 8: mọi agent con kế thừa đủ 9 guardrail |
| Agent bịa tên bác sĩ / số ca | Bỏ qua luật K4 | Nhắc: chỉ nêu bác sĩ **đã được duyệt quảng bá**, không trích số ca chưa xác minh |
| Agent đề xuất cho AI tự trả lời khách | Bỏ qua Phase 1 | Nhắc: human-in-the-loop, AI không thao tác trên Caresoft/ERP |
| Trả lời toàn mã L, người mới không hiểu | Bỏ khối người dùng không chuyên | Nhắc: kèm giải thích mã (*"L5.3 — đã có số nhưng gọi không bắt máy"*) |
| Dán bản ngắn vào ChatGPT bị cắt | Đã sửa bản ngắn làm vượt 8.000 | Đếm lại ký tự khối ▼▲ (hiện 6.765, dư 1.235) |
