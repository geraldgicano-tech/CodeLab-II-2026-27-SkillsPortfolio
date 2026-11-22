from tkinter import *
import random
from tkinter import messagebox
from pathlib import Path

jokes_file = (
    Path(__file__).resolve().parent
    / "jokes"
    / "randomJokes.txt"
)

jokes = []
with jokes_file.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        line = line.removeprefix("-").strip()
        if "?" in line:
            joke, punchline = line.split("?", 1)
            joke = joke.strip() + "?"
            punchline = punchline.strip()
            if joke and punchline:
                jokes.append((joke, punchline))





        


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
