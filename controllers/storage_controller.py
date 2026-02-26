"""
Storage Controller — in-memory session storage for Flet 0.81.0.
Uses a plain Python dict so all operations are synchronous.
Data persists for the duration of the browser session.
"""


class StorageController:
    """Manages all data in-memory (no async, no coroutines, works everywhere)."""

    def __init__(self, page):
        self.page = page
        self._data = {
            "progress": {},
            "badges": [],
            "difficulty": {},
            "total_stars": 0,
            "streak": 0,
        }

    # ── progress ─────────────────────────────────────────────────

    def load_progress(self) -> dict:
        return self._data["progress"]

    def save_progress(self, progress: dict):
        self._data["progress"] = progress

    def increment_progress(self, subject: str, amount: int = 1):
        progress = self.load_progress()
        progress[subject] = progress.get(subject, 0) + amount
        self.save_progress(progress)

    # ── stars ────────────────────────────────────────────────────

    def load_total_stars(self) -> int:
        return self._data["total_stars"]

    def save_total_stars(self, stars: int):
        self._data["total_stars"] = stars

    def add_stars(self, count: int = 1):
        self._data["total_stars"] += count

    # ── badges ───────────────────────────────────────────────────

    def load_badges(self) -> list:
        return self._data["badges"]

    def save_badges(self, badges: list):
        self._data["badges"] = badges

    def add_badge(self, badge: str):
        if badge not in self._data["badges"]:
            self._data["badges"].append(badge)
            return True
        return False

    # ── difficulty profile ───────────────────────────────────────

    def load_difficulty_profile(self) -> dict:
        return self._data["difficulty"]

    def save_difficulty_profile(self, profile: dict):
        self._data["difficulty"] = profile

    # ── streak ───────────────────────────────────────────────────

    def load_streak(self) -> int:
        return self._data["streak"]

    def save_streak(self, streak: int):
        self._data["streak"] = streak

    # ── reset ────────────────────────────────────────────────────

    def reset_all(self):
        self._data = {
            "progress": {},
            "badges": [],
            "difficulty": {},
            "total_stars": 0,
            "streak": 0,
        }
