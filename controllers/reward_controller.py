"""
Reward Controller — manages stars, streaks, and badge awards.
"""


# Badge definitions
BADGES = {
    "first_steps":    {"name": "First Steps",     "icon": "🌟", "desc": "Complete your first quiz!"},
    "quick_thinker":  {"name": "Quick Thinker",   "icon": "🧠", "desc": "Answer 5 questions in under 3 seconds each!"},
    "streak_5":       {"name": "On Fire",          "icon": "🔥", "desc": "Get 5 correct answers in a row!"},
    "streak_10":      {"name": "Unstoppable",      "icon": "💥", "desc": "Get 10 correct answers in a row!"},
    "star_25":        {"name": "Star Collector",    "icon": "⭐", "desc": "Earn 25 stars!"},
    "star_50":        {"name": "Star Master",       "icon": "🌠", "desc": "Earn 50 stars!"},
    "star_100":       {"name": "Superstar",         "icon": "💫", "desc": "Earn 100 stars!"},
    "english_master": {"name": "English Master",    "icon": "📖", "desc": "Score 15+ in English!"},
    "urdu_master":    {"name": "Urdu Master",       "icon": "📝", "desc": "Score 15+ in Urdu!"},
    "maths_master":   {"name": "Maths Master",      "icon": "🔢", "desc": "Score 15+ in Maths!"},
    "colors_master":  {"name": "Colors Master",     "icon": "🎨", "desc": "Score 15+ in Colors!"},
    "shapes_master":  {"name": "Shapes Master",     "icon": "📐", "desc": "Score 15+ in Shapes!"},
    "animals_master": {"name": "Animals Master",    "icon": "🐾", "desc": "Score 15+ in Animals!"},
    "champion":       {"name": "Champion",           "icon": "🏆", "desc": "Earn all subject master badges!"},
}


class RewardController:
    """Handles star awarding and badge milestone checks."""

    def __init__(self, storage):
        self.storage = storage

    def award_correct_answer(self, time_taken: float) -> dict:
        """
        Award stars for a correct answer. Returns info about any new badges.

        Returns:
            dict with keys:
                stars_earned (int): 1 or 2 stars
                new_badges (list[str]): list of newly unlocked badge keys
        """
        # Bonus star for fast answers (< 3 seconds)
        stars = 2 if time_taken < 3.0 else 1
        self.storage.add_stars(stars)

        # Update streak
        streak = self.storage.load_streak() + 1
        self.storage.save_streak(streak)

        # Check badges
        new_badges = self._check_badges(streak, time_taken)

        return {"stars_earned": stars, "new_badges": new_badges}

    def record_wrong_answer(self):
        """Reset streak on wrong answer."""
        self.storage.save_streak(0)

    def _check_badges(self, streak: int, time_taken: float) -> list:
        """Check and award any new badges based on current stats."""
        new_badges = []
        total_stars = self.storage.load_total_stars()
        progress = self.storage.load_progress()

        # First quiz completion
        if self.storage.add_badge("first_steps"):
            new_badges.append("first_steps")

        # Quick thinker (single fast answer contributes; badge = 5 fast in window)
        if time_taken < 3.0 and self.storage.add_badge("quick_thinker"):
            new_badges.append("quick_thinker")

        # Streak badges
        if streak >= 5 and self.storage.add_badge("streak_5"):
            new_badges.append("streak_5")
        if streak >= 10 and self.storage.add_badge("streak_10"):
            new_badges.append("streak_10")

        # Star milestones
        if total_stars >= 25 and self.storage.add_badge("star_25"):
            new_badges.append("star_25")
        if total_stars >= 50 and self.storage.add_badge("star_50"):
            new_badges.append("star_50")
        if total_stars >= 100 and self.storage.add_badge("star_100"):
            new_badges.append("star_100")

        # Subject mastery (15+ score)
        master_badges = {
            "english": "english_master",
            "urdu": "urdu_master",
            "maths": "maths_master",
            "colors": "colors_master",
            "shapes": "shapes_master",
            "animals": "animals_master",
        }
        earned_masters = []
        for subj, badge_key in master_badges.items():
            if progress.get(subj, 0) >= 15:
                if self.storage.add_badge(badge_key):
                    new_badges.append(badge_key)
                earned_masters.append(badge_key)

        # Champion — all 6 subject masters earned
        if len(earned_masters) == 6 and self.storage.add_badge("champion"):
            new_badges.append("champion")

        return new_badges

    def get_badge_info(self, badge_key: str) -> dict:
        """Return display info for a badge."""
        return BADGES.get(badge_key, {"name": badge_key, "icon": "❓", "desc": ""})

    def get_all_badge_info(self) -> dict:
        """Return the full badge catalog."""
        return BADGES
