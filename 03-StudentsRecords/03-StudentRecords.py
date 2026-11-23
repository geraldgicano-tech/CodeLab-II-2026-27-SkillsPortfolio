from pathlib import Path
import json
import tkinter as tk
from tkinter import messagebox, ttk

DATA_FILE = Path(__file__).resolve().parent / "Records" / "StudentMarks.json"
FULL_COURSEWORK = 60
FULL_EXAM = 100
MAX_MARKS = FULL_COURSEWORK + FULL_EXAM

root = Tk()
root.title("Student Marks Manager")
root.geometry("920x600")
root.minsize(780, 500)

sidebar = tk.Frame(root, width=250)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)