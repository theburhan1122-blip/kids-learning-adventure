"""
Colors View — color learning with interactive swatches and quiz.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft

COLORS_DATA = [
    {"name": "Red",    "hex": "#F44336", "fact": "Red means stop — look at traffic lights!"},
    {"name": "Blue",   "hex": "#2196F3", "fact": "The sky and ocean appear blue."},
    {"name": "Green",  "hex": "#4CAF50", "fact": "Plants are green because of chlorophyll!"},
    {"name": "Yellow", "hex": "#FFEB3B", "fact": "Sunflowers and school buses are yellow!"},
    {"name": "Orange", "hex": "#FF9800", "fact": "Oranges got their name from the color!"},
    {"name": "Purple", "hex": "#9C27B0", "fact": "Purple is the color of royalty."},
    {"name": "Pink",   "hex": "#E91E63", "fact": "Flamingos are pink from the shrimp they eat!"},
    {"name": "Brown",  "hex": "#795548", "fact": "Chocolate and wood are brown!"},
    {"name": "Black",  "hex": "#424242", "fact": "Black absorbs all light!"},
    {"name": "White",  "hex": "#FAFAFA", "fact": "Snow and clouds are white!"},
]

def build_colors_view(page: ft.Page, **kwargs):
    """Build the Colors learning view."""
    nav = page.data["nav"]

    def make_color_card(c):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    width=70, height=70,
                    bgcolor=c["hex"],
                    border_radius=35,
                    border=ft.Border.all(3, "#ffffff44"),
                    shadow=ft.BoxShadow(spread_radius=0, blur_radius=12, color=c["hex"]),
                ),
                ft.Text(c["name"], size=18, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text(c["fact"], size=11, color="#90a4ae", text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
            bgcolor="#1e2a38",
            border_radius=20,
            padding=20,
            width=170,
            border=ft.Border.all(1, "#AD145744"),
        )

    color_cards = [make_color_card(c) for c in COLORS_DATA]

    view = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white",
                              on_click=lambda e: nav.go_home()),
                ft.Text("🎨 Colors", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.ElevatedButton(
                    "Start Quiz 🎯", bgcolor="#AD1457", color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=lambda e: nav.navigate_to("quiz", subject="colors"),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=10, color="transparent"),
            ft.Row(
                controls=color_cards,
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
