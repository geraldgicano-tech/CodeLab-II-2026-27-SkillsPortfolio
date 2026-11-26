from pathlib import Path
import shutil
import json
import tkinter as tk
from tkinter import messagebox, ttk

BASE_DIR   = Path(__file__).resolve().parent
RECORDS    = BASE_DIR / "Records"
DATA_FILE  = RECORDS / "StudentMarks.json"
BACKUP     = BASE_DIR / "Records" / "StudentMarks_backup.json"

MAX_CW     = 60
MAX_EXAM   = 100
MAX_TOTAL  = MAX_CW + MAX_EXAM

BG_MAIN    = "#F1F5F9"
BG_CARD    = "#FFFFFF"
ACCENT     = "#2563EB"
ACCENT_H   = "#1D4ED8"
DANGER     = "#DC2626"
TEXT_DARK  = "#0F172A"
TEXT_MUTED = "#64748B"

def calculate_grade(percent):
    if percent >= 70: return "A"
    elif percent >= 60: return "B"
    elif percent >= 50: return "C"
    elif percent >= 40: return "D"
    else: return "F"

def get_grade_color(grade):
    if grade == "A": return "#16A34A"
    if grade == "B": return "#2563EB"
    if grade == "C": return "#D97706"
    if grade == "D": return "#EA580C"
    return DANGER

def create_record(code, name, cw1, cw2, cw3, exam):
    cw_total = cw1 + cw2 + cw3
    total = cw_total + exam
    percent = (total / MAX_TOTAL) * 100
    return {
        "code": code, "name": name,
        "cw1": cw1, "cw2": cw2, "cw3": cw3,
        "cw_total": cw_total, "exam": exam,
        "total": total, "percent": percent,
        "grade": calculate_grade(percent),
    }

students = []

def load_Stu():
    if not DATA_FILE.exists():
        raise FileNotFoundError("Could not find " + str(DATA_FILE))
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    for item in raw:
        cd = item["cw"] 
        students.append(create_record(
            item["id"], item["name"], cd[0], cd[1], cd[2], item["score"]
        ))
    return students

def student_save():
    if DATA_FILE.exists():
        shutil.copy2(DATA_FILE, BACKUP)
    raw = []
    for s in students:
        raw.append({
            "id": s["code"],
            "name": s["name"],
            "cw": [s["cw1"], s["cw2"], s["cw3"]],
            "score": s["exam"],
        })
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(raw, f, indent=2)


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.search_var = tk.StringVar()

        root.title("Student Dashboard")
        root.geometry("1050x600")
        root.configure(bg=BG_MAIN)

        self.load_data()

    def load_data(self):
        try:
            load_Stu()
            print("Loaded " + str(len(students)) + " students successfully.")
        except FileNotFoundError:
            print("Could not find the JSON file")


if __name__ == "__main__":
    root = tk.Tk()
    StudentApp(root)
    root.mainloop()