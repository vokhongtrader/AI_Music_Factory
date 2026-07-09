# AI Music Factory

AI Music Factory is a long-term modular platform for building and operating AI-powered music production workflows.

Sprint P001 introduced the architecture baseline for an external AI Project Manager.
Sprint P002 extends that architecture into a centralized Factory Manager control center.
Sprint P003 and P004 move Factory Manager from architecture to executable runtime operations.
Sprint P005 adds Notification Service implementation for factory reporting.
Sprint P006 formalizes AI_Music_Factory as an official Git repository.

This repository currently contains **Sprint 0 (Foundation)** only.

## Sprint 0 Scope

- Establish project architecture and folder boundaries
- Create baseline governance and planning documents
- Create project automation script placeholders
- Define module roles and future integration paths

## Out of Scope (Current)

- Music generation logic
- Model training or inference pipelines
- Audio processing implementation
- Telegram bot runtime implementation

## Current Structure

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for full architecture details.
See [docs/PROJECT_MANAGER.md](docs/PROJECT_MANAGER.md) for the automation workflow architecture in Sprint P001.
See [../AI_Core/project_manager/FACTORY_MANAGER.md](../AI_Core/project_manager/FACTORY_MANAGER.md) for Sprint P002 Factory Manager control-center architecture.

## Working Rules

- Work directly in this repository
- No temporary workspace generation
- No zip packaging
- Foundation first, implementation later

## Sprint Status

- Sprint 0: complete
- Sprint P001: architecture setup for AI Project Manager complete
- Sprint P002: Factory Manager architecture expanded as operation center
- Sprint P003: core runtime flow implemented and tested
- Sprint P004: scheduler/decision/resource/monitor completed for real factory control
- Sprint P005: Notification Service implemented with Telegram-first extensible channel design
- Sprint P006: Git repository initialized, baseline commit/tag process established
- Current focus: Factory Manager architecture only (no AI Music Factory feature development)
