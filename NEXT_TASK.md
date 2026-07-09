# NEXT TASK

## Sprint P009 — Factory Automation Architecture

### Mục tiêu
Hoàn thiện hệ thống tự động hóa Factory:
- Hiển thị tiếng Việt trong khi chạy
- Tạo LAST_RUN.md sau mỗi lần chạy
- scripts/start_factory.ps1 là entry point duy nhất từ Windows
- Không cần copy/paste hay chạy lệnh thủ công

### Quy tắc làm việc
1. Claude chỉ ghi NEXT_TASK.md để định nghĩa task
2. Windows chạy: `.\scripts\start_factory.ps1`
3. factory_runner.py tự động thực hiện toàn bộ workflow
4. Mỗi sprint kết thúc bằng LAST_RUN.md và git push

### Trạng thái
- Factory Runner: ✅ hoàn chỉnh
- Vietnamese mode: ✅ hoàn chỉnh
- LAST_RUN.md: ✅ hoàn chỉnh
- Permission Policy: ✅ hoàn chỉnh
- Auto test + backup + git + telegram: ✅ hoàn chỉnh

### Sprint tiếp theo (P010)
Xây dựng module skeletons cho 7 module AI Music Factory.
