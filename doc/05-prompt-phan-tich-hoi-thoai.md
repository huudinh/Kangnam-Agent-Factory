# 05 — PROMPT: PHÂN TÍCH HỘI THOẠI → 2 FILE EXCEL

Prompt tái sử dụng. Cho AI đọc một file hội thoại đã xuất từ Caresoft, trả về **hai file Excel**:

| File | Nội dung |
|---|---|
| `output/Kangnam_<DV>_PhanLoai_KichBan.xlsx` | Quy trình 4 bước cho **từng hội thoại** + bank kịch bản theo giai đoạn S1–S3 |
| `output/Kangnam_KichBan_<DV>.xlsx` | Phân loại chi tiết từng hội thoại + bộ kịch bản theo nhóm đối tượng A/B/C |

**Cần AI chạy được code** (Claude Code, ChatGPT có Code Interpreter, hoặc Gemini có code execution) vì đầu ra là `.xlsx`. Nếu AI không chạy được code, nó chỉ trả bảng — bạn tự dán vào Excel.

**Trước khi chạy:** thay `{{FILE}}` và `{{DỊCH VỤ}}` ở đầu prompt.

---

## PROMPT — copy từ đây

````
# NHIỆM VỤ
Đọc file hội thoại `{{FILE}}` và sinh ra ĐÚNG 2 file Excel trong thư mục `output/`.
Dịch vụ đang phân tích: {{DỊCH VỤ}}.

Viết script Python dùng openpyxl để tạo file. Không trả bảng trong chat — ghi ra file thật.

# ĐẦU VÀO — cấu trúc file hội thoại
Mỗi hội thoại là một khối:

  ## <STT>. <Tên KH> — <DD/MM HH:MM>
  - Phụ trách: <tên NV> · Có SĐT: <Có|Không> · Số tin: <n>
  - **<DD/MM HH:MM> KH:** <nội dung khách>
  - **<DD/MM HH:MM> NV (<tên NV>):** <nội dung nhân viên>

Quy ước: `[Ảnh]` `[Tệp]` `[Thẻ: …]` là đính kèm hoặc tin tự động, KHÔNG phải chữ khách gõ.
Trường `Có SĐT` lấy nguyên từ dữ liệu, không tự suy luận lại.

# BƯỚC 1 — CHẤM MỘT LẦN, HAI FILE DÙNG CHUNG
Chấm từng hội thoại đúng một lần, lưu kết quả, rồi cả hai file đọc từ kết quả đó.
Hai file BẮT BUỘC khớp nhau tuyệt đối về: L-code · độ nóng · nhóm đối tượng · giai đoạn.
Nếu hai file cho ra con số khác nhau cho cùng một hội thoại là SAI.

## Chấm 5 tín hiệu (mỗi tín hiệu 1 điểm)
① Nêu dịch vụ cụ thể (cắt mí / mí dưới / sụp mí / mở góc…), không phải "làm đẹp" chung
② Mốc thời gian dự kiến ≤ 14 ngày, hoặc đã đặt lịch / đang đến viện
③ Hỏi lịch, bác sĩ, hoặc chi phí theo đúng tình trạng của mình
④ Gửi ảnh hoặc mô tả rõ tình trạng mắt
⑤ Để lại SĐT/Zalo thật và đồng ý nhận tư vấn (ưu tiên có nêu khung giờ)

→ HOT 4–5 điểm · WARM 2–3 điểm · COLD 0–1 điểm.
Đã đặt lịch hoặc đang đến viện → HOT bất kể điểm.
Ghi lại kết quả dạng bitmask 5 chữ số, ví dụ `[10110]` = có ①③④, thiếu ②⑤.

# BỘ MÃ BẮT BUỘC — không tự chế mã mới

## Giai đoạn hành trình (trực page tiếp xúc)
S1 · NHẬN BIẾT — hỏi chung, hỏi giá/địa chỉ ngay từ đầu (Cold)
S2 · TÌM HIỂU — gửi ảnh/mô tả, hỏi phương pháp, công nghệ, bác sĩ (Warm)
S3 · CÂN NHẮC & NỖI SỢ — lo đau/rủi ro, so sánh, hỏi người nhà, chần chừ giá/thời gian (Warm→Hot)
CS · Hậu phẫu / chăm sóc sau làm

## L-code (trạng thái vận hành, chuẩn K6)
L1.1 lần đầu nhắn chưa tư vấn · L2.1 đang tư vấn hợp tác · L2.3 chưa phản hồi lại
L2.4 hẹn nhắn lại sau · L2.5 không có / xa chi nhánh · L4.1 có SĐT + rõ dịch vụ
L5.3 gọi không bắt máy · L5.4 từ chối nghe điện thoại · L5.5 hẹn gọi lại · L5.6 chỉ nhắn Zalo
L6.1 chưa rõ rào cản · L6.2 so sánh nơi khác · L6.3 chưa tài chính
L6.4 chưa có thời gian · L6.5 lo lắng/sợ đau · L6.6 hỏi ý kiến người thân

## Nhóm đối tượng theo insight
NHÓM A — chưa để lại SĐT (mục tiêu: xin số)
  A1 hỏi giá ngay chưa rõ tình trạng · A2 trung niên trẻ hóa mắt
  A3 khách sửa mắt lỗi / làm lại · A4 sụp mí bẩm sinh, phân biệt da dư vs cơ
  A5 Việt kiều / ở xa / nước ngoài · A6 trẻ, sợ đau, muốn tư vấn kỹ
NHÓM B — đã để lại SĐT (mục tiêu: kết nối → booking)
  B1 vừa cho số · B2 chưa kết nối được · B3 chỉ nhắn Zalo
  B4 đã gọi còn rào cản · B5 đã đặt lịch / hậu phẫu
NHÓM C — sau làm (LTV)
  C1 hậu phẫu · C2 gắn bó & mở rộng
Loại — không phải khách hàng (B2B chào bán)

## Mã kịch bản
S1.1 hỏi giá ngay · S1.2 hỏi địa chỉ/cơ sở · S1.3 chào mở chưa rõ nhu cầu
S2.1 đã gửi ảnh → nhận định theo vùng + xin số · S2.2 hỏi phương pháp/công nghệ/gây mê/bao lâu lành
S2.3 khách trẻ (1 mí / mí lót / mở góc) · S2.4 trung niên trẻ hóa · S2.5 bệnh nền / tình trạng đặc biệt
S3.1 lo lắng sợ đau · S3.2 so sánh nơi khác · S3.3 chưa tài chính · S3.4 chưa sắp xếp thời gian
S3.5 hỏi/giấu người nhà · S3.6 khách sửa lại · S3.7 ở xa/nước ngoài · S3.8 muốn đặt lịch → chốt khám
X1 xin SĐT đúng cách · X2 gọi nhỡ · X3 chỉ Zalo · X4 nuôi dưỡng Cold/im lặng
CS hậu phẫu + cross-sell

Nhiều mã dùng kèm thì nối bằng ` · ` — ví dụ `S2.4 · X2`.

## Vấn đề mắt (phân loại tình trạng)
Cắt mí (chung) · Sụp mí · Mở góc · Bọng mỡ/mí dưới · Da chùng/lão hóa
Treo cung/cung mày · 1 mí/mí lót · Nhấn mí · Mí lệch/không đều · Làm lại/sửa

# FILE 1 — output/Kangnam_<DV>_PhanLoai_KichBan.xlsx
Góc nhìn: QUY TRÌNH. Mỗi hội thoại đi trọn 4 bước trên một dòng.
5 sheet, đúng thứ tự:

1. **Tổng quan** — tiêu đề, nguồn dữ liệu, ngày lập; sơ đồ 4 bước
   ① ĐỐI TƯỢNG → ② NHÓM → ③ KỊCH BẢN → ④ NỘI DUNG;
   bảng 5 tín hiệu; bảng HOT/WARM/COLD; bảng giai đoạn S1–S3;
   kết quả phân loại (đếm thật); 6 nguyên tắc bắt buộc khi dùng nội dung.
2. **Chú giải ký hiệu** — giải nghĩa mọi ký hiệu dùng trong file:
   ⚠ · giai đoạn S · nhóm chăm sóc · L-code · mã kịch bản ·
   `[ … ]` chỗ cần điền · `{ … }` biến lấy từ chương trình tháng ·
   `·` phân tách mã · `→` bước kế tiếp · nhịp T/D/N · quy ước màu · viết tắt.
3. **Khung 5 bước B1-B5** — khung tư vấn chuẩn: mỗi bước một dòng,
   cột: Bước | Làm gì | Câu mẫu | Lưu ý.
4. **Quy trình <N> HT** — một dòng mỗi hội thoại, cột đúng thứ tự:
   STT | Tên khách | Tình trạng / Nhu cầu | Giai đoạn | Nhóm KH (insight) |
   Nhóm chăm sóc | Kịch bản (mã) | Tên kịch bản | Nội dung gợi ý gửi ngay | Rào cản / ghi chú
   → Cột "Nội dung gợi ý gửi ngay" phải là TIN NHẮN gửi được ngay, đã cá nhân hoá
     theo tình trạng của chính khách đó, không phải mô tả việc cần làm.
5. **Nhịp chăm sóc** — cột: Nhóm | Khi nào dùng | Nhịp chạm | KB gợi ý | Điều kiện dừng.
   Tối thiểu các nhóm: HOT đã có số · HOT gọi nhỡ · WARM đang nuôi · COLD ·
   Ở xa/nước ngoài · Sửa lại. Chốt bằng dòng trần nhắn.

# FILE 2 — output/Kangnam_KichBan_<DV>.xlsx
Góc nhìn: PHÂN LOẠI + BANK KỊCH BẢN theo nhóm đối tượng.
5 sheet, đúng thứ tự:

1. **Tổng quan** — kết quả phân loại (tổng HT, có/không SĐT kèm %, HOT/WARM/COLD,
   booking/hậu phẫu); bảng nhóm đối tượng A/B/C kèm insight từng nhóm;
   **mục "Lỗi quan sát trong data — phải tránh"** (trích số hiệu hội thoại thật
   làm dẫn chứng, ví dụ cam kết tuyệt đối, báo giá cứng, dán mẫu robotic,
   chăm sóc sau xin số chậm); mục biến số từ chương trình tháng, mọi số gắn ⚠.
2. **Chú giải ký hiệu** — như file 1 nhưng theo cột của file này:
   cột SĐT · Vấn đề mắt · Ghi chú (bitmask) · Nhóm ĐT · L-code · Độ nóng ·
   nhịp chăm sóc · ⚠ · lưu ý cốt lõi hai trục.
3. **Phân loại <N> HT** — một dòng mỗi hội thoại, cột đúng thứ tự:
   STT | Tên KH | Ngày | Phụ trách | Số tin | SĐT | Vấn đề mắt | Nhóm ĐT |
   L-code | Độ nóng | Ghi chú (tín hiệu ①②③④⑤)
   → Cột Ghi chú: bitmask `[01011]` + dấu hiệu quan sát (gửi ảnh, hỏi giá,
     ở xa/VK, sợ đau, so sánh, bận).
4. **Kịch bản <DV>** — bank kịch bản theo nhóm đối tượng, cột:
   Nhóm | Mã | Giai đoạn hành trình | Insight khách hàng (nỗi lo thật) |
   Trạng thái / L-code | Khi nào dùng | Nội dung 1 | Nội dung 2 | Nội dung 3 | Lưu ý an toàn
   → Mỗi mã A1–A6, B1–B5, C1–C2 một dòng.
5. **Chăm sóc theo độ nóng** — cột:
   Độ nóng | Số lead | Nghĩa | Tín hiệu nhận biết | SLA kết nối | Nhịp chăm sóc |
   KB / Hành động | Mục tiêu (KPI).
   → Cột "Số lead" phải khớp con số đếm được ở bước 1.

# QUY TẮC VIẾT NỘI DUNG KỊCH BẢN
- Nội dung là TIN NHẮN gửi khách, viết sẵn để trực page dán — không phải hướng dẫn.
- Mỗi tin một giá trị mới, 2–4 dòng, một câu hỏi chính.
- Trả lời câu khách hỏi TRƯỚC, rồi mới hỏi câu mới.
- Không lờ câu hỏi giá: nêu lý do chưa báo được + cho một thông tin giá trị + mời khám.
- Đề nghị = chọn giữa 2 phương án, không hỏi có/không.
- Xin SĐT kèm lý do mới + 2 khung giờ cụ thể, tối đa 2 lần/hội thoại.
- Chưa rõ giới tính → xưng "mình".
- `[ … ]` = chỗ điền theo tình huống. `{ … }` = biến lấy từ chương trình tháng, luôn kèm ⚠.

# QUY TẮC AN TOÀN — kiểm trước khi ghi file
- ❌ Từ cấm: `cam kết 100%` · `tốt nhất` · `không đau` · `an toàn tuyệt đối`.
- ❌ Không bắn giá cứng. Nêu khung giá niêm yết thì được, chốt số cuối cùng thì không.
- ❌ Không bịa bác sĩ, ca bệnh, giải thưởng, tỷ lệ thành công.
- ❌ Chỉ nhắc tên bác sĩ đã được duyệt quảng bá.
- ⚠ Mọi con số ưu đãi / % / ngày / hotline / số cơ sở / địa chỉ phải gắn ⚠ và
  ghi rõ cần xác minh — không lấy số của tháng trước.
- Không đưa số điện thoại, link, hay thông tin định danh của khách vào file đầu ra.
- Tên khách giữ như trong file nguồn, không bổ sung thêm thông tin cá nhân nào khác.

# TRÌNH BÀY EXCEL
- Font Arial toàn bộ. Freeze dòng tiêu đề. Wrap text ở các cột nội dung dài.
- Tiêu đề bảng: nền đậm, chữ trắng, in đậm.
- Độ rộng cột đặt theo nội dung; cột nội dung tin nhắn tối thiểu 60.
- Màu quy ước: xanh nhạt bước ①/giai đoạn S1 · cam nhạt bước ② ·
  xanh lá nhạt bước ③ · vàng bước ④ và mọi ô có ⚠ ·
  đỏ nhạt HOT · cam WARM · xanh dương nhạt COLD.

# CÁCH LÀM — theo thứ tự
1. Đọc và tách toàn bộ hội thoại. Báo số lượng tách được, đối chiếu với tiêu đề file.
2. Chấm 5 tín hiệu cho từng hội thoại, lưu một bảng kết quả duy nhất.
3. In ra bảng đếm: tổng HT · có/không SĐT · HOT/WARM/COLD · phân bố giai đoạn.
   DỪNG LẠI cho tôi xác nhận con số trước khi viết kịch bản.
4. Sinh bank kịch bản cho các mã có xuất hiện trong dữ liệu.
5. Ghi 2 file Excel.
6. Tự kiểm và báo cáo: hai file có khớp nhau về L-code/độ nóng/nhóm của từng
   hội thoại không · tổng số lead ở sheet "Chăm sóc theo độ nóng" có bằng tổng
   đếm được không · còn sót từ cấm hoặc số chưa gắn ⚠ không.
````

## Đến đây

---

## Lưu ý khi dùng

**Bước 3 cố tình dừng lại.** Chấm 5 tín hiệu là chỗ dễ lệch nhất — xem con số phân bố trước khi AI viết hàng trăm dòng kịch bản sẽ rẻ hơn nhiều so với sửa sau.

**Hai file phải khớp nhau.** Bản sinh lần đầu từng bị lệch: một file ghi HOT 47 · WARM 50 · COLD 3, file kia ghi HOT 25 · WARM 57 · COLD 18 trên cùng 100 hội thoại. Prompt này ép chấm một lần rồi cả hai file đọc chung kết quả, và yêu cầu AI tự đối chiếu ở bước 6.

**Đổi dịch vụ khác** chỉ cần thay `{{DỊCH VỤ}}` và bảng "Vấn đề mắt" thành bảng tình trạng của dịch vụ đó. Phần còn lại dùng lại được.

**File nguồn chứa dữ liệu khách thật** — tên, ảnh, mô tả tình trạng. Chạy trên máy nội bộ, và kiểm tra file đầu ra trước khi chia sẻ ra ngoài.
