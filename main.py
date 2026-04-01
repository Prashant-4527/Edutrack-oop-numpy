"""
EduTrack — Student Performance Intelligence System
===================================================
Module: main.py
Description: Entry point — runs full EduTrack analysis

Author: Prashant-kun
Phase: 1 — Foundation (April 2026)
"""

import numpy as np
from student import Student
from analysis import PerformanceAnalyzer


def main():

    print("=" * 55)
    print("   🎓 EDUTRACK — Student Intelligence System")
    print("        Built with Python OOP + NumPy")
    print("=" * 55)

    # ── Subject Names ─────────────────────────────────────────
    subjects = ["Python", "SQL", "Math", "English", "Science"]

    # ── Create Student Objects ────────────────────────────────
    students = [
        Student("Prashant", 17, [87, 92, 78, 85, 90]),
        Student("Rahul",    18, [72, 68, 80, 75, 70]),
        Student("Ananya",   18, [95, 88, 92, 91, 96]),
        Student("Rohan",    17, [60, 55, 62, 58, 65]),
        Student("Priya",    18, [78, 82, 75, 80, 77]),
        Student("Arjun",    19, [91, 90, 88, 93, 89]),
        Student("Sneha",    17, [55, 60, 50, 62, 58]),
        Student("Vikram",   18, [83, 79, 85, 76, 82]),
        Student("Kavya",    17, [69, 72, 70, 68, 71]),
        Student("Aisha",    18, [88, 85, 91, 87, 84]),
    ]

    print(f"\n✅ Total students created: {Student.get_total_students()}")

    # ── Individual Student Demo ───────────────────────────────
    print("\n" + "─" * 55)
    print("  INDIVIDUAL STUDENT DEMO")
    print("─" * 55)

    for s in students[:3]:
        print(s)              # uses __str__

    print(f"\n{students[0].introduce()}")
    print(f"Repr: {repr(students[0])}")   # uses __repr__
    print(f"Subjects count: {len(students[0])}")  # uses __len__

    # Sorting works because of __lt__
    sorted_students = sorted(students, reverse=True)
    print(f"\n🏆 Top student: {sorted_students[0].name} "
          f"({sorted_students[0].average():.1f})")

    # Validation demo
    print("\n--- Validation Demo ---")
    Student("TestUser", 17, [-10, 50, 200])   # invalid marks
    Student("TestUser", 17, "not a list")      # invalid type

    # ── Full Analysis ─────────────────────────────────────────
    print("\n" + "─" * 55)
    print("  RUNNING FULL ANALYSIS")
    print("─" * 55)

    analyzer = PerformanceAnalyzer(students, subjects)
    analyzer.full_report()

    # ── Broadcasting Demo ─────────────────────────────────────
    # Different bonus per subject
    subject_bonus = [3, 5, 4, 2, 3]   # Python+3, SQL+5, Math+4...
    analyzer.apply_bonus(subject_bonus)


if __name__ == "__main__":
    main()
