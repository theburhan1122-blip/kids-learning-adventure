"""
Difficulty Manager — adaptive learning logic.
Classifies learners as slow / normal / fast and adjusts quiz difficulty per subject.
"""
import time
from typing import Optional


class DifficultyManager:
    """Tracks response accuracy and speed to adapt quiz difficulty."""

    # Rolling window size for classification
    WINDOW_SIZE = 10

    # Thresholds
    FAST_ACCURACY = 0.8     # ≥80% correct & fast → increase difficulty
    SLOW_ACCURACY = 0.4     # ≤40% correct or slow → decrease difficulty
    FAST_TIME = 5.0         # Under 5s per question = fast
    SLOW_TIME = 15.0        # Over 15s per question = slow

    def __init__(self, storage):
        """
        Args:
            storage: StorageController instance for persistence.
        """
        self.storage = storage
        self._profile = storage.load_difficulty_profile()
        # profile schema: {
        #   "english": {"history": [{"correct": true, "time": 3.2}, ...], "level": 1},
        #   ...
        # }

    def _ensure_subject(self, subject: str):
        """Initialize subject profile if missing."""
        if subject not in self._profile:
            self._profile[subject] = {"history": [], "level": 1}

    def record_answer(self, subject: str, correct: bool, time_taken: float):
        """Record a quiz answer and recalculate difficulty."""
        self._ensure_subject(subject)
        entry = self._profile[subject]

        # Append to rolling window
        entry["history"].append({"correct": correct, "time": time_taken})
        # Keep only last WINDOW_SIZE entries
        entry["history"] = entry["history"][-self.WINDOW_SIZE:]

        # Recalculate classification
        self._recalculate(subject)

        # Persist
        self.storage.save_difficulty_profile(self._profile)

    def _recalculate(self, subject: str):
        """Recalculate difficulty level based on rolling window."""
        entry = self._profile[subject]
        history = entry["history"]

        if len(history) < 3:
            return  # Not enough data yet

        total = len(history)
        correct_count = sum(1 for h in history if h["correct"])
        accuracy = correct_count / total
        avg_time = sum(h["time"] for h in history) / total

        current_level = entry["level"]

        # Classify and adjust
        if accuracy >= self.FAST_ACCURACY and avg_time <= self.FAST_TIME:
            # Fast learner → increase difficulty
            new_level = min(3, current_level + 1)
        elif accuracy <= self.SLOW_ACCURACY or avg_time >= self.SLOW_TIME:
            # Slow learner → decrease difficulty
            new_level = max(1, current_level - 1)
        else:
            # Normal learner → stay
            new_level = current_level

        entry["level"] = new_level

    def get_difficulty(self, subject: str) -> int:
        """
        Get the current difficulty level for a subject.
        Returns 1 (easy), 2 (medium), or 3 (hard).
        """
        self._ensure_subject(subject)
        return self._profile[subject]["level"]

    def get_learner_type(self, subject: str) -> str:
        """Get a human-readable learner classification."""
        self._ensure_subject(subject)
        history = self._profile[subject]["history"]

        if len(history) < 3:
            return "New Learner 🌱"

        total = len(history)
        correct_count = sum(1 for h in history if h["correct"])
        accuracy = correct_count / total
        avg_time = sum(h["time"] for h in history) / total

        if accuracy >= self.FAST_ACCURACY and avg_time <= self.FAST_TIME:
            return "Fast Learner 🚀"
        elif accuracy <= self.SLOW_ACCURACY or avg_time >= self.SLOW_TIME:
            return "Steady Learner 🐢"
        else:
            return "Good Learner ⭐"

    def get_difficulty_label(self, level: int) -> str:
        """Convert numeric level to label."""
        return {1: "Easy 🟢", 2: "Medium 🟡", 3: "Hard 🔴"}.get(level, "Easy 🟢")
