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

main_frame.pack(fill="both", expand=True)

current_punchline = ""

def start_joke():
    main_frame.pack_forget()
    jokes_frame.pack(fill="both", expand=True)

    next_joke()

def next_joke():
    global current_punchline

    if not jokes:
        return

    setup, current_punchline = random.choice(jokes)

    # Display the setup
    setup_label.config(text=setup)

    # Hide the previous punchline
    punchline_label.config(text="")

    # Reset the punchline button
    punchline_button.config(
        text="Show Punchline",
        state="normal"
    )

    def show_punchline():

    punchline_label.config(
        text=current_punchline
    )

    punchline_button.config(
        text="Punchline Revealed!",
        state="disabled"
    )

def quit_app():
    
    root.destroy()

root.mainloop
