# PROJECT MANAGER

## Mục tiêu

Xây dựng AI Project Manager để trong tương lai chỉ cần một hành động `Start`, toàn bộ quy trình vận hành được tự động hóa theo workflow chuẩn.

Sprint P001 chỉ xây dựng kiến trúc, chưa lập trình chi tiết runtime.

## Phạm vi Sprint P001

- Tạo module khung tại `AI_Core/project_manager/`
- Tạo script vận hành tại `scripts/`
- Định nghĩa luồng tự động end-to-end ở mức tài liệu và workflow model

## Kiến trúc module

- `manager.py`: điểm vào orchestration cấp cao
- `task_loader.py`: đọc trạng thái dự án và nhiệm vụ kế tiếp
- `workflow.py`: định nghĩa thứ tự các bước tự động
- `reporter.py`: cập nhật báo cáo tiến độ chạy
- `shutdown.py`: chính sách tắt máy cuối ca
- `telegram.py`: adapter gửi thông báo Telegram
- `scheduler.py`: định nghĩa lịch chạy hằng ngày

## Quy trình tự động mong muốn

1. Đọc `PROJECT_STATUS.json`
2. Đọc `NEXT_TASK.md`
3. Kiểm tra Environment
4. Kiểm tra Git
5. Kiểm tra Backup
6. Bắt đầu Task
7. Cập nhật REPORT
8. Commit Git
9. Backup
10. Gửi Telegram
11. Nếu hết thời gian làm việc thì tự tắt máy

## Quy ước triển khai tương lai

- Contract-first cho dữ liệu bước workflow
- Mỗi bước có trạng thái: `pending`, `running`, `success`, `failed`, `skipped`
- Mọi cập nhật phải ghi log có timestamp và run_id
- Không gắn chặt logic module business vào manager

## Script vận hành

- `scripts/start_factory.ps1`: điểm vào một nút Start
- `scripts/stop_factory.ps1`: dừng tác vụ an toàn
- `scripts/daily_run.ps1`: chạy theo lịch hằng ngày

## Trạng thái hiện tại

- Hoàn tất kiến trúc P001
- Chưa có xử lý thực thi thực tế
- Chưa tích hợp API Telegram thật
- Chưa tích hợp scheduler backend thật
