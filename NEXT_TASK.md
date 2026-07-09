# NEXT TASK

## Sprint P009 — Module Skeletons & Interface Contracts

Define executable skeletons and interface contracts for all AI Music Factory modules.
Each module must expose a `FactoryModule` subclass registered in the global `ModuleRegistry`.

### Modules to scaffold

- `AI_Music_Factory/core/` — orchestration runtime, `CoreModule`
- `AI_Music_Factory/composer/` — music composition, `ComposerModule`  
- `AI_Music_Factory/lyrics/` — lyric generation, `LyricsModule`
- `AI_Music_Factory/voice/` — vocal production, `VoiceModule`
- `AI_Music_Factory/judge/` — quality evaluation, `JudgeModule`
- `AI_Music_Factory/telegram/` — user interaction, `TelegramModule`
- `AI_Music_Factory/export/` — output packaging, `ExportModule`

### Requirements

- Each module has a `__init__.py` that imports and exports its `FactoryModule` subclass.
- Each module registers itself with `get_registry()` on import.
- No AI model calls in this sprint — stubs only.
- `factory_runner.py --list-modules` must show all seven modules after this sprint.
