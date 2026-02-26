"""
Quiz View — shared quiz engine used by all subject modules.
Updated for Flet 0.81.0 compatibility.
"""
import flet as ft
import time
import random

def build_quiz_view(page: ft.Page, subject: str = "english", **kwargs):
    """Build and return the quiz view for a given subject."""
    from models.question import QuestionBank
    nav = page.data["nav"]
    difficulty_mgr = page.data["difficulty_mgr"]
    reward_ctrl = page.data["reward_ctrl"]
    storage = page.data["storage"]

    difficulty = difficulty_mgr.get_difficulty(subject)
    questions = QuestionBank.get_questions(subject, difficulty, count=5)
    if not questions:
        questions = QuestionBank.get_questions(subject, 1, count=5)

    state = {
        "current_index": 0,
        "score": 0,
        "start_time": time.time(),
        "answered": False,
    }

    # ── Subject accent colors ────────────────────────────────────
    subject_colors = {
        "english": "#2E7D32", "urdu": "#00695C", "maths": "#1565C0",
        "colors": "#AD1457", "shapes": "#E65100", "animals": "#558B2F",
    }
    accent = subject_colors.get(subject, "#6200EA")

    progress_text = ft.Text("Question 1 of 5", size=14, color="#90a4ae")
    progress_bar = ft.ProgressBar(value=0, width=300, color=accent, bgcolor="#263238")
    difficulty_chip = ft.Container(
        content=ft.Text(
            difficulty_mgr.get_difficulty_label(difficulty),
            size=12, weight=ft.FontWeight.BOLD, color="white",
        ),
        bgcolor="#263238",
        border_radius=12,
        padding=ft.Padding(12, 4, 12, 4),
    )

    question_text = ft.Text(
        "", size=22, weight=ft.FontWeight.BOLD, color="white",
        text_align=ft.TextAlign.CENTER,
    )

    feedback_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    stars_text = ft.Text("", size=14, color="#FFD600")
    badge_container = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    options_column = ft.Column(spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    next_btn = ft.ElevatedButton(
        "Next Question ➡️", visible=False, bgcolor=accent, color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
    )

    # ── Logic ────────────────────────────────────────────────────

    def load_question():
        idx = state["current_index"]
        if idx >= len(questions):
            show_results()
            return

        q = questions[idx]
        state["start_time"] = time.time()
        state["answered"] = False

        progress_text.value = f"Question {idx + 1} of {len(questions)}"
        progress_bar.value = idx / len(questions)
        feedback_text.value = ""
        stars_text.value = ""
        badge_container.controls.clear()
        next_btn.visible = False

        if q.rtl:
            question_text.text_align = ft.TextAlign.RIGHT
            question_text.rtl = True
        else:
            question_text.text_align = ft.TextAlign.CENTER
            question_text.rtl = False

        question_text.value = q.text

        options_column.controls.clear()
        shuffled = q.options[:]
        random.shuffle(shuffled)
        for opt in shuffled:
            btn = ft.ElevatedButton(
                content=ft.Container(
                    content=ft.Text(opt, size=16, text_align=ft.TextAlign.CENTER, color="white"),
                    alignment=ft.Alignment(0, 0),
                    width=280, padding=10,
                ),
                bgcolor="#263238",
                color="white",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=12),
                ),
                data=opt,
                on_click=lambda e, option=opt: on_answer(e, option),
            )
            options_column.controls.append(btn)

        page.update()

    def on_answer(e, selected_option):
        if state["answered"]:
            return
        state["answered"] = True

        q = questions[state["current_index"]]
        time_taken = time.time() - state["start_time"]
        correct = selected_option == q.correct_answer

        difficulty_mgr.record_answer(subject, correct, time_taken)

        if correct:
            state["score"] += 1
            storage.increment_progress(subject)
            result = reward_ctrl.award_correct_answer(time_taken)

            feedback_text.value = "✅ Correct! Great job!"
            feedback_text.color = "#66BB6A"
            stars_text.value = f"+{result['stars_earned']} ⭐"

            for badge_key in result.get("new_badges", []):
                info = reward_ctrl.get_badge_info(badge_key)
                badge_container.controls.append(
                    ft.Container(
                        content=ft.Text(
                            f"{info['icon']} Badge Unlocked: {info['name']}!",
                            size=14, color="#FFD600", weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        bgcolor="#33691E",
                        border_radius=8,
                        padding=8,
                        animate_opacity=ft.Animation(500, ft.AnimationCurve.EASE_IN),
                    )
                )
        else:
            reward_ctrl.record_wrong_answer()
            feedback_text.value = f"❌ Oops! The answer was: {q.correct_answer}"
            feedback_text.color = "#EF5350"

        for btn in options_column.controls:
            if isinstance(btn, ft.ElevatedButton):
                opt_text = btn.data
                if opt_text == q.correct_answer:
                    btn.bgcolor = "#2E7D32"
                elif opt_text == selected_option and not correct:
                    btn.bgcolor = "#C62828"
                btn.disabled = True

        next_btn.visible = True
        page.update()

    def on_next(e):
        state["current_index"] += 1
        load_question()

    def show_results():
        total = len(questions)
        score = state["score"]
        percentage = (score / total) * 100 if total > 0 else 0
        learner_type = difficulty_mgr.get_learner_type(subject)

        if percentage >= 80:
            emoji, msg = "🏆", "Outstanding!"
        elif percentage >= 60:
            emoji, msg = "⭐", "Great Work!"
        elif percentage >= 40:
            emoji, msg = "👍", "Good Try!"
        else:
            emoji, msg = "💪", "Keep Practicing!"

        options_column.controls.clear()
        question_text.value = ""
        feedback_text.value = ""
        stars_text.value = ""
        progress_text.value = "Quiz Complete!"
        progress_bar.value = 1.0
        next_btn.visible = False
        badge_container.controls.clear()

        result_card = ft.Container(
            content=ft.Column([
                ft.Text(emoji, size=60, text_align=ft.TextAlign.CENTER),
                ft.Text(msg, size=28, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                ft.Text(f"Score: {score}/{total} ({percentage:.0f}%)", size=20, color="#b0bec5", text_align=ft.TextAlign.CENTER),
                ft.Text(f"Your level: {learner_type}", size=16, color="#78909c", text_align=ft.TextAlign.CENTER),
                ft.Divider(height=20, color="transparent"),
                ft.Row([
                    ft.ElevatedButton(
                        "🔄 Retry", bgcolor=accent, color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                        on_click=lambda e: nav.navigate_to("quiz", subject=subject),
                    ),
                    ft.ElevatedButton(
                        "🏠 Home", bgcolor="#263238", color="white",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                        on_click=lambda e: nav.go_home(),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=15),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8),
            bgcolor="#1e2a38",
            border_radius=20,
            padding=30,
            width=380,
        )

        options_column.controls.append(result_card)
        page.update()

    next_btn.on_click = on_next

    # ── Layout ───────────────────────────────────────────────────

    view = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK_ROUNDED, icon_color="white", icon_size=24,
                    on_click=lambda e: nav.navigate_to(subject),
                ),
                ft.Text(
                    f"{subject.capitalize()} Quiz",
                    size=20, weight=ft.FontWeight.BOLD, color="white",
                ),
                difficulty_chip,
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

            ft.Column([progress_text, progress_bar],
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),

            ft.Divider(height=15, color="transparent"),

            ft.Container(
                content=ft.Column([
                    question_text,
                    ft.Divider(height=10, color="transparent"),
                    options_column,
                    ft.Divider(height=8, color="transparent"),
                    feedback_text,
                    stars_text,
                    badge_container,
                    next_btn,
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5,
                    scroll=ft.ScrollMode.AUTO),
                bgcolor="#1e2a38",
                border_radius=20,
                padding=25,
                expand=True,
            ),
        ], spacing=10, expand=True),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=["#1a1a2e", "#16213e", "#0f3460"],
        ),
        padding=20,
        expand=True,
    )

    load_question()
    return view
