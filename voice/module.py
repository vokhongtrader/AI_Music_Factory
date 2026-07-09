"""Voice module skeleton."""

from __future__ import annotations


class VoiceModule:
    """Creates vocal output in future sprints."""

    name = "voice"

    def run(self, context: dict) -> dict:
        return {
            "module": self.name,
            "status": "skeleton",
            "message": "Voice module skeleton is ready.",
            "context": context,
        }
