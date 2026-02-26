"""
Home View — main landing page with subject grid and star counter.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft


def build_home_view(page: ft.Page, **kwargs):
    """Build the colorful home screen with subject cards."""
    nav = page.data["nav"]
    storage = page.data["storage"]

    progress = storage.load_progress()
    total_stars = storage.load_total_stars()
    badges = storage.load_badges()

    subjects = [
        {"name": "English",  "icon": "📖", "desc": "Words & Grammar",  "color": "#2E7D32",  "route": "english"},
        {"name": "Urdu",     "icon": "📝", "desc": "حروف اور الفاظ",    "color": "#00695C",  "route": "urdu"},
        {"name": "Maths",    "icon": "🔢", "desc": "Numbers & Sums",    "color": "#1565C0",  "route": "maths"},
        {"name": "Colors",   "icon": "🎨", "desc": "Learn Colors",      "color": "#AD1457",  "route": "colors"},
        {"name": "Shapes",   "icon": "📐", "desc": "Shapes & Sides",    "color": "#E65100",  "route": "shapes"},
        {"name": "Animals",  "icon": "🐾", "desc": "Animal World",      "color": "#558B2F",  "route": "animals"},
    ]

    def make_subject_card(subj):
        score = progress.get(subj["route"], 0)
        return ft.Container(
            content=ft.Column([
                ft.Text(subj["icon"], size=36),
                ft.Text(subj["name"], size=18, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text(subj["desc"], size=12, color="#ffffffbb"),
                ft.Container(
                    content=ft.Text(f"⭐ {score}", size=12, color="#FFD600"),
                    bgcolor="#1a1a2e",
                    border_radius=8,
                    padding=ft.Padding(8, 2, 8, 2),
                    margin=ft.Margin(0, 5, 0, 0),
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=[subj["color"], "#1a1a2e"],
            ),
            border_radius=20,
            padding=20,
            width=170,
            height=180,
            on_click=lambda e, r=subj["route"]: nav.navigate_to(r),
        )

    cards = [make_subject_card(s) for s in subjects]

    # Top bar
    top_bar = ft.Container(
        content=ft.Row([
            ft.Text("🎓 Smart Learning", size=20, weight=ft.FontWeight.BOLD, color="white"),
            ft.Row([
                ft.Container(
                    content=ft.Text(f"⭐ {total_stars}", size=16, color="#FFD600", weight=ft.FontWeight.BOLD),
                    bgcolor="#2a2a3e",
                    border_radius=20,
                    padding=ft.Padding(14, 6, 14, 6),
                ),
                ft.Container(
                    content=ft.Text(f"🏅 {len(badges)}", size=16, color="#FF9800", weight=ft.FontWeight.BOLD),
                    bgcolor="#2a2a3e",
                    border_radius=20,
                    padding=ft.Padding(14, 6, 14, 6),
                    on_click=lambda e: nav.navigate_to("progress"),
                ),
            ], spacing=8),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.Padding(0, 0, 0, 10),
    )

    # Welcome message
    welcome = ft.Container(
        content=ft.Column([
            ft.Text("Welcome, Explorer! 🚀", size=26, weight=ft.FontWeight.BOLD,
                     color="white", text_align=ft.TextAlign.CENTER),
            ft.Text("Choose a subject and start your adventure!", size=14, color="#ffffffaa",
                     text_align=ft.TextAlign.CENTER),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
        padding=ft.Padding(0, 15, 0, 15),
    )

    # Subject grid
    grid = ft.Row(
        controls=cards,
        wrap=True,
        spacing=15,
        run_spacing=15,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # Bottom buttons
    bottom = ft.Container(
        content=ft.TextButton(
            "📊 My Progress",
            style=ft.ButtonStyle(color="white"),
            on_click=lambda e: nav.navigate_to("progress"),
        ),
        padding=ft.Padding(0, 10, 0, 0),
    )

    view = ft.Container(
        content=ft.Column([
            top_bar,
            welcome,
            grid,
            bottom,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO, expand=True),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=["#1a1a2e", "#16213e", "#0f3460"],
        ),
        padding=20,
        expand=True,
    )
    return view
