# KANGNAM AGENT FACTORY
Hệ **1 meta-agent sinh 4 agent CSKH**, dùng chung bộ Knowledge Module. Xây theo công thức HCI **R·M·K·W·O (+Rules)**, kiến trúc **lõi brand-neutral + module thương hiệu** (đổi brand = đổi K, không sửa lõi).
Version 1.0 · 2026-10-08.

---

## 1. CẤU TRÚC
```
kangnam-agent-factory/
├── 00-FACTORY.md              ← Brain: sinh agent + trả lời luồng vận hành
├── knowledge/                 ← Module thương hiệu (Kangnam)
│   ├── K1-thuong-hieu.md
│   ├── K2-khach-hang.md
│   ├── K3-hanh-vi-trang-thai.md   ← xương sống: 6 giai đoạn ↔ L1–L6
│   ├── K4-dich-vu.md
│   ├── K5-kich-ban.md             ← bank kịch bản + 8 lỗi cấm + 8 quy tắc vàng + luồng 7 bước
│   ├── K6-van-hanh.md             ← trạng thái L1–L6, routing, quy ước KB, handoff
│   └── K7-chien-dich-thang.md     ← HOT-SWAP, thay mỗi tháng (bản hiện tại: T10/2026)
├── templates/                 ← Agent brand-neutral
│   ├── A1-tu-van-truc-page.md
│   ├── A2-qc.md               (kèm Rubric QC v1)
│   ├── A3-lead-scoring.md     (kèm bộ tiêu chí ± v1)
│   └── A4-nhac-lich.md
└── README.md
```

## 2. 4 AGENT (khớp 3 AI trong file + Nhắc lịch)
| Agent | = AI trong file | Việc |
|---|---|---|
| **A1 Tư vấn** | (nằm trong "Chuyển đổi Data") | Gợi ý nội dung trả lời khách cho trực page |
| **A2 QC** | AI QC | Chấm điểm, phân loại Hot/Warm, báo lỗi NV, action plan đào tạo |
| **A3 Lead Scoring** | AI Lead scoring | Chấm 2 luồng (hội thoại + cuộc gọi), xếp hạng A/B/C/D |
| **A4 Nhắc lịch** | (nằm trong "Chuyển đổi Data") | Sinh lịch nhắc/chăm sóc theo nhịp |

## 3. CÁCH DÙNG (nạp vào Claude Project)
1. Tạo 1 Project, upload cả thư mục này làm Project knowledge.
2. Dán nội dung `00-FACTORY.md` vào **Custom Instructions** của Project → đó là meta-agent.
3. Ra lệnh: *"Tạo agent tư vấn cho dịch vụ [X]"* → Factory ráp template + module → trả **system prompt agent con + phiếu 6 ô**.
4. Lấy system prompt đó tạo 1 Project con (hoặc nạp vào Caresoft) để chạy agent.

Hoặc hỏi trực tiếp Factory câu vận hành: *"Khách cho số rồi gọi không nghe là trạng thái gì, dùng KB nào?"* → L5.3 · `Missed call_KB`.

## 4. BẢO TRÌ HÀNG THÁNG
- **Thay K7:** cuối tháng → đổi tên bản cũ `K7-2026-10.md`, tạo `K7-chien-dich-thang.md` mới cho tháng sau. Agent chỉ đọc bản hiện hành → không chào nhầm ưu đãi cũ. **Không đụng K5/lõi.**
- **Bổ sung K5:** nhồi thêm nội dung vào đúng slot `No Number/Call-back/Missed call/Take care_KB{n}`.

## 5. ⚠ DANH SÁCH CẦN KANGNAM XÁC MINH TRƯỚC KHI CHẠY
1. **Giá & % ưu đãi, ngày chương trình, số suất** (K7) — chống mâu thuẫn (lỗi quá khứ: 6tr≠3tr, 7≠10 cơ sở, sai ngày).
2. **Hotline** 02873066499 / 466 / 02473088885 (K7).
3. **Cách nói số cơ sở** thống nhất (3 BV + 7 viện vs "7 cơ sở").
4. **Bảng giá:** giá niêm yết tham khảo 09/2026 (K4 §5) — ⚠ xác nhận giá cắt mí Plasma (8tr vs 7.2tr) & đồng bộ khi web đổi. **Bác sĩ:** đã trích đủ 22 hồ sơ từ sitemap (K4 §4). ⚠ còn: Kangnam chốt **danh sách được duyệt quảng bá** (KF-02/"10 bác sĩ") + CCHN còn hiệu lực — web tự gắn cờ vài hồ sơ "chưa duyệt / chưa trong KF-02 / ảnh bằng cấp placeholder / năm KN & số ca mâu thuẫn"; agent chỉ nêu người đã duyệt, không trích số ca chưa xác minh.
5. **Phác đồ hậu phẫu** từng dịch vụ (K4/A4).
6. **Link before-after & video** quy trình/hành trình (K5 §6) — verify còn sống.
7. **Nội dung chi tiết KB1–16** sheet "Cài đặt KB" (mới có tên slot).
8. **Quy tắc routing** cho L2.3/L2.4/L5/L6 (K6 §3 — file gốc để trống).
9. **Rubric QC v1 & tiêu chí Lead Scoring v1** (A2/A3) — bản đề xuất, cần duyệt/điều chỉnh trọng số.

## 6. NGUYÊN TẮC AN TOÀN (mọi agent)
Human-in-the-loop · không cam kết kết quả tuyệt đối · không chẩn đoán/kê đơn · không báo giá cứng chưa xác minh · kiểm chứng mọi con số · không bịa dữ liệu · không nạp CCCD/hồ sơ/ảnh khách lên công cụ công cộng · lưu ý nhóm KH có thể là vị thành niên.
"# Kangnam-Agent-Factory" 
