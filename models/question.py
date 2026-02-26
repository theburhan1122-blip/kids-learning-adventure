"""
Question model and QuestionBank for all subjects.
"""
from dataclasses import dataclass, field
from typing import List
import random


@dataclass
class Question:
    """Represents a single quiz question."""
    text: str
    options: List[str]
    correct_answer: str
    difficulty: int  # 1=easy, 2=medium, 3=hard
    subject: str
    rtl: bool = False  # True for Urdu questions


class QuestionBank:
    """Static question data for all 6 subjects at 3 difficulty levels."""

    _questions = {
        # ── ENGLISH ──────────────────────────────────────────────
        "english": [
            # Difficulty 1 — Easy
            Question("What letter does 'Apple' start with?", ["A", "B", "C", "D"], "A", 1, "english"),
            Question("What is the opposite of 'Hot'?", ["Cold", "Warm", "Big", "Small"], "Cold", 1, "english"),
            Question("Which word means a baby cat?", ["Puppy", "Kitten", "Cub", "Foal"], "Kitten", 1, "english"),
            Question("Complete: 'The sun is ___'.", ["Yellow", "Green", "Blue", "Purple"], "Yellow", 1, "english"),
            Question("Which is a fruit?", ["Chair", "Mango", "Book", "Pen"], "Mango", 1, "english"),
            # Difficulty 2 — Medium
            Question("What is the plural of 'Child'?", ["Childs", "Children", "Childes", "Childern"], "Children", 2, "english"),
            Question("Choose the correct spelling:", ["Beautyful", "Beautful", "Beautiful", "Beutiful"], "Beautiful", 2, "english"),
            Question("Which is a verb?", ["Happy", "Run", "Blue", "Table"], "Run", 2, "english"),
            Question("What is the past tense of 'Go'?", ["Goed", "Gone", "Went", "Goes"], "Went", 2, "english"),
            Question("Fill in: 'She ___ to school every day.'", ["go", "goes", "going", "gone"], "goes", 2, "english"),
            # Difficulty 3 — Hard
            Question("Which sentence is correct?", ["He don't like it.", "He doesn't likes it.", "He doesn't like it.", "He not like it."], "He doesn't like it.", 3, "english"),
            Question("What is a synonym for 'Happy'?", ["Sad", "Angry", "Joyful", "Tired"], "Joyful", 3, "english"),
            Question("Identify the adjective: 'The tall boy runs fast.'", ["boy", "runs", "tall", "fast"], "tall", 3, "english"),
            Question("Which word is an adverb?", ["Quick", "Quickly", "Quicker", "Quickest"], "Quickly", 3, "english"),
            Question("Choose the correct sentence:", ["Their going home.", "They're going home.", "There going home.", "Theyre going home."], "They're going home.", 3, "english"),
        ],

        # ── URDU ─────────────────────────────────────────────────
        "urdu": [
            # Difficulty 1 — Easy
            Question("'سیب' کا مطلب کیا ہے؟", ["Apple", "Banana", "Mango", "Orange"], "Apple", 1, "urdu", rtl=True),
            Question("'بلی' کا مطلب کیا ہے؟", ["Dog", "Cat", "Bird", "Fish"], "Cat", 1, "urdu", rtl=True),
            Question("'پانی' کا انگریزی کیا ہے؟", ["Fire", "Water", "Air", "Earth"], "Water", 1, "urdu", rtl=True),
            Question("'کتاب' کا مطلب کیا ہے؟", ["Pen", "Book", "Chair", "Table"], "Book", 1, "urdu", rtl=True),
            Question("اردو حروف میں پہلا حرف کون سا ہے؟", ["ب", "الف", "پ", "ت"], "الف", 1, "urdu", rtl=True),
            # Difficulty 2 — Medium
            Question("'خوبصورت' کا مطلب کیا ہے؟", ["Ugly", "Beautiful", "Tall", "Small"], "Beautiful", 2, "urdu", rtl=True),
            Question("'مدرسہ' کا مطلب کیا ہے؟", ["Hospital", "Market", "School", "House"], "School", 2, "urdu", rtl=True),
            Question("'سورج' کا انگریزی کیا ہے؟", ["Moon", "Star", "Sun", "Cloud"], "Sun", 2, "urdu", rtl=True),
            Question("'دوست' کا مطلب کیا ہے؟", ["Enemy", "Friend", "Brother", "Teacher"], "Friend", 2, "urdu", rtl=True),
            Question("خالی جگہ پر کریں: 'میں ___ جاتا ہوں'", ["گھر", "کتاب", "پانی", "بلی"], "گھر", 2, "urdu", rtl=True),
            # Difficulty 3 — Hard
            Question("'استاد' کی جمع کیا ہے؟", ["استاد", "اساتذہ", "استادیں", "استادان"], "اساتذہ", 3, "urdu", rtl=True),
            Question("'علم' کا مطلب کیا ہے؟", ["Wealth", "Power", "Knowledge", "Health"], "Knowledge", 3, "urdu", rtl=True),
            Question("اس جملے کو مکمل کریں: 'پاکستان ایک ___ ملک ہے'", ["چھوٹا", "خوبصورت", "بڑا", "پرانا"], "خوبصورت", 3, "urdu", rtl=True),
            Question("'محنت' کی ضد کیا ہے؟", ["سستی", "ہمت", "طاقت", "عزت"], "سستی", 3, "urdu", rtl=True),
            Question("'آسمان' کا رنگ کیا ہے؟", ["سبز", "نیلا", "لال", "پیلا"], "نیلا", 3, "urdu", rtl=True),
        ],

        # ── MATHS ────────────────────────────────────────────────
        "maths": [
            # Difficulty 1 — Easy (single-digit)
            Question("2 + 3 = ?", ["4", "5", "6", "7"], "5", 1, "maths"),
            Question("5 - 2 = ?", ["2", "3", "4", "1"], "3", 1, "maths"),
            Question("1 + 1 = ?", ["1", "2", "3", "0"], "2", 1, "maths"),
            Question("4 + 4 = ?", ["6", "7", "8", "9"], "8", 1, "maths"),
            Question("7 - 3 = ?", ["3", "4", "5", "2"], "4", 1, "maths"),
            # Difficulty 2 — Medium (double-digit)
            Question("12 + 15 = ?", ["25", "27", "26", "28"], "27", 2, "maths"),
            Question("30 - 14 = ?", ["14", "15", "16", "17"], "16", 2, "maths"),
            Question("5 × 3 = ?", ["12", "15", "18", "20"], "15", 2, "maths"),
            Question("20 ÷ 4 = ?", ["4", "5", "6", "7"], "5", 2, "maths"),
            Question("9 × 2 = ?", ["16", "17", "18", "19"], "18", 2, "maths"),
            # Difficulty 3 — Hard (mixed operations)
            Question("(5 + 3) × 2 = ?", ["14", "16", "18", "13"], "16", 3, "maths"),
            Question("45 - 18 + 3 = ?", ["28", "30", "32", "27"], "30", 3, "maths"),
            Question("7 × 8 = ?", ["54", "56", "58", "48"], "56", 3, "maths"),
            Question("100 ÷ 5 = ?", ["15", "20", "25", "10"], "20", 3, "maths"),
            Question("(12 + 8) ÷ 4 = ?", ["4", "5", "6", "7"], "5", 3, "maths"),
        ],

        # ── COLORS ───────────────────────────────────────────────
        "colors": [
            Question("What color is the sky?", ["Red", "Blue", "Green", "Yellow"], "Blue", 1, "colors"),
            Question("What color is grass?", ["Blue", "Red", "Green", "Orange"], "Green", 1, "colors"),
            Question("What color is a banana?", ["Red", "Yellow", "Purple", "Pink"], "Yellow", 1, "colors"),
            Question("What color do you get mixing red and yellow?", ["Green", "Purple", "Orange", "Blue"], "Orange", 1, "colors"),
            Question("What color is snow?", ["White", "Grey", "Blue", "Silver"], "White", 1, "colors"),
            Question("What color is a strawberry?", ["Yellow", "Blue", "Red", "Green"], "Red", 2, "colors"),
            Question("What color do you get mixing blue and yellow?", ["Red", "Orange", "Green", "Purple"], "Green", 2, "colors"),
            Question("What color do you get mixing red and blue?", ["Green", "Yellow", "Purple", "Orange"], "Purple", 2, "colors"),
            Question("What color is chocolate?", ["White", "Brown", "Black", "Red"], "Brown", 2, "colors"),
            Question("Which color represents 'stop' on a traffic light?", ["Green", "Yellow", "Red", "Blue"], "Red", 2, "colors"),
            Question("What is the complementary color of blue?", ["Red", "Orange", "Green", "Yellow"], "Orange", 3, "colors"),
            Question("Which color has the longest wavelength?", ["Blue", "Green", "Red", "Violet"], "Red", 3, "colors"),
            Question("What are the primary colors?", ["Red, Green, Blue", "Red, Yellow, Blue", "Red, Orange, Purple", "Blue, Green, Yellow"], "Red, Yellow, Blue", 3, "colors"),
            Question("What color is indigo closest to?", ["Red", "Blue", "Green", "Yellow"], "Blue", 3, "colors"),
            Question("Mixing all primary colors of light gives?", ["Black", "White", "Grey", "Brown"], "White", 3, "colors"),
        ],

        # ── SHAPES ───────────────────────────────────────────────
        "shapes": [
            Question("How many sides does a triangle have?", ["2", "3", "4", "5"], "3", 1, "shapes"),
            Question("What shape is a ball?", ["Square", "Circle", "Triangle", "Star"], "Circle", 1, "shapes"),
            Question("How many sides does a square have?", ["3", "4", "5", "6"], "4", 1, "shapes"),
            Question("Which shape has no corners?", ["Square", "Triangle", "Circle", "Rectangle"], "Circle", 1, "shapes"),
            Question("What shape is a door?", ["Circle", "Triangle", "Rectangle", "Oval"], "Rectangle", 1, "shapes"),
            Question("How many sides does a pentagon have?", ["4", "5", "6", "7"], "5", 2, "shapes"),
            Question("How many sides does a hexagon have?", ["5", "6", "7", "8"], "6", 2, "shapes"),
            Question("What shape has 8 sides?", ["Hexagon", "Heptagon", "Octagon", "Nonagon"], "Octagon", 2, "shapes"),
            Question("A diamond shape is also called a?", ["Rectangle", "Rhombus", "Trapezoid", "Pentagon"], "Rhombus", 2, "shapes"),
            Question("Which shape has 3 corners?", ["Square", "Circle", "Triangle", "Rectangle"], "Triangle", 2, "shapes"),
            Question("How many degrees in a triangle?", ["90", "180", "270", "360"], "180", 3, "shapes"),
            Question("What is a 10-sided shape called?", ["Nonagon", "Decagon", "Dodecagon", "Hectagon"], "Decagon", 3, "shapes"),
            Question("How many faces does a cube have?", ["4", "6", "8", "12"], "6", 3, "shapes"),
            Question("A 3D circle is called a?", ["Cylinder", "Sphere", "Cone", "Cube"], "Sphere", 3, "shapes"),
            Question("What is the sum of angles in a rectangle?", ["180", "270", "360", "450"], "360", 3, "shapes"),
        ],

        # ── ANIMALS ──────────────────────────────────────────────
        "animals": [
            Question("What sound does a cat make?", ["Woof", "Meow", "Moo", "Baa"], "Meow", 1, "animals"),
            Question("What sound does a dog make?", ["Meow", "Woof", "Quack", "Roar"], "Woof", 1, "animals"),
            Question("Which animal lives in water?", ["Cat", "Dog", "Fish", "Bird"], "Fish", 1, "animals"),
            Question("What animal says 'Moo'?", ["Horse", "Sheep", "Cow", "Pig"], "Cow", 1, "animals"),
            Question("Which animal can fly?", ["Dog", "Fish", "Cat", "Bird"], "Bird", 1, "animals"),
            Question("What is a baby dog called?", ["Kitten", "Puppy", "Calf", "Lamb"], "Puppy", 2, "animals"),
            Question("Which animal is the tallest?", ["Elephant", "Giraffe", "Horse", "Bear"], "Giraffe", 2, "animals"),
            Question("How many legs does a spider have?", ["6", "8", "10", "4"], "8", 2, "animals"),
            Question("Which animal is known as the 'King of the Jungle'?", ["Tiger", "Elephant", "Lion", "Bear"], "Lion", 2, "animals"),
            Question("What do you call a group of fish?", ["Herd", "Flock", "School", "Pack"], "School", 2, "animals"),
            Question("Which animal can change its color?", ["Frog", "Chameleon", "Snake", "Lizard"], "Chameleon", 3, "animals"),
            Question("What is the fastest land animal?", ["Lion", "Horse", "Cheetah", "Gazelle"], "Cheetah", 3, "animals"),
            Question("Which animal has the largest brain?", ["Elephant", "Whale", "Dolphin", "Sperm Whale"], "Sperm Whale", 3, "animals"),
            Question("How many hearts does an octopus have?", ["1", "2", "3", "4"], "3", 3, "animals"),
            Question("Which bird cannot fly?", ["Eagle", "Penguin", "Hawk", "Parrot"], "Penguin", 3, "animals"),
        ],
    }

    @classmethod
    def get_questions(cls, subject: str, difficulty: int, count: int = 5) -> List[Question]:
        """Get randomized questions for a subject at a given difficulty."""
        pool = [q for q in cls._questions.get(subject, []) if q.difficulty == difficulty]
        if not pool:
            # Fallback: get any question for the subject
            pool = cls._questions.get(subject, [])
        return random.sample(pool, min(count, len(pool)))

    @classmethod
    def get_all_subjects(cls) -> List[str]:
        """Return list of all available subjects."""
        return list(cls._questions.keys())
