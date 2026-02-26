"""
Progress View — shows per-subject progress bars, badge gallery, and reset option.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft
from controllers.reward_controller import BADGES

def build_progress_view(page: ft.Page, **kwargs):
    """Build the progress and badge gallery view."""
    nav = page.data["nav"]
    storage = page.data["storage"]

    progress = storage.load_progress()
    earned_badges = storage.load_badges()
    total_stars = storage.load_total_stars()

    subjects_info = [
        {"key": "english",  "name": "English",  "icon": "📖", "color": "#2E7D32"},
        {"key": "urdu",     "name": "Urdu",      "icon": "📝", "color": "#00695C"},
        {"key": "maths",    "name": "Maths",     "icon": "🔢", "color": "#1565C0"},
        {"key": "colors",   "name": "Colors",    "icon": "🎨", "color": "#AD1457"},
        {"key": "shapes",   "name": "Shapes",    "icon": "📐", "color": "#E65100"},
        {"key": "animals",  "name": "Animals",   "icon": "🐾", "color": "#558B2F"},
    ]

    # Progress bars
    progress_controls = []
    for subj in subjects_info:
        score = progress.get(subj["key"], 0)
        max_score = 50
        bar_value = min(score / max_score, 1.0)

        progress_controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(f"{subj['icon']} {subj['name']}", size=16, color="white", weight=ft.FontWeight.W_500),
                        ft.Text(f"{score} pts", size=14, color=subj["color"], weight=ft.FontWeight.BOLD),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.ProgressBar(value=bar_value, color=subj["color"], bgcolor="#263238", height=8),
                ], spacing=6),
                padding=ft.Padding(0, 6, 0, 6),
            )
        )

    # Badge gallery
    badge_controls = []
    for badge_key, badge_info in BADGES.items():
        earned = badge_key in earned_badges
        badge_controls.append(
            ft.Container(
                content=ft.Column([
                    ft.Text(badge_info["icon"], size=32),
                    ft.Text(
                        badge_info["name"], size=11,
                        color="white" if earned else "#546e7a",
                        weight=ft.FontWeight.BOLD if earned else ft.FontWeight.NORMAL,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                bgcolor="#1e3a3a" if earned else "#1a2030",
                border_radius=16,
                padding=12,
                width=95,
                height=95,
                opacity=1.0 if earned else 0.4,
                border=ft.Border.all(2, "#FFD600") if earned else None,
            )
        )

    def on_reset(e):
        def confirm_reset(e2):
            storage.reset_all()
            page.pop_dialog()
            nav.go_home()

        dlg = ft.AlertDialog(
            title=ft.Text("Reset All Progress?"),
            content=ft.Text("This will delete all stars, badges, and progress. Are you sure?"),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e2: page.pop_dialog()),
                ft.TextButton("Reset", on_click=confirm_reset,
                              style=ft.ButtonStyle(color="#EF5350")),
            ],
        )
        page.show_dialog(dlg)

    view = ft.Container(
        content=ft.Column([
            # Top bar
            ft.Row([
                ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white",
                              on_click=lambda e: nav.go_home()),
                ft.Text("📊 My Progress", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.Container(
                    content=ft.Text(f"⭐ {total_stars}", size=16, color="#FFD600", weight=ft.FontWeight.BOLD),
                    bgcolor="#2a2a3e", border_radius=20,
                    padding=ft.Padding(14, 6, 14, 6),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            ft.Divider(height=5, color="transparent"),

            # Subject progress
            ft.Container(
                content=ft.Column([
                    ft.Text("Subject Scores", size=18, weight=ft.FontWeight.BOLD, color="white"),
                    *progress_controls,
                ], spacing=4),
                bgcolor="#1e2a38", border_radius=16, padding=20,
            ),

            ft.Divider(height=10, color="transparent"),

            # Badge gallery
            ft.Container(
                content=ft.Column([
                    ft.Text(f"🏅 Badges ({len(earned_badges)}/{len(BADGES)})",
                            size=18, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Divider(height=5, color="transparent"),
                    ft.Row(
                        controls=badge_controls,
                        wrap=True, spacing=8, run_spacing=8,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ], spacing=4),
                bgcolor="#1e2a38", border_radius=16, padding=20,
            ),

            ft.Divider(height=10, color="transparent"),

            # Reset
            ft.Row([
                ft.TextButton(
                    "🗑️ Reset All Progress",
                    style=ft.ButtonStyle(color="#EF5350"),
                    on_click=on_reset,
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ], scroll=ft.ScrollMode.AUTO, expand=True, spacing=5),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=["#1a1a2e", "#16213e", "#0f3460"],
        ),
        padding=20,
        expand=True,
    )

    return view
