# 🎓 EduTrack — Student Performance Intelligence System

> **Phase 1 Project** · Python OOP + NumPy · April 2026  
> Built as part of a structured AI/ML engineering roadmap targeting METI Japan internship (2027) and Mercari Japan (2028)

---

## 📌 What is EduTrack?

EduTrack is a data-driven student performance analysis system built entirely with **Python OOP** and **NumPy**. It demonstrates how clean software design and numerical computing work together to extract real insights from raw data — without any ML library.

This is Phase 1 of a larger project that will evolve into a full EDA system using Pandas, Matplotlib, and Seaborn.

---

## 🧠 Concepts Demonstrated

### Object-Oriented Programming
| Concept | Where Used |
|---|---|
| Classes & Objects | `Student`, `PerformanceAnalyzer` |
| Encapsulation | `@property` with validation on marks |
| Class Variables | `Student.total_students` counter |
| Instance Methods | `average()`, `get_grade()`, `introduce()` |
| Class Methods | `Student.get_total_students()` |
| Static Methods | `Student.validate_mark()` |
| Dunder Methods | `__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__` |
| Inheritance ready | Base class structure for future `TeachingAssistant`, `Examiner` |

### NumPy
| Concept | Where Used |
|---|---|
| Array creation | Building marks matrix from student objects |
| `axis=0` / `axis=1` | Subject averages vs student averages |
| Boolean Masking | Filtering at-risk students, weak subjects |
| Broadcasting | Applying subject-wise bonus marks |
| `np.argsort` | Ranking students by performance |
| `np.where` | Grade assignment without loops |
| `np.any` | Detecting students failing any subject |
| Normalization | Scaling data to 0–1 for ML readiness |
| Train/Test Split | 80/20 split for scikit-learn preparation |

---

## 📁 Project Structure

```
edutrack-oop-numpy/
│
├── student.py      # Student class — OOP core
│                   # Properties, validation, dunder methods
│
├── analysis.py     # PerformanceAnalyzer class
│                   # NumPy-powered analysis engine
│
├── main.py         # Entry point — runs full pipeline
│
└── README.md       # This file
```

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/Prashant-4527/edutrack-oop-numpy.git
cd edutrack-oop-numpy

# Install dependency
pip install numpy

# Run
python main.py
```

---

## 📊 Sample Output

```
🎓 EDUTRACK — Student Intelligence System
     Built with Python OOP + NumPy

✅ Total students created: 10

═══════════════════════════════════════════════════════
           CLASS OVERVIEW REPORT
═══════════════════════════════════════════════════════

Overall class average : 77.54
Highest mark          : 96
Lowest mark           : 50
Standard deviation    : 12.37

Subject        Average   Best   Worst
──────────────────────────────────────
Python           77.8     95      55
SQL              77.1     92      55
Math             77.1     92      50
English          77.5     93      58
Science          78.2     96      58

🏆 Best subject  : Science (78.2)
⚠️  Weak subject  : SQL (77.1)

═══════════════════════════════════════════════════════
           STUDENT RANKINGS
═══════════════════════════════════════════════════════

Rank   Name           Average  Grade       Status
──────────────────────────────────────────────────────
1      Ananya            92.4      A      🏆 Top 3
2      Arjun             90.2      A      🏆 Top 3
3      Prashant          86.4      B      🏆 Top 3
4      Aisha             87.0      B
5      Vikram            81.0      B
...
10     Sneha             57.0      F    ⚠️  At Risk
```

---

## 🔑 Key Design Decisions

**Why OOP instead of plain functions?**  
Each student is a self-contained entity with its own data (marks, age) and behavior (average, grade). OOP lets us model this naturally. Scaling from 10 to 500 students requires zero architectural changes.

**Why `@property` for marks validation?**  
Without validation, a student could have marks of `-999` or `"hello"` — breaking every calculation silently. The setter catches bad data at the point of entry, not 10 lines later when it causes a crash.

**Why NumPy instead of pure Python?**  
NumPy's vectorized operations (broadcasting, masking, axis-based stats) are 50x faster than Python loops on large datasets. This matters when scaling from 10 students to 10,000. It also mirrors real ML pipelines which are built entirely on NumPy arrays.

**Why normalize data at the end?**  
Most ML algorithms (Linear Regression, Neural Networks) are sensitive to feature scale. A mark of 95 and a mark of 55 are 40 units apart — normalization maps everything to 0.0–1.0, making algorithms converge faster and perform better.

---

## 🗺️ Roadmap

This project is Phase 1 of a larger engineering roadmap:

```
Phase 1 (Apr 2026)  → EduTrack OOP + NumPy        ← YOU ARE HERE
Phase 2 (May 2026)  → EduTrack + Pandas EDA
Phase 3 (Jun 2026)  → EduTrack + Matplotlib/Seaborn visualizations
Phase 4 (Aug 2026)  → EduTrack + ML predictions (scikit-learn)
Phase 5 (Dec 2026)  → EduTrack + AI chatbot (LangChain + RAG)
```

---

## 🎯 Skills Targeted

This project was built as part of preparation for:
- **METI Japan Internship** (Apply May–Jun 2027)
- **Germany Internship** (Jan–Jul 2028)
- **Mercari Japan** (Apply Jul 2028)

---

## 👨‍💻 Author

**Prashant** · BCA Student · Jaipur, India  
Self-directed AI/ML Engineering path  
GitHub: [@Prashant-4527](https://github.com/Prashant-4527)

---

*Built with focus, consistency, and zero tutorials — just Python, NumPy, and deep understanding.*
