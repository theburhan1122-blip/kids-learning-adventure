"""
English View — vocabulary learning and quiz launcher.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft

ENGLISH_LESSONS = [
    {"word": "Apple",     "meaning": "A round red or green fruit",           "example": "I eat an apple every day."},
    {"word": "Book",      "meaning": "A set of written pages",               "example": "She reads a book before bed."},
    {"word": "Cat",       "meaning": "A small furry pet",                    "example": "The cat likes to sleep."},
    {"word": "Dog",       "meaning": "A loyal animal friend",                "example": "My dog loves to play fetch."},
    {"word": "Elephant",  "meaning": "The largest land animal",              "example": "An elephant never forgets."},
    {"word": "Fish",      "meaning": "An animal that lives in water",        "example": "We saw colorful fish in the pond."},
    {"word": "Garden",    "meaning": "A place where plants grow",            "example": "She planted roses in the garden."},
    {"word": "House",     "meaning": "A building where people live",         "example": "They live in a big house."},
    {"word": "Ice cream", "meaning": "A frozen sweet treat",                 "example": "I love chocolate ice cream!"},
    {"word": "Juice",     "meaning": "A drink made from fruit",              "example": "Orange juice is refreshing."},
    {"word": "Kite",      "meaning": "A toy that flies in the wind",         "example": "We flew a kite at the beach."},
    {"word": "Lion",      "meaning": "A large wild cat, king of the jungle", "example": "The lion roared loudly."},
]

def build_english_view(page: ft.Page, **kwargs):
    """Build the English learning view."""
    nav = page.data["nav"]

    def make_word_card(item):
        return ft.Container(
            content=ft.Row([
                ft.Text("📗", size=28),
                ft.Column([
                    ft.Text(item["word"], size=18, weight=ft.FontWeight.BOLD, color="#81C784"),
                    ft.Text(item["meaning"], size=13, color="#b0bec5"),
                    ft.Text(f'"{item["example"]}"', size=12, color="#78909c", italic=True),
                ], spacing=2, expand=True),
            ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="#1e2a38",
            border_radius=16,
            padding=18,
            border=ft.Border.all(1, "#2E7D3244"),
        )

    word_cards = [make_word_card(item) for item in ENGLISH_LESSONS]

    view = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white",
                              on_click=lambda e: nav.go_home()),
                ft.Text("📖 English", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.ElevatedButton(
                    "Start Quiz 🎯", bgcolor="#2E7D32", color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=lambda e: nav.navigate_to("quiz", subject="english"),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=10, color="transparent"),
            ft.Column(controls=word_cards, spacing=10, scroll=ft.ScrollMode.AUTO, expand=True),
        ], spacing=5, expand=True),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=["#1a1a2e", "#16213e", "#0f3460"],
        ),
        padding=20,
        expand=True,
    )
    return view
