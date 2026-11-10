# W17-Portfolio — Portfolio Showcase & Interactive Capability Deck (V3)

Hệ sinh thái **Portfolio Showcase & Hồ Sơ Năng Lực Tương Tác (Version 3)** của **Thao Nguyen (TJ)** — *Data-Driven Performance Marketer • GA4 Ecosystem Hub • AI Orchestration & Multilingual Growth Specialist*.

---

## 📁 Cấu Trúc Thư Mục Chuẩn (V3)

```text
W17-portfolio/
├── index.html                  # [Final] Portfolio Showcase V3 (Tích hợp GA4, BigQuery & Power BI Dashboard)
├── index_portfolio_clean.html  # [Final] Hồ Sơ Năng Lực / Interactive CV V3 (Bản sạch sẵn sàng deploy & in PDF)
├── editor_workspace/           # Không gian soạn thảo trực quan (Visual Editor)
│   ├── editor_portfolio.html   # Bản Editor của Portfolio Showcase (Có thanh công cụ sửa chữ & xuất bản Final)
│   └── editor_cv.html          # Bản Editor của Hồ Sơ Năng Lực (Có nút [⬆][⬇], kéo thả, đổi màu, đổi ảnh)
├── ga4_metrics_live.json       # Dữ liệu đo lường thực tế từ Google Analytics 4 & BigQuery (airy-web-503408-c6)
├── fetch_ga4_bigquery.py       # Script Python truy vấn dữ liệu GA4 từ Google BigQuery
├── dev_server.py               # Local Dev Server hỗ trợ xem trực tiếp & lưu file sạch tự động qua /api/save
└── server.py                   # Core HTTP handler cho Visual Editor
```

---

## 🚀 Điểm Nổi Bật (Key Features)

1. **`index.html` — Portfolio Showcase V3**:
   - **Mô phỏng Phễu & Hiệu suất (Interactive Funnel Simulation)**: Lọc KPI động theo khu vực/kênh bán hàng.
   - **GA4 & Power BI Telemetry Dashboard**:
     - Tích hợp **Chart.js** biểu đồ đường & miền (Line & Area Chart) xu hướng 28 ngày (`1.684 lượt xem`, `174 người dùng`, `10.465 sự kiện`, `12m 30s tương tác TB`).
     - Bộ lọc Slicer tương tác (`[Tất cả]`, `[🇺🇸 Hoa Kỳ]`, `[🇻🇳 Việt Nam]`, chuyển đổi `28 ngày` / `7 ngày`).
     - **Interactive Drill-down Modal (Popup)**: Xem chi tiết Top 10 Quốc gia và Top 10 Tiêu đề trang kèm thanh tiến độ Data Bar.
   - **Hệ Thống 4 Ứng Dụng Thực Chiến**: Liên kết trực tiếp tới Live Demo & GitHub của *WRP Tax Services*, *Operation 0 — 1,000 Chunks Engine*, *TJ WordLoop Multiplayer Game*, và *TJ Courses Hub*.

2. **`index_portfolio_clean.html` — Hồ Sơ Năng Lực / Interactive CV V3**:
   - Giao diện Executive Dark/Light Mode với 4 bảng màu chủ đạo (*Ocean, Emerald, Royal Gold, Midnight Indigo*).
   - Tối ưu hóa CSS in ấn (`@media print`) xuất PDF chuẩn màu 100%.
   - Liên kết điều hướng 2 chiều mượt mà giữa **Portfolio Showcase (`./index.html`)** và **Hồ Sơ Năng Lực (`./index_portfolio_clean.html`)**.

---

## 💻 Cách Chạy Thử Nhanh Trên Máy Khác

### Cách 1: Mở trực tiếp (Zero-Config)
- Chỉ cần **double-click** mở trực tiếp file `index.html` hoặc `index_portfolio_clean.html` trên bất kỳ trình duyệt nào (mọi thư viện Tailwind CSS, Lucide Icons, Chart.js và Google Fonts đều hoạt động độc lập qua CDN và đường dẫn tương đối).

### Cách 2: Chạy qua Local Dev Server (Hỗ trợ tự động lưu file sạch từ Visual Editor)
```bash
python dev_server.py
```
Sau đó mở trình duyệt tại địa chỉ:
- **Portfolio Showcase (Final)**: `http://localhost:8000/index.html`
- **Hồ Sơ Năng Lực (Final)**: `http://localhost:8000/index_portfolio_clean.html`
- **Visual Editor Workspace**: `http://localhost:8000/editor_workspace/editor_portfolio.html`
