"""
Shapes View — shape learning with visual cards and quiz.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft

SHAPES_DATA = [
    {"name": "Circle",    "emoji": "⚫", "sides": 0,  "fact": "A circle has no corners — every point is the same distance from the center!"},
    {"name": "Triangle",  "emoji": "🔺", "sides": 3,  "fact": "The pyramids of Egypt are giant triangles!"},
    {"name": "Square",    "emoji": "🟧", "sides": 4,  "fact": "A square has 4 equal sides and 4 right angles."},
    {"name": "Rectangle", "emoji": "📱", "sides": 4,  "fact": "Your phone screen is a rectangle!"},
    {"name": "Pentagon",  "emoji": "⬠",  "sides": 5,  "fact": "The US Pentagon building has 5 sides!"},
    {"name": "Hexagon",   "emoji": "⬡",  "sides": 6,  "fact": "Honeybee combs are hexagonal — nature's engineers!"},
    {"name": "Star",      "emoji": "⭐", "sides": 10, "fact": "Most drawn stars have 5 points!"},
    {"name": "Diamond",   "emoji": "💎", "sides": 4,  "fact": "A diamond shape is a tilted square (rhombus)."},
    {"name": "Heart",     "emoji": "❤️", "sides": 0,  "fact": "The heart shape has been a symbol of love for centuries!"},
    {"name": "Oval",      "emoji": "🥚", "sides": 0,  "fact": "An oval is like a stretched circle — eggs are oval!"},
]

def build_shapes_view(page: ft.Page, **kwargs):
    """Build the Shapes learning view."""
    nav = page.data["nav"]

    def make_shape_card(s):
        return ft.Container(
            content=ft.Column([
                ft.Text(s["emoji"], size=38),
                ft.Text(s["name"], size=16, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text(f"{s['sides']} sides" if s["sides"] > 0 else "Curved", size=12, color="#FFB74D"),
                ft.Text(s["fact"], size=10, color="#90a4ae", text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
            bgcolor="#1e2a38",
            border_radius=16,
            padding=18,
            width=170,
            height=190,
            border=ft.Border.all(1, "#E6510044"),
        )

    shape_cards = [make_shape_card(s) for s in SHAPES_DATA]

    view = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white",
                              on_click=lambda e: nav.go_home()),
                ft.Text("📐 Shapes", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.ElevatedButton(
                    "Start Quiz 🎯", bgcolor="#E65100", color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=lambda e: nav.navigate_to("quiz", subject="shapes"),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=10, color="transparent"),
            ft.Row(
                controls=shape_cards,
                wrap=True, spacing=12, run_spacing=12,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ], spacing=5, expand=True, scroll=ft.ScrollMode.AUTO),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=["#1a1a2e", "#16213e", "#0f3460"],
        ),
        padding=20, expand=True,
    )
    return view
