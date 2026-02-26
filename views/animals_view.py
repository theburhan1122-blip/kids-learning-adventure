"""
Animals View — animal cards with facts, sounds, and quiz.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft

ANIMALS_DATA = [
    {"name": "Cat",       "emoji": "🐱", "sound": "Meow",   "fact": "Cats sleep 12–16 hours a day!"},
    {"name": "Dog",       "emoji": "🐶", "sound": "Woof",   "fact": "A dog's nose print is unique, like a fingerprint."},
    {"name": "Elephant",  "emoji": "🐘", "sound": "Trumpet", "fact": "Elephants can't jump!"},
    {"name": "Lion",      "emoji": "🦁", "sound": "Roar",   "fact": "A lion's roar can be heard 5 miles away!"},
    {"name": "Bird",      "emoji": "🐦", "sound": "Tweet",  "fact": "Some birds can fly backwards!"},
    {"name": "Fish",      "emoji": "🐟", "sound": "Blub",   "fact": "Fish have been on earth for over 500 million years."},
    {"name": "Horse",     "emoji": "🐴", "sound": "Neigh",  "fact": "Horses can sleep standing up!"},
    {"name": "Cow",       "emoji": "🐮", "sound": "Moo",    "fact": "Cows have best friends!"},
    {"name": "Duck",      "emoji": "🦆", "sound": "Quack",  "fact": "A duck's quack doesn't echo."},
    {"name": "Frog",      "emoji": "🐸", "sound": "Ribbit", "fact": "Frogs drink water through their skin!"},
    {"name": "Owl",       "emoji": "🦉", "sound": "Hoot",   "fact": "Owls can rotate their heads 270 degrees."},
    {"name": "Monkey",    "emoji": "🐵", "sound": "Ooh-ooh","fact": "Monkeys can understand basic maths!"},
]

def build_animals_view(page: ft.Page, **kwargs):
    """Build the Animals learning view."""
    nav = page.data["nav"]

    def make_animal_card(a):
        return ft.Container(
            content=ft.Column([
                ft.Text(a["emoji"], size=38),
                ft.Text(a["name"], size=16, weight=ft.FontWeight.BOLD, color="white"),
                ft.Container(
                    content=ft.Text(f'"{a["sound"]}!"', size=13, color="#AED581", italic=True),
                    bgcolor="#33691E",
                    border_radius=8,
                    padding=ft.Padding(10, 3, 10, 3),
                ),
                ft.Text(a["fact"], size=11, color="#90a4ae", text_align=ft.TextAlign.CENTER),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
            bgcolor="#1e2a38",
            border_radius=16,
            padding=18,
            width=170,
            height=210,
            border=ft.Border.all(1, "#558B2F44"),
        )

    animal_cards = [make_animal_card(a) for a in ANIMALS_DATA]

    view = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white",
                              on_click=lambda e: nav.go_home()),
                ft.Text("🐾 Animals", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.ElevatedButton(
                    "Start Quiz 🎯", bgcolor="#558B2F", color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=lambda e: nav.navigate_to("quiz", subject="animals"),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=10, color="transparent"),
            ft.Row(
                controls=animal_cards,
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
