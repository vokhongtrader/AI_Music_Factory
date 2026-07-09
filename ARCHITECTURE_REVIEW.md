# ARCHITECTURE REVIEW

Date: 2026-07-09
Project: AI_Music_Factory
Scope: Sprint 0 foundation review only (no Sprint 1 implementation)

## Điểm mạnh

- Kiến trúc theo module rõ ràng: `core`, `composer`, `lyrics`, `voice`, `judge`, `telegram`, `export` giúp tách trách nhiệm tốt.
- Có phân tách giữa runtime (`core`, module) và tri thức (`knowledge`) cùng không gian thử nghiệm (`research`).
- Bộ tài liệu quản trị dự án khá đầy đủ cho giai đoạn nền tảng: định hướng, kế hoạch, trạng thái, quyết định.
- Có sẵn script vận hành nền tảng trong `scripts/` để chuẩn bị cho quy trình làm việc dài hạn.
- Hướng kiến trúc pipeline đã được mô tả nhất quán trong tài liệu kiến trúc.

## Điểm yếu

- Tài liệu trạng thái hiện bị phân mảnh ở nhiều file có nội dung giao thoa.
- Chưa có định nghĩa contract dữ liệu chính thức giữa các module (schema/versioning/idempotency).
- `core/` đang được định nghĩa rất rộng, dễ thành nơi gom logic khi bắt đầu coding.
- Chưa có taxonomy chuẩn cho `knowledge/` và `research/`, dễ trùng vai trò khi dự án tăng trưởng.
- Chưa có cấu trúc con cho `tests/`, `config/`, `assets/`, gây mơ hồ khi mở rộng.

## Rủi ro

### 1) Thư mục có thể dư ở giai đoạn hiện tại

- Không có thư mục nào dư hoàn toàn theo mục tiêu dài hạn.
- `.ai/` có thể bị xem là chưa cần thiết nếu không dùng ngay cho automation metadata, nhưng vẫn hợp lý để dành chỗ cho quy trình AI-assisted sau này.

### 2) Tài liệu có khả năng trùng hoặc chồng lấn

- `REPORT.md`, `SESSION.md`, `CHANGELOG.md`: đều ghi nhận những gì đã làm trong Sprint 0, mức độ trùng thông tin cao.
- `NEXT_TASK.md` và trường `next` trong `PROJECT_STATUS.json`: cùng thể hiện bước tiếp theo.
- `MASTER_PLAN.md` và `ROADMAP.md`: không trùng hoàn toàn nhưng đang giao thoa nội dung tiến độ.

### 3) Module nên tách

- `core/` nên tách sớm thành các nhóm con để tránh monolith orchestration:
  - orchestration
  - contracts
  - shared utilities
  - run state/context
- `judge/` về lâu dài nên tách rõ:
  - quality evaluation
  - policy/compliance checks

### 4) Module nên gộp

- Không nên gộp các module nghiệp vụ chính (`composer`, `lyrics`, `voice`) ở hiện tại vì sẽ mất tính độc lập tiến hóa.
- Có thể cân nhắc gộp tạm logic quản trị tài liệu trạng thái thành một nguồn sự thật duy nhất (thay vì gộp module runtime).

### 5) Thư mục có nguy cơ khó mở rộng

- `config/`: nếu để phẳng sẽ khó quản lý môi trường, module config và secrets mapping.
- `tests/`: nếu để phẳng sẽ khó scale khi có unit/integration/e2e/contract tests.
- `knowledge/` và `research/`: không có chuẩn phân loại sẽ khó truy hồi tri thức và tái sử dụng.
- `assets/`: thiếu phân vùng theo loại tài nguyên và vòng đời (raw/processed/published).

## Đề xuất

### A. Chuẩn hóa nguồn sự thật cho trạng thái dự án

- Chọn `PROJECT_STATUS.json` làm source of truth máy đọc.
- Giữ `CHANGELOG.md` cho lịch sử thay đổi.
- Dùng `SESSION.md` cho nhật ký theo phiên làm việc.
- Giảm nội dung trùng trong `REPORT.md` thành dạng tổng kết định kỳ (không lặp changelog/session).

### B. Thiết kế khung mở rộng thư mục trước Sprint 1

- Định nghĩa cấu trúc con cho:
  - `core/` (orchestration/contracts/shared)
  - `tests/` (unit/integration/e2e/contracts)
  - `config/` (base/env/modules)
  - `knowledge/` (prompts/rules/templates/versioned)
  - `research/` (experiments/findings/decisions)

### C. Áp dụng contract-first trước khi viết logic

- Chuẩn hóa schema trao đổi giữa module (input/output/error/retry metadata).
- Quy định versioning cho contract để tránh breaking changes chéo module.

### D. Giữ module business tách biệt, tránh gộp sớm

- Duy trì tách riêng `composer`, `lyrics`, `voice`, `judge`, `export`, `telegram`.
- Chỉ chia sẻ qua contract và orchestration, không chia sẻ trực tiếp logic nội bộ.

## Ưu tiên

### P0 (Làm ngay trước Sprint 1)

1. Chốt mô hình source of truth tài liệu trạng thái để giảm trùng.
2. Chốt contract dữ liệu liên module (format, versioning, validation).
3. Chốt cấu trúc con cho `core`, `config`, `tests`.

### P1 (Đầu Sprint 1)

1. Chốt taxonomy cho `knowledge` và `research`.
2. Chốt ranh giới `judge` giữa quality và policy.
3. Chốt convention naming cho artifacts và run context.

### P2 (Sau khi có skeleton chạy được)

1. Rà soát lại việc có cần duy trì `.ai/` theo quy trình thực tế.
2. Tối ưu hóa lại bộ tài liệu để giảm chi phí bảo trì dài hạn.

## Kết luận

- Kiến trúc nền tảng hiện tại tốt cho khởi động dài hạn.
- Không có thư mục nào dư hoàn toàn, nhưng có một số điểm giao thoa tài liệu và rủi ro mở rộng nếu không chuẩn hóa trước Sprint 1.
- Khuyến nghị chính: không gộp module nghiệp vụ, ưu tiên tách rõ vai trò trong `core` và chuẩn hóa contract + tài liệu trạng thái.
