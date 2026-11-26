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
        self.build_left_panel()
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

    def load_data(self):
        try:
            load_Stu()
            self.refresh_tree()
        except FileNotFoundError:
            print("Could not find the JSON file")

    def refresh_tree(self, show_list=None):
        for i in self.tree.get_children():
            self.tree.delete(i)
        source = show_list if show_list else students
        for s in source:
            self.tree.insert("", "end", iid=str(s["code"]), text=" " + s['name'] + " (" + str(s['code']) + ")")

    def filter_list(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    StudentApp(root)
    root.mainloop()