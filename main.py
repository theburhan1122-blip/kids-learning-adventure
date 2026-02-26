"""
Smart Learning Adventure — Main Entry Point
A kid-friendly learning app built with Flet.
Runs as a server-side web app on Render / Railway / etc.
"""
import os
import flet as ft

# Controllers
from controllers.storage_controller import StorageController
from controllers.difficulty_manager import DifficultyManager
from controllers.reward_controller import RewardController
from controllers.navigation import NavigationController

# Views
from views.home_view import build_home_view
from views.english_view import build_english_view
from views.urdu_view import build_urdu_view
from views.maths_view import build_maths_view
from views.colors_view import build_colors_view
from views.shapes_view import build_shapes_view
from views.animals_view import build_animals_view
from views.quiz_view import build_quiz_view
from views.progress_view import build_progress_view


def main(page: ft.Page):
    # ── Page Configuration ───────────────────────────────────────
    page.title = "Smart Learning Adventure 🎓"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1a1a2e"
    page.padding = 0

    page.theme = ft.Theme(
        color_scheme_seed="#6200EA",
    )

    # ── Initialize Controllers ───────────────────────────────────
    storage = StorageController(page)
    difficulty_mgr = DifficultyManager(storage)
    reward_ctrl = RewardController(storage)
    nav = NavigationController(page)

    # Store controllers on page.data for access from views
    page.data = {
        "storage": storage,
        "difficulty_mgr": difficulty_mgr,
        "reward_ctrl": reward_ctrl,
        "nav": nav,
    }

    # ── Register Routes ──────────────────────────────────────────
    nav.register("home", build_home_view)
    nav.register("english", build_english_view)
    nav.register("urdu", build_urdu_view)
    nav.register("maths", build_maths_view)
    nav.register("colors", build_colors_view)
    nav.register("shapes", build_shapes_view)
    nav.register("animals", build_animals_view)
    nav.register("quiz", build_quiz_view)
    nav.register("progress", build_progress_view)

    # ── Start on Home ────────────────────────────────────────────
    nav.navigate_to("home")


# ── Entry point ──────────────────────────────────────────────────
# Reads PORT from environment (Render sets this automatically)
# Binds to 0.0.0.0 so Render can route traffic to it
port = int(os.environ.get("PORT", 8550))
ft.run(
    main,
    host="0.0.0.0",
    port=port,
    view=ft.AppView.WEB_BROWSER,
    assets_dir="assets",
)

