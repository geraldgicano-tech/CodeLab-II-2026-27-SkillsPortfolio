from pathlib import Path
import shutil
import json
import tkinter as tk
from tkinter import messagebox, ttk

BASE_DIR   = Path(__file__).resolve().parent
RECORDS    = BASE_DIR / "Records"
DATA_FILE  = RECORDS / "StudentMarks.json"
BACKUP_DIR = RECORDS / "Backups"
BACKUP     = BASE_DIR / "Records" / "StudentMarks_backup.json"


MAX_CW     = 60
MAX_EXAM   = 100
MAX_TOTAL  = MAX_CW + MAX_EXAM

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
            item["id"], item["name"], cw[0], cw[1], cw[2], item["score"]
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
    with open(DATA_FILE, "w", encoding="utf=8") as f:
        json.dump(raw, f, indet=2)

BG_MAIN    = "#F1F5F9"
BG_CARD    = "#FFFFFF"
ACCENT     = "#2563EB"
ACCENT_H   = "#1D4ED8"
DANGER     = "#DC2626"
TEXT_DARK  = "#0F172A"
TEXT_MUTED = "#64748B"

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.students = []
        self.search_var = tk.StringVar()
        self.selected_student = None

        root.title("Student Dashboard")
        root.geometry("1050x600")
        root.configure(bg=BG_MAIN)

        self.build_left_panel()
        self.build_middle_panel()
        self.build_right_panel()
        self.load_data()

def build_left_panel(self):
        left = tk.Frame(self.root, bg=BG_CARD, width=280)
        left.pack(side="left", fill="y", padx=10, pady=10)
        left.pack_propagate(False)

        tk.Label(left, text="Students", font=("Segoe UI", 14, "bold"), bg=BG_CARD, fg=TEXT_DARK).pack(anchor="w", padx=10, pady=(10, 5))

        s_row = tk.Frame(left, bg=BG_CARD)
        s_row.pack(fill="x", padx=10, pady=5)
        tk.Entry(s_row, textvariable=self.search_var, width=20).pack(side="left", fill="x", expand=True)
        tk.Button(s_row, text="Find", command=self.filter_list, bg=ACCENT, fg="white").pack(side="left", padx=(4,0))

        self.tree = ttk.Treeview(left, columns=("name",), show="tree", height=20)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        tk.Button(left, text="View All / Stats", command=self.show_all, bg="#E2E8F0").pack(fill="x", padx=10, pady=(0, 10))

def build_middle_panel(self):
        mid = tk.Frame(self.root, bg=BG_CARD, width=400)
        mid.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        mid.pack_propagate(False)

        tk.Label(mid, text="Profile", font=("Segoe UI", 14, "bold"), bg=BG_CARD, fg=TEXT_DARK).pack(anchor="w", padx=15, pady=(10, 10))

        self.empty_lbl = tk.Label(mid, text="Select a student...", font=("Segoe UI", 11), bg=BG_CARD, fg=TEXT_MUTED)
        self.empty_lbl.pack(expand=True)

        self.prof = tk.Frame(mid, bg="#F8FAFC", padx=20, pady=20)
        
        self.name_lbl = tk.Label(self.prof, text="", font=("Segoe UI", 18, "bold"), bg="#F8FAFC", anchor="w")
        self.id_lbl = tk.Label(self.prof, text="", font=("Segoe UI", 10), bg="#F8FAFC", fg=TEXT_MUTED, anchor="w")
        self.grade_lbl = tk.Label(self.prof, text="", font=("Segoe UI", 24, "bold"), bg="#F8FAFC", anchor="w")
        
        tk.Frame(self.prof, height=2, bg="#E2E8F0").pack(fill="x", pady=15)
        
        self.cw_lbl = tk.Label(self.prof, text="", font=("Segoe UI", 12), bg="#F8FAFC", anchor="w")
        self.exam_lbl = tk.Label(self.prof, text="", font=("Segoe UI", 12), bg="#F8FAFC", anchor="w")
        self.total_lbl = tk.Label(self.prof, text="", font=("Segoe UI", 14, "bold"), bg="#F8FAFC", anchor="w")
        self.pct_lbl = tk.Label(self.prof, text="", font=("Segoe UI", 14, "bold"), bg="#F8FAFC", anchor="w")

        self.name_lbl.pack(fill="x")
        self.id_lbl.pack(fill="x")
        self.grade_lbl.pack(fill="x")
        self.cw_lbl.pack(fill="x", pady=2)
        self.exam_lbl.pack(fill="x", pady=2)
        self.total_lbl.pack(fill="x", pady=(10, 2))
        self.pct_lbl.pack(fill="x")


root = tk.Tk()
root.title("Student Marks Manager")
root.geometry("920x600")
root.minsize(780, 500)



sidebar = tk.Frame(root, width=250)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

root.mainloop()
