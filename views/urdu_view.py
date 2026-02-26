"""
Urdu View — Urdu alphabet and vocabulary with full RTL support.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft

URDU_ALPHABET = [
    "ا", "ب", "پ", "ت", "ٹ", "ث", "ج", "چ", "ح", "خ",
    "د", "ڈ", "ذ", "ر", "ڑ", "ز", "ژ", "س", "ش", "ص",
    "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل",
    "م", "ن", "و", "ہ", "ھ", "ی", "ے",
]

URDU_WORDS = [
    {"urdu": "سیب",     "english": "Apple",      "roman": "Saib"},
    {"urdu": "کتاب",    "english": "Book",       "roman": "Kitaab"},
    {"urdu": "بلی",     "english": "Cat",        "roman": "Billi"},
    {"urdu": "کتا",     "english": "Dog",        "roman": "Kutta"},
    {"urdu": "پانی",    "english": "Water",      "roman": "Paani"},
    {"urdu": "سورج",    "english": "Sun",        "roman": "Sooraj"},
    {"urdu": "چاند",    "english": "Moon",       "roman": "Chaand"},
    {"urdu": "پھول",    "english": "Flower",     "roman": "Phool"},
    {"urdu": "گھر",     "english": "Home",       "roman": "Ghar"},
    {"urdu": "مدرسہ",   "english": "School",     "roman": "Madrasa"},
    {"urdu": "دوست",    "english": "Friend",     "roman": "Dost"},
    {"urdu": "ماں",     "english": "Mother",     "roman": "Maa"},
    {"urdu": "باپ",     "english": "Father",     "roman": "Baap"},
    {"urdu": "بھائی",   "english": "Brother",    "roman": "Bhai"},
    {"urdu": "بہن",     "english": "Sister",     "roman": "Behan"},
]


def build_urdu_view(page: ft.Page, **kwargs):
    """Build the Urdu learning view with RTL support."""
    nav = page.data["nav"]

    # ── Alphabet content ─────────────────────────────────────────
    alphabet_chips = []
    for letter in URDU_ALPHABET:
        alphabet_chips.append(
            ft.Container(
                content=ft.Text(letter, size=28, color="white", text_align=ft.TextAlign.CENTER,
                                rtl=True, weight=ft.FontWeight.BOLD),
                bgcolor="#1e3a3a",
                border_radius=12,
                width=55,
                height=55,
                alignment=ft.Alignment(0, 0),
                border=ft.Border.all(1, "#00695C"),
            )
        )

    alphabet_grid = ft.Row(
        controls=alphabet_chips, wrap=True, spacing=8, run_spacing=8,
        alignment=ft.MainAxisAlignment.CENTER, rtl=True,
    )

    alphabet_panel = ft.Container(
        content=ft.Column([
            ft.Divider(height=10, color="transparent"),
            ft.Text("اردو حروفِ تہجی", size=20, weight=ft.FontWeight.BOLD,
                    color="white", text_align=ft.TextAlign.RIGHT, rtl=True),
            ft.Text("The Urdu Alphabet — 37 letters", size=13, color="#90a4ae"),
            ft.Divider(height=10, color="transparent"),
            alphabet_grid,
        ], scroll=ft.ScrollMode.AUTO, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=ft.Padding(0, 10, 0, 0), expand=True,
    )

    # ── Words content ────────────────────────────────────────────
    def make_word_card(item):
        return ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text(item["english"], size=16, weight=ft.FontWeight.BOLD, color="#80CBC4"),
                    ft.Text(item["roman"], size=13, color="#78909c", italic=True),
                ], spacing=2, expand=True),
                ft.Container(
                    content=ft.Text(
                        item["urdu"], size=26, weight=ft.FontWeight.BOLD,
                        color="white", text_align=ft.TextAlign.RIGHT, rtl=True,
                    ),
                    alignment=ft.Alignment(1, 0), width=120,
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="#1e2a38",
            border_radius=16,
            padding=ft.Padding(20, 14, 20, 14),
            border=ft.Border.all(1, "#00695C44"),
        )

    word_cards = [make_word_card(w) for w in URDU_WORDS]

    words_panel = ft.Container(
        content=ft.Column([
            ft.Divider(height=10, color="transparent"),
            ft.Text("بنیادی اردو الفاظ", size=20, weight=ft.FontWeight.BOLD,
                    color="white", text_align=ft.TextAlign.RIGHT, rtl=True),
            ft.Text("Basic Urdu Vocabulary", size=13, color="#90a4ae"),
            ft.Divider(height=10, color="transparent"),
            *word_cards,
        ], scroll=ft.ScrollMode.AUTO, spacing=10),
        padding=ft.Padding(0, 10, 0, 0), expand=True,
    )

    # ── Manual tab switching ─────────────────────────────────────
    state = {"active_tab": 0}
    tab_panels = [alphabet_panel, words_panel]
    words_panel.visible = False

    def switch_tab(idx):
        state["active_tab"] = idx
        for i, panel in enumerate(tab_panels):
            panel.visible = (i == idx)
        for btn in tab_buttons_row.controls:
            if hasattr(btn, "data"):
                is_active = btn.data == idx
                btn.bgcolor = "#00695C" if is_active else "#1e2a38"
        page.update()

    tab_btn_alphabet = ft.Container(
        content=ft.Text("حروفِ تہجی (Alphabet)", size=14, color="white",
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, rtl=True),
        bgcolor="#00695C", border_radius=12,
        padding=ft.Padding(16, 10, 16, 10), on_click=lambda e: switch_tab(0), data=0,
    )
    tab_btn_words = ft.Container(
        content=ft.Text("الفاظ (Words)", size=14, color="white",
                        weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, rtl=True),
        bgcolor="#1e2a38", border_radius=12,
        padding=ft.Padding(16, 10, 16, 10), on_click=lambda e: switch_tab(1), data=1,
    )

    tab_buttons_row = ft.Row(
        controls=[tab_btn_alphabet, tab_btn_words],
        alignment=ft.MainAxisAlignment.CENTER, spacing=10,
    )

    view = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white",
                              on_click=lambda e: nav.go_home()),
                ft.Text("📝 اردو — Urdu", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.ElevatedButton(
                    "Quiz 🎯", bgcolor="#00695C", color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=lambda e: nav.navigate_to("quiz", subject="urdu"),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=5, color="transparent"),
            tab_buttons_row,
            ft.Divider(height=5, color="transparent"),
            *tab_panels,
        ], spacing=5, expand=True),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=["#1a1a2e", "#16213e", "#0f3460"],
        ),
        padding=20, expand=True,
    )
    return view
