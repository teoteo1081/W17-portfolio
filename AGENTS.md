# AGENTS SHARED CONSTITUTION & UI/UX RULES
> Tệp quy chuẩn kỹ thuật bắt buộc dành cho mọi AI Agent (AGY, Codex, Claude Code) hoạt động trên repository này.

## 1. QUY TẮC CHỐNG RỚT CHỮ (NO ORPHAN WORDS)
- Mọi tiêu đề (H1, H2) và đoạn mô tả (Hero Paragraph) BẮT BUỘC có thuộc tính `text-wrap: balance` (hoặc class Tailwind `text-balance`).
- Cụm từ 2 chữ cuối câu luôn được bảo vệ bằng non-breaking space (`&nbsp;`) hoặc bọc trong `<span class="inline-block"></span>`.
- Container bọc chữ Hero luôn đặt tối thiểu `max-w-4xl` đến `max-w-5xl`, không dùng container hẹp gây bẻ dòng gượng ép.

## 2. QUY TẮC ĐỒNG BỘ ĐA NGÔN NGỮ (I18N DRIFT PREVENTION)
- Khi cập nhật văn bản qua JavaScript, KHÔNG BAO GIỜ dùng chuỗi thô ghi đè làm mất thẻ ngắt dòng (`<br>`) của HTML gốc.
- Dropdown ngôn ngữ toàn hệ sinh thái BẮT BUỘC dùng chung 1 format chuẩn quốc tế duy nhất: Mã 2 chữ cái in hoa (`VI | EN | ES | ZH`), tuyệt đối không chèn tiền tố mã quốc gia (như VN, US).

## 3. TIÊU CHUẨN THƯƠNG MẠI & TƯƠNG TÁC (EXECUTIVE STANDARD)
- Nút bấm (CTA) có hover effect rõ ràng, không có liên kết rỗng `href="#"`.
- Layout responsive 100% không bị tràn viền ngang (`overflow-x: hidden`) trên mobile 375px - 390px.
- Trực quan hóa dữ liệu sạch sẽ, padding/margin đồng nhất theo hệ lưới 8px.

## 4. DESIGN SYSTEM CONSISTENCY
- Ưu tiên sử dụng design tokens và components hiện có.
- Không tự ý tạo màu sắc, font chữ, spacing hoặc button style mới nếu hệ thống đã có chuẩn.
- Duy trì typography hierarchy nhất quán (H1, H2, H3, body, caption).
- Sử dụng spacing scale 4px/8px phù hợp ngữ cảnh.

## 5. ACCESSIBILITY FIRST
- Đáp ứng WCAG 2.2 AA đối với các tiêu chí áp dụng.
- Đảm bảo keyboard navigation, visible focus, semantic HTML và accessible names.
- Không sử dụng màu sắc làm phương tiện duy nhất để truyền đạt thông tin.
- Kiểm tra độ tương phản, kích thước vùng tương tác và hỗ trợ reduced motion.

## 6. SAFE CONTENT RENDERING
- Không đưa chuỗi HTML không đáng tin cậy trực tiếp vào `innerHTML`.
- Phân biệt plain text, Markdown, HTML và structured JSON.
- Ưu tiên structured components thay vì phụ thuộc vào chuỗi chứa thẻ HTML.
- Không làm mất định dạng, cấu trúc hoặc dữ liệu khi chuyển ngôn ngữ.

## 7. COMPLETE INTERACTION STATES
- Components tương tác phải có các trạng thái phù hợp: default, hover, focus, active và disabled.
- Các tác vụ bất đồng bộ phải xử lý loading, success, error và empty state khi áp dụng.
- Không tạo nút hoặc liên kết không có hành động thực tế.
- Thông báo lỗi phải rõ ràng và hướng dẫn người dùng cách khắc phục khi có thể.

## 8. RESPONSIVE WITHOUT HIDING ERRORS
- Kiểm tra giao diện tại các viewport 320px, 375px, 390px, 768px, 1024px và 1440px.
- Không dùng `overflow-x: hidden` như giải pháp mặc định để che lỗi layout.
- Đảm bảo text wrapping, tables, images, dialogs và buttons hoạt động trên màn hình nhỏ.
- Hỗ trợ zoom 200% mà không làm mất nội dung hoặc chức năng thiết yếu.

## 9. INTERNATIONALIZATION QUALITY
- Dùng một cơ chế i18n nhất quán, với locale chuẩn trong dữ liệu (`vi`, `en`, `es`, `zh`).
- Không hardcode text hiển thị nếu ứng dụng đã có hệ thống bản dịch.
- Hỗ trợ chuỗi dịch dài/ngắn khác nhau.
- Đảm bảo font fallback cho dấu tiếng Việt, tiếng Tây Ban Nha và chữ Trung.
- Không dùng cách ghi đè DOM làm mất cấu trúc component hoặc event handlers.

## 10. UI REGRESSION PROTECTION
- Không thay đổi các component ngoài phạm vi yêu cầu nếu không cần thiết.
- Không xóa hoặc thay đổi tính năng hiện có khi chỉ được giao sửa giao diện.
- Kiểm tra những trang cùng sử dụng shared components.
- Báo cáo rõ: files changed, UI impact, tests performed, remaining risks.
- Không tuyên bố PASS nếu chưa thực sự kiểm tra trực quan.

## 11. IMPLEMENTATION PRIORITY
Khi các quy tắc xung đột, ưu tiên theo thứ tự:
1. Security và data integrity.
2. Functional correctness.
3. Accessibility.
4. Responsive usability.
5. Design system consistency.
6. Visual polish.
(Tuyệt đối không hy sinh chức năng hoặc khả năng sử dụng chỉ để đạt hiệu ứng thị giác).
