from tkinter import *
import random
from tkinter import messagebox
from pathlib import Path

file_path = (
Path(__file__).resolve().parent
/ "jokes"
/ "randomJokes.txt"
)



root = Tk()
root.title('jokoy')
root.geometry("650x500")
root.resizable(False, False)

BACKGROUND = "#FFE7A7"
PINK = "#FD9FF1"
GREEN = "#41946F"
DARK = "#000000"
WHITE = "#FFFFFF"
BROWN = "#966A4C"

root.configure(bg=BACKGROUND)

main_frame = Frame(root, bg=BACKGROUND)
jokes_frame = Frame(root, bg=BACKGROUND)



root.mainloop
