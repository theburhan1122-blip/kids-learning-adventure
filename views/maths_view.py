"""
Maths View — number learning and arithmetic exercises.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft

MATHS_LESSONS = [
    {"topic": "Counting 1–10",    "content": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10",                     "icon": "🔢"},
    {"topic": "Addition (+)",      "content": "Adding means putting numbers together.  2 + 3 = 5",  "icon": "➕"},
    {"topic": "Subtraction (−)",   "content": "Subtracting means taking away.  7 − 4 = 3",          "icon": "➖"},
    {"topic": "Multiplication (×)","content": "Multiplying means adding a number many times. 3 × 4 = 12", "icon": "✖️"},
    {"topic": "Division (÷)",      "content": "Dividing means splitting equally. 12 ÷ 3 = 4",       "icon": "➗"},
    {"topic": "Even & Odd",        "content": "Even: 2,4,6,8  |  Odd: 1,3,5,7,9",                   "icon": "🔄"},
]

TIMES_TABLE = [
    f"{i} × {j} = {i*j}" for i in range(1, 6) for j in range(1, 11)
]


def build_maths_view(page: ft.Page, **kwargs):
    """Build the Maths learning view."""
    nav = page.data["nav"]

    def make_lesson_card(item):
        return ft.Container(
            content=ft.Row([
                ft.Text(item["icon"], size=32),
                ft.Column([
                    ft.Text(item["topic"], size=18, weight=ft.FontWeight.BOLD, color="#64B5F6"),
                    ft.Text(item["content"], size=13, color="#b0bec5"),
                ], spacing=2, expand=True),
            ], spacing=15, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="#1e2a38",
            border_radius=16,
            padding=18,
            border=ft.Border.all(1, "#1565C044"),
        )

    lesson_cards = [make_lesson_card(item) for item in MATHS_LESSONS]

    table_chips = []
    for entry in TIMES_TABLE[:30]:
        table_chips.append(
            ft.Container(
                content=ft.Text(entry, size=13, color="white", text_align=ft.TextAlign.CENTER),
                bgcolor="#1e3050",
                border_radius=10,
                padding=ft.Padding(10, 6, 10, 6),
            )
        )

    # ── Panels ───────────────────────────────────────────────────
    learn_panel = ft.Container(
        content=ft.Column(lesson_cards, spacing=10, scroll=ft.ScrollMode.AUTO),
        padding=ft.Padding(0, 10, 0, 0), expand=True, visible=True,
    )

    tables_panel = ft.Container(
        content=ft.Column([
            ft.Divider(height=10, color="transparent"),
            ft.Text("Times Tables (1–5)", size=18, weight=ft.FontWeight.BOLD, color="white"),
            ft.Divider(height=5, color="transparent"),
            ft.Row(controls=table_chips, wrap=True, spacing=6, run_spacing=6),
        ], scroll=ft.ScrollMode.AUTO),
        padding=ft.Padding(0, 10, 0, 0), expand=True, visible=False,
    )

    panels = [learn_panel, tables_panel]

    def switch_tab(idx):
        for i, panel in enumerate(panels):
            panel.visible = (i == idx)
        for btn in tab_buttons_row.controls:
            if hasattr(btn, "data"):
                is_active = btn.data == idx
                btn.bgcolor = "#1565C0" if is_active else "#1e2a38"
        page.update()

    tab_btn_learn = ft.Container(
        content=ft.Text("📚 Learn", size=14, color="white", weight=ft.FontWeight.BOLD),
        bgcolor="#1565C0", border_radius=12,
        padding=ft.Padding(16, 10, 16, 10), on_click=lambda e: switch_tab(0), data=0,
    )
    tab_btn_tables = ft.Container(
        content=ft.Text("📊 Times Tables", size=14, color="white", weight=ft.FontWeight.BOLD),
        bgcolor="#1e2a38", border_radius=12,
        padding=ft.Padding(16, 10, 16, 10), on_click=lambda e: switch_tab(1), data=1,
    )

    tab_buttons_row = ft.Row(
        controls=[tab_btn_learn, tab_btn_tables],
        alignment=ft.MainAxisAlignment.CENTER, spacing=10,
    )

    view = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white",
                              on_click=lambda e: nav.go_home()),
                ft.Text("🔢 Maths", size=22, weight=ft.FontWeight.BOLD, color="white"),
                ft.ElevatedButton(
                    "Start Quiz 🎯", bgcolor="#1565C0", color="white",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=lambda e: nav.navigate_to("quiz", subject="maths"),
                ),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=5, color="transparent"),
            tab_buttons_row,
            ft.Divider(height=5, color="transparent"),
            *panels,
        ], spacing=5, expand=True),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=["#1a1a2e", "#16213e", "#0f3460"],
        ),
        padding=20, expand=True,
    )
    return view
