# Hướng dẫn sử dụng Base · Trình ký (E-office, BPM, E-Sign)

Trang chính `index.html` có 3 tab (mở thẳng bằng `#eoffice`, `#bpm`, `#esign`):

| Tab | Nguồn | Nội dung |
|---|---|---|
| E-office | `eoffice/index.html` | Văn bản đi có trình ký (soạn → xem xét & phê duyệt → **Trình ký sang E-Sign** → ký → cấp số → ban hành) và công văn đến có bút phê, 8 bước × 4 vai trò, 19 tình huống, setup S1–S12 cho Quản trị |
| BPM | `bpm/index.html` | Phiếu đề nghị thanh toán có bước trình ký kiểu mới (Liên kết Yêu cầu ký + khối Kết quả ký), 6 bước × 4 vai trò, 10 tình huống, setup S1–S9 |
| E-Sign | `esign/index.html` | Ký điện tử độc lập: chữ ký cá nhân, tạo hồ sơ, đặt trường (kéo thả / mã đặt trường), gửi, ký, hoàn thành; 7 bước, 9 tình huống, setup S1–S10 |

Song ngữ VI/EN, ảnh chụp thật trên tenant demo (Customer Success HN), dữ liệu TEST.

## Sửa nội dung
1. Sửa `src/content_<app>.py` (chuỗi dạng cặp (vi, en)); ảnh gốc ở `src/raw/`, ghim số ở `src/annos_spec.py` (ghim tìm theo chữ nhờ OCR cache `src/ocr/`, chạy `python3 src/ocr.py` khi thêm ảnh mới).
2. `python3 src/annos.py` → `python3 src/build.py content_<app>` (ghi `<app>/index.html`).
3. `python3 build_tabs.py` gộp thành `index.html`. QA: `NODE_PATH=$(npm root -g) node src/qa.js`.

## Xem online
Bật GitHub Pages (Settings › Pages › Branch `main` / root) hoặc import repo vào Vercel; trang chính là `index.html`.
