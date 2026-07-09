# AI Music Factory

AI Music Factory is a long-term modular platform for building and operating AI-powered music production workflows.

Sprint P008 delivers **Factory Runner** — single-command, fully automated workflow engine.

## Quick Start

```powershell
# Run full factory workflow (one command)
python AI_Core\project_manager\factory_runner.py

# Via PowerShell
.\scripts\start_factory.ps1

# Dry-run (no backup/git/push)
python AI_Core\project_manager\factory_runner.py --dry-run

# List registered modules
python AI_Core\project_manager\factory_runner.py --list-modules
```

## Factory Workflow (10 steps, automatic)

| Step              | Action                                  |
| ----------------- | --------------------------------------- |
| startup           | Validate project root                   |
| check_environment | Verify Python, Git, required files      |
| read_task         | Load NEXT_TASK.md + PROJECT_STATUS.json |
| execute_task      | Dispatch to module via keyword match    |
| run_tests         | Run test suite (unittest / pytest)      |
| update_report     | Write REPORT, SESSION, CHANGELOG        |
| backup            | Copy project to `D:\Projects\Backup\`   |
| git               | Commit + push to GitHub                 |
| telegram          | Notify (skipped if not configured)      |
| shutdown          | Optional OS shutdown (off by default)   |

## Permission Policy

`factory_config.json` controls which steps auto-run:

```json
"permissions": {
  "backup": true,
  "git_commit": true,
  "git_push": true,
  "run_tests": true,
  "telegram": true,
  "shutdown": false
}
```

## Registering a New Module

```python
from module_registry import FactoryModule, get_registry

class ComposerModule(FactoryModule):
    NAME = "composer"
    KEYWORDS = ["compose", "melody", "music"]

    def run(self, context):
        return "composed"

get_registry().register(ComposerModule())
```

## Sprint History

- Sprint 0: Foundation architecture
- Sprint P001: AI Project Manager architecture
- Sprint P002: Factory Manager control center architecture
- Sprint P003/P004: Runtime flow implemented and tested
- Sprint P005: Notification Service (Telegram-first)
- Sprint P006: Git repository initialized
- Sprint P007: GitHub repository connected
- Sprint P008: Factory Runner — single-command end-to-end automation

## Structure

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for full architecture.

## Working Rules

- Work directly in this repository
- No temporary workspace generation
- Foundation first, implementation later

## Last Factory Run

- run_id: `run-20260709-223927`
- status: success
- phase: Sprint P010
- duration: 38.4s
- updated_utc: 2026-07-09 22:40