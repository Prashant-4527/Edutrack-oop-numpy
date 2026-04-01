"""
EduTrack — Student Performance Intelligence System
===================================================
Module: analysis.py
Description: NumPy-powered analysis engine
             Arrays, Broadcasting, Boolean Masking,
             Reshaping, Stacking, Splitting

Author: Prashant-kun
Phase: 1 — Foundation (April 2026)
"""

import numpy as np
from student import Student


class PerformanceAnalyzer:
    """
    Analyzes student performance data using NumPy.

    Demonstrates:
    - Array creation and manipulation
    - Statistical operations with axis
    - Boolean masking for filtering
    - Broadcasting for bulk operations
    - Reshaping and splitting for ML prep
    """

    def __init__(self, students: list, subject_names: list):
        """
        Initialize analyzer with list of Student objects.

        Args:
            students      (list): List of Student objects
            subject_names (list): Names of subjects in order
        """
        self.students      = students
        self.subject_names = np.array(subject_names)
        self.names         = np.array([s.name for s in students])

        # ── Build marks matrix using NumPy ───────────────────
        # Each row = one student, each column = one subject
        # Shape: (num_students, num_subjects)
        self.marks_matrix  = np.array([s.marks for s in students])

        print(f"✅ Analyzer ready: {self.marks_matrix.shape[0]} students, "
              f"{self.marks_matrix.shape[1]} subjects")
        print(f"   Matrix shape: {self.marks_matrix.shape}")

    # ── 1. Basic Statistics ───────────────────────────────────
    def class_overview(self):
        """
        Prints overall class health report.
        Uses: np.mean, np.max, np.min, np.std — all with axis
        """
        print("\n" + "=" * 55)
        print("           CLASS OVERVIEW REPORT")
        print("=" * 55)

        # Overall stats
        print(f"\nOverall class average : {np.mean(self.marks_matrix):.2f}")
        print(f"Highest mark          : {np.max(self.marks_matrix)}")
        print(f"Lowest mark           : {np.min(self.marks_matrix)}")
        print(f"Standard deviation    : {np.std(self.marks_matrix):.2f}")

        # axis=0 → per column → per subject average
        subject_avgs = np.mean(self.marks_matrix, axis=0)
        print(f"\n{'Subject':<14} {'Average':>8} {'Best':>6} {'Worst':>7}")
        print("-" * 38)
        for i, subject in enumerate(self.subject_names):
            print(f"{subject:<14} {subject_avgs[i]:>8.1f} "
                  f"{np.max(self.marks_matrix[:, i]):>6} "
                  f"{np.min(self.marks_matrix[:, i]):>7}")

        best_subj  = self.subject_names[np.argmax(subject_avgs)]
        worst_subj = self.subject_names[np.argmin(subject_avgs)]
        print(f"\n🏆 Best subject  : {best_subj} ({np.max(subject_avgs):.1f})")
        print(f"⚠️  Weak subject  : {worst_subj} ({np.min(subject_avgs):.1f})")

    # ── 2. Student Rankings ───────────────────────────────────
    def rank_students(self):
        """
        Ranks all students by average marks.
        Uses: np.mean axis=1, np.argsort, np.where
        """
        print("\n" + "=" * 55)
        print("           STUDENT RANKINGS")
        print("=" * 55)

        # axis=1 → per row → per student average
        student_avgs = np.mean(self.marks_matrix, axis=1)

        # argsort gives ascending → [::-1] reverses to descending
        ranked_idx = np.argsort(student_avgs)[::-1]

        # np.where for grade assignment
        grades = np.where(student_avgs >= 90, "A",
                 np.where(student_avgs >= 75, "B",
                 np.where(student_avgs >= 60, "C", "F")))

        print(f"\n{'Rank':<6} {'Name':<14} {'Average':>8} {'Grade':>6} {'Status':>12}")
        print("-" * 50)

        for rank, idx in enumerate(ranked_idx, 1):
            status = "🏆 Top 3"   if rank <= 3           else \
                     "⚠️  At Risk" if grades[idx] == "F"  else ""
            print(f"{rank:<6} {self.names[idx]:<14} "
                  f"{student_avgs[idx]:>8.1f} "
                  f"{grades[idx]:>6} "
                  f"{status:>12}")

        return student_avgs, grades

    # ── 3. Boolean Masking — Filtering ───────────────────────
    def find_at_risk_students(self, threshold: float = 60.0):
        """
        Finds students below a threshold using boolean masking.
        Uses: Boolean mask, np.any for subject-level detection
        """
        print("\n" + "=" * 55)
        print(f"    AT-RISK STUDENTS (Average < {threshold})")
        print("=" * 55)

        student_avgs = np.mean(self.marks_matrix, axis=1)

        # Boolean mask — True where average is below threshold
        at_risk_mask     = student_avgs < threshold
        at_risk_names    = self.names[at_risk_mask]
        at_risk_avgs     = student_avgs[at_risk_mask]

        if len(at_risk_names) == 0:
            print("\n✅ No students at risk! Great class performance.")
            return

        print(f"\n{'Name':<14} {'Average':>8} {'Weak Subjects':>20}")
        print("-" * 46)

        for i, name in enumerate(at_risk_names):
            # Find original index
            orig_idx     = np.where(self.names == name)[0][0]
            # Boolean mask on subjects — marks below 60
            weak_mask    = self.marks_matrix[orig_idx] < 60
            weak_subjects = self.subject_names[weak_mask]
            print(f"{name:<14} {at_risk_avgs[i]:>8.1f} "
                  f"{str(list(weak_subjects)):>20}")

        # np.any — students failing at least ONE subject
        any_subject_fail = np.any(self.marks_matrix < 60, axis=1)
        struggling       = self.names[any_subject_fail]
        print(f"\n⚠️  Students failing at least 1 subject: {list(struggling)}")

    # ── 4. Broadcasting — Bonus Marks ────────────────────────
    def apply_bonus(self, subject_bonus: list):
        """
        Applies different bonus marks per subject using broadcasting.
        Uses: Broadcasting — (n_students, n_subjects) + (n_subjects,)

        Args:
            subject_bonus (list): Bonus marks per subject
        """
        bonus_array  = np.array(subject_bonus)
        boosted      = self.marks_matrix + bonus_array   # broadcasting!
        boosted      = np.clip(boosted, 0, 100)          # cap at 100

        print("\n" + "=" * 55)
        print("    BONUS MARKS APPLIED (Broadcasting)")
        print("=" * 55)
        print(f"\nBonus per subject: {dict(zip(self.subject_names, subject_bonus))}")

        before_avg = np.mean(self.marks_matrix, axis=1)
        after_avg  = np.mean(boosted, axis=1)
        gain       = after_avg - before_avg

        print(f"\n{'Name':<14} {'Before':>8} {'After':>8} {'Gain':>7}")
        print("-" * 40)
        for i, name in enumerate(self.names):
            print(f"{name:<14} {before_avg[i]:>8.1f} "
                  f"{after_avg[i]:>8.1f} +{gain[i]:>5.1f}")

        return boosted

    # ── 5. Normalization ─────────────────────────────────────
    def normalize(self) -> np.ndarray:
        """
        Normalizes marks to 0-1 range for ML.
        Formula: (x - min) / (max - min)
        Uses: Broadcasting for element-wise normalization
        """
        x_min      = np.min(self.marks_matrix)
        x_max      = np.max(self.marks_matrix)
        normalized = (self.marks_matrix - x_min) / (x_max - x_min)

        print("\n" + "=" * 55)
        print("    NORMALIZED DATA (ML Preparation)")
        print("=" * 55)
        print(f"\nOriginal range : {x_min} to {x_max}")
        print(f"Normalized range: {np.min(normalized):.2f} to {np.max(normalized):.2f}")
        print(f"\nNormalized matrix (first 3 students):")
        print(np.round(normalized[:3], 3))

        return normalized

    # ── 6. Train/Test Split ───────────────────────────────────
    def prepare_for_ml(self, test_size: float = 0.2):
        """
        Prepares data for ML — normalizes and splits.
        Uses: Reshaping, Stacking, np.vsplit
        """
        print("\n" + "=" * 55)
        print("    ML DATA PREPARATION PIPELINE")
        print("=" * 55)

        # Features = normalized marks matrix
        X = self.normalize()

        # Target = student averages (what we'd predict)
        y = np.mean(self.marks_matrix, axis=1)

        # Split point
        split = int(len(X) * (1 - test_size))

        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]

        print(f"\n📦 Dataset shape    : {X.shape}")
        print(f"✂️  Split point      : {split} / {len(X)} ({int((1-test_size)*100)}% / {int(test_size*100)}%)")
        print(f"\nX_train : {X_train.shape}  ← model learns from this")
        print(f"X_test  : {X_test.shape}   ← model tested on this (unseen!)")
        print(f"y_train : {y_train.shape}  ← true averages for training")
        print(f"y_test  : {y_test.shape}   ← true averages for evaluation")
        print(f"\n✅ Data ready for scikit-learn!")

        return X_train, X_test, y_train, y_test

    # ── 7. Full Report ────────────────────────────────────────
    def full_report(self):
        """Runs all analysis in sequence — full EduTrack report."""
        self.class_overview()
        self.rank_students()
        self.find_at_risk_students()
        self.prepare_for_ml()
