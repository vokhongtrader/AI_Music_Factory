"""Telegram module skeleton."""

from __future__ import annotations


class TelegramModule:
    """Handles chat delivery in future sprints."""

    name = "telegram"

    def run(self, context: dict) -> dict:
        return {
            "module": self.name,
            "status": "skeleton",
            "message": "Telegram module skeleton is ready.",
            "context": context,
        }
