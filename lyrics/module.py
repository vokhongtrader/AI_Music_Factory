"""Lyrics module skeleton."""

from __future__ import annotations


class LyricsModule:
    """Creates lyric content in future sprints."""

    name = "lyrics"

    def run(self, context: dict) -> dict:
        return {
            "module": self.name,
            "status": "skeleton",
            "message": "Lyrics module skeleton is ready.",
            "context": context,
        }
