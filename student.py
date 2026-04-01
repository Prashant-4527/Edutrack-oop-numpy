"""
EduTrack — Student Performance Intelligence System
===================================================
Module: student.py
Description: Core Student class with OOP principles
             Encapsulation, Properties, Dunder Methods

Author: Prashant-kun
Phase: 1 — Foundation (April 2026)
"""

import numpy as np


class Student:
    """
    Represents a student in the EduTrack system.

    Features:
    - Encapsulated marks with full validation
    - NumPy-powered statistics
    - Grade calculation
    - Dunder methods for clean output
    """

    # ── Class Variable ────────────────────────────────────────
    total_students = 0    # shared counter — tracks all students created

    # ── Constructor ───────────────────────────────────────────
    def __init__(self, name: str, age: int, marks: list):
        """
        Initialize a Student object.

        Args:
            name  (str):   Student's full name
            age   (int):   Student's age
            marks (list):  List of marks (0-100 each)
        """
        self.name    = name
        self.age     = age
        self._marks  = []       # private variable — safe default first
        self.marks   = marks    # calls the setter for validation
        Student.total_students += 1

    # ── Property: Getter ──────────────────────────────────────
    @property
    def marks(self) -> list:
        """Returns the student's marks (read via getter)."""
        return self._marks

    # ── Property: Setter with Validation ─────────────────────
    @marks.setter
    def marks(self, value):
        """
        Validates and sets marks.
        Rules:
        - Must be a list
        - Each mark must be int or float
        - Each mark must be between 0 and 100
        """
        if not isinstance(value, list):
            print(f"❌ Error: Marks must be a list, got {type(value).__name__}")
            return

        if any(
            (not isinstance(x, (int, float)) or x < 0 or x > 100)
            for x in value
        ):
            print("❌ Error: Each mark must be a number between 0 and 100.")
            return

        self._marks = value
        print(f"✅ Marks set successfully for {self.name}")

    # ── Instance Methods ──────────────────────────────────────
    def average(self) -> float:
        """Returns the student's average mark using NumPy."""
        if not self._marks:
            return 0.0
        return round(float(np.mean(np.array(self._marks))), 2)

    def get_grade(self) -> str:
        """
        Returns letter grade based on average.
        A  → 90 and above
        B  → 75 to 89
        C  → 60 to 74
        F  → below 60
        """
        avg = self.average()
        return str(np.where(avg >= 90, "A",
               np.where(avg >= 75, "B",
               np.where(avg >= 60, "C", "F"))))

    def is_passing(self) -> bool:
        """Returns True if student's average is 60 or above."""
        return self.average() >= 60

    def highest_mark(self) -> float:
        """Returns the highest mark using NumPy."""
        return float(np.max(np.array(self._marks))) if self._marks else 0.0

    def lowest_mark(self) -> float:
        """Returns the lowest mark using NumPy."""
        return float(np.min(np.array(self._marks))) if self._marks else 0.0

    def introduce(self) -> str:
        """Returns a friendly introduction string."""
        status = "passing ✅" if self.is_passing() else "needs support ⚠️"
        return (
            f"Hi! I'm {self.name}, {self.age} years old. "
            f"My average is {self.average():.1f} — Grade {self.get_grade()} — {status}"
        )

    # ── Class Method ──────────────────────────────────────────
    @classmethod
    def get_total_students(cls) -> int:
        """Returns total number of students created."""
        return cls.total_students

    # ── Static Method ─────────────────────────────────────────
    @staticmethod
    def validate_mark(mark) -> bool:
        """
        Validates a single mark.
        Returns True if valid (0-100 number), False otherwise.
        """
        return isinstance(mark, (int, float)) and 0 <= mark <= 100

    # ── Dunder Methods ────────────────────────────────────────
    def __str__(self) -> str:
        """Human-readable string — for print()"""
        return (
            f"Student: {self.name:<12} | "
            f"Age: {self.age} | "
            f"Avg: {self.average():.1f} | "
            f"Grade: {self.get_grade()} | "
            f"Status: {'Pass' if self.is_passing() else 'Fail'}"
        )

    def __repr__(self) -> str:
        """Developer string — for debugging"""
        return f"Student(name='{self.name}', age={self.age}, marks={self._marks})"

    def __eq__(self, other) -> bool:
        """Two students are equal if same name and same average."""
        return self.name == other.name and self.average() == other.average()

    def __lt__(self, other) -> bool:
        """Enables sorting students by average (ascending)."""
        return self.average() < other.average()

    def __len__(self) -> int:
        """Returns number of subjects (marks entries)."""
        return len(self._marks)
