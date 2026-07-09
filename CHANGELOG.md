# CHANGELOG

## 2026-07-10 - Sprint P010 (Telegram Notification Completion)

- Created `AI_Core/notification/config.py` — credential file (BOT_TOKEN / CHAT_ID), user edits manually.
- Rewrote `AI_Core/notification/telegram_service.py`:
  - Reads `config.py` via `importlib.util` (priority over telegram.json).
  - Prints "Telegram chưa cấu hình." and skips gracefully when token empty.
  - `is_configured()` replaces `is_enabled()`.
- Rewrote `AI_Core/notification/message_builder.py`:
  - New functions return `str` with Vietnamese UTF-8 content and emojis.
  - `build_start()`, `build_finish()`, `build_error()`, `build_status()`.
  - Backward compat shims (`build_progress`, `build_success`, `build_shutdown`) return `MessagePayload`.
- Rewrote `AI_Core/notification/notification_manager.py`:
  - New API: `send_start()`, `send_finish()`, `send_error()`, `send_status()`.
  - Backward compat: `notify_success()`, `notify_error()`, `notify_progress()`.
- Updated `AI_Core/project_manager/factory_runner.py`:
  - `send_start()` called at startup step.
  - `send_finish()` called in finally (success) and telegram step.
  - `send_error()` called in both except blocks.
- Rewrote `AI_Core/notification/test_notification.py` — 21 tests, all PASS with empty token.
- Created `AI_Core/notification/README.md` — setup guide (BotFather, CHAT_ID, test command).

## 2026-07-09 - Sprint P008 (Factory Runner)

- Created `factory_runner.py` at `D:\Projects\` — single entry point for full workflow.
- Created `AI_Core/project_manager/module_registry.py`:
  - `FactoryModule` abstract base class with `NAME`, `DESCRIPTION`, `KEYWORDS`, `run()`, `matches()`.
  - `ModuleRegistry` singleton — `register()` / `dispatch()` / `list_modules()`.
  - Built-in `NullModule` (fallback) and `StatusModule` (phase/status reporter).
  - `TaskContext` dataclass passed to every module run.
- Created `factory_config.json` at `D:\Projects\` — master config (project, root, dry_run, auto_shutdown).
- Wired `execute_task` step in `manager.py` to dispatch through `ModuleRegistry` instead of writing a static marker.
- Updated `scripts/start_factory.ps1` — now calls `factory_runner.py` instead of placeholder TODO.
- New modules self-register via `get_registry().register(MyModule())` — no edits to core runner needed.
- Usage: `python factory_runner.py` or `.\scripts\start_factory.ps1`.
- Usage: `python factory_runner.py --list-modules` to inspect registered modules.

## 2026-07-09 - Sprint P007 (GitHub Connection)

- Created public GitHub repository `vokhongtrader/AI_Music_Factory`.
- Connected local repository remote `origin` to GitHub.
- Pushed branch `main` to GitHub.
- Pushed tag `v0.1.0` to GitHub.

## 2026-07-09 - Sprint P006 (Git Repository Setup)

- Initialized `AI_Music_Factory` as a Git repository (when missing).
- Set `main` as default branch.
- Added repository `.gitignore` with standard Python/VSCode/Node/cache/runtime/logs/.env ignores.
- Performed initial commit with message `Initial Project Structure`.
- Created repository tag `v0.1.0`.
- Verified clean git status after setup.

## 2026-07-09 - Sprint P005 (Notification Service)

- Implemented Notification Service module in `AI_Core/notification/`:
  - `notification_manager.py`
  - `telegram_service.py`
  - `message_builder.py`
- Added notification configs:
  - `config/system.json`
  - `config/telegram.json`
- Implemented message builder support for:
  - START
  - PROGRESS
  - SUCCESS
  - ERROR
  - SHUTDOWN
- Implemented Telegram service behavior:
  - reads config
  - when token/chat is missing, does not fail and logs `Telegram Disabled.`
- Integrated Factory Manager to use NotificationManager API:
  - `notify_success()`
  - `notify_error()`
  - `notify_progress()`
- Added and executed `test_notification.py` with passing results.

## 2026-07-09 - Sprint P004 (Factory Manager Runtime Control)

- Completed `scheduler.py` for session lifecycle management:
  - startup
  - heartbeat tracking
  - session termination
- Completed `decision_manager.py` for runtime permission decisions:
  - run allowed or blocked
  - missing required files
  - missing environment dependencies
- Completed `resource_manager.py` environment checks:
  - RAM
  - CPU
  - Disk
  - Python
  - Node
  - Git
  - Claude
- Completed `factory_monitor.py` runtime tracking:
  - current task
  - progress
  - start time
  - elapsed time
  - status
- Runtime artifacts are now generated:
  - `runtime/status.json`
  - `logs/factory.log`
- `manager.py` now runs with `python manager.py` and prints:
  - Environment OK
  - Workflow Loaded
  - Task Loaded
  - Factory Ready
- Added and executed test suite `test_p004.py` with passing results.

## 2026-07-09 - Sprint P002 (Factory Manager Control Center Architecture)

- Expanded `AI_Core/project_manager/` with new architecture modules:
  - `resource_manager.py`
  - `backup_manager.py`
  - `git_manager.py`
  - `factory_monitor.py`
  - `decision_manager.py`
  - `knowledge_router.py`
- Added runtime directories under `AI_Core/project_manager/`:
  - `logs/`
  - `state/`
  - `cache/`
  - `runtime/`
- Added architecture document:
  - `AI_Core/project_manager/FACTORY_MANAGER.md`
- Updated workflow and manager skeleton to represent the P002 ten-step operating flow.
- Updated project-level status and reporting documents for Sprint P002.

## 2026-07-09 - Sprint P001 (AI Project Manager Architecture)

- Added `AI_Core/project_manager/` architecture skeleton:
  - `manager.py`
  - `task_loader.py`
  - `workflow.py`
  - `reporter.py`
  - `shutdown.py`
  - `telegram.py`
  - `scheduler.py`
- Added workspace-level operation scripts:
  - `scripts/start_factory.ps1`
  - `scripts/stop_factory.ps1`
  - `scripts/daily_run.ps1`
- Added `docs/PROJECT_MANAGER.md`
- Updated core project documents for Sprint P001 status

## 2026-07-09 - Sprint 0 Foundation

- Added repository architecture folders
- Added project governance and planning documents
- Added `docs/ARCHITECTURE.md`
- Added placeholder scripts in `scripts/`
- Added `PROJECT_STATUS.json`

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-160547` with status `running`
- Progress recorded: 44.4%
- Notes: Workflow reached report step

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-160547` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-160646` with status `running`
- Progress recorded: 44.4%
- Notes: Workflow reached report step

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-160646` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-161342` with status `running`
- Progress recorded: 44.4%
- Notes: Workflow reached report step

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-161342` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-161453` with status `running`
- Progress recorded: 44.4%
- Notes: Workflow reached report step

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-161453` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-163735` with status `running`
- Progress recorded: 44.4%
- Notes: Workflow reached report step

## 2026-07-09 - Sprint P003 Factory Runtime

- Executed factory run `run-20260709-163735` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P008 Factory Runtime

- Executed factory run `run-20260709-164147` with status `running`
- Progress recorded: 44.4%
- Notes: Workflow reached report step

## 2026-07-09 - Sprint P008 Factory Runtime

- Executed factory run `run-20260709-164147` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P008 Factory Runtime

- Executed factory run `run-20260709-165408` with status `running`
- Progress recorded: 50.0%
- Notes: Workflow in progress

## 2026-07-09 - Sprint P008 Factory Runtime

- Executed factory run `run-20260709-165408` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P008 Factory Runtime

- Executed factory run `run-20260709-170356` with status `failed`
- Progress recorded: 10.0%
- Notes: 'charmap' codec can't encode character '\u2705' in position 2: character maps to <undefined>

## 2026-07-09 - Sprint P008 Factory Runtime

- Executed factory run `run-20260709-170422` with status `running`
- Progress recorded: 50.0%
- Notes: Workflow in progress

## 2026-07-09 - Sprint P008 Factory Runtime

- Executed factory run `run-20260709-170422` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P009 Factory Runtime

- Executed factory run `run-20260709-170453` with status `running`
- Progress recorded: 50.0%
- Notes: Workflow in progress

## 2026-07-09 - Sprint P009 Factory Runtime

- Executed factory run `run-20260709-170453` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-180518` with status `running`
- Progress recorded: 50.0%
- Notes: Workflow in progress

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-180518` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-223750` with status `running`
- Progress recorded: 50.0%
- Notes: Workflow in progress

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-223750` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-223927` with status `running`
- Progress recorded: 50.0%
- Notes: Workflow in progress

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-223927` with status `success`
- Progress recorded: 100.0%
- Notes: completed

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-224704-c01` with status `success`
- Progress recorded: 100.0%
- Notes: cycle 1 completed

## 2026-07-09 - Sprint P010 Factory Runtime

- Executed factory run `run-20260709-224704` with status `success`
- Progress recorded: 100.0%
- Notes: completed
