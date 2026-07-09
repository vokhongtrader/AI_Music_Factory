"""P010 tests for AI Music Factory module skeletons."""

from __future__ import annotations

import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from composer import ComposerModule
from core import CoreModule
from export import ExportModule
from judge import JudgeModule
from lyrics import LyricsModule
from telegram import TelegramModule
from voice import VoiceModule


class TestP010ModuleSkeletons(unittest.TestCase):
    def test_all_modules_return_skeleton_payload(self) -> None:
        context = {"run_id": "p010-test"}
        modules = [
            CoreModule(),
            ComposerModule(),
            LyricsModule(),
            VoiceModule(),
            JudgeModule(),
            TelegramModule(),
            ExportModule(),
        ]

        for module in modules:
            result = module.run(context)
            self.assertEqual(result["status"], "skeleton")
            self.assertEqual(result["module"], module.name)
            self.assertEqual(result["context"], context)


if __name__ == "__main__":
    unittest.main(verbosity=2)
