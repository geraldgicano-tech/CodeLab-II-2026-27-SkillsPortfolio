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
try:
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
except FileNotFoundError:
    messagebox.showerror(
        "File Not Found",
        "Could not find randomJokes.txt.\nCheck that it is inside the jokes folder."
    )
    raise SystemExit

root = Tk()
root.title("jokoy")
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
    if not jokes:
        messagebox.showerror("No Jokes Found", "Add some valid jokes to randomJokes.txt.")
        return

    main_frame.pack_forget()
    jokes_frame.pack(fill="both", expand=True)
    next_joke()


def next_joke():
    global current_punchline
    if not jokes:
        return

    setup, current_punchline = random.choice(jokes)
    setup_label.config(text=setup)
    punchline_label.config(text="")
    punchline_button.config(
        text="Show Punchline",
        state="normal"
    )


def show_punchline():
    punchline_label.config(text=current_punchline)
    punchline_button.config(text="HAHAHAH! funny right?", state="disabled")


def quit_app():
    root.destroy()


alexa_button = Button(
    main_frame,
    text="Alexa, tell me a joke",
    font=("Arial", 18, "bold"),
    bg=PINK,
    fg=WHITE,
    activebackground=PINK,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=18,
    command=start_joke
)
alexa_button.place(relx=0.5, rely=0.5, anchor="center")

title = Label(
    jokes_frame,
    text="jokoy",
    font=("Arial", 24, "bold"),
    bg=BACKGROUND,
    fg=PINK
)
title.pack(pady=(25, 5))

subtitles = Label(
    jokes_frame,
    text="joke so bad that its funny",
    font=("Arial", 12, "italic"),
    bg=BACKGROUND,
    fg=BROWN
)
subtitles.pack(pady=(0, 20))

setup_label = Label(
    jokes_frame,
    text="",
    font=("Arial", 20, "bold"),
    bg=WHITE,
    fg=DARK,
    wraplength=520,
    justify="center",
    padx=20,
    pady=25,
    width=40,
    height=3
)
setup_label.pack(pady=10, padx=30)

punchline_label = Label(
    jokes_frame,
    text="",
    font=("Arial", 16, "italic"),
    bg=BACKGROUND,
    fg=GREEN,
    wraplength=520,
    justify="center"
)
punchline_label.pack(pady=15)

button_frame = Frame(jokes_frame, bg=BACKGROUND)
button_frame.pack(pady=15)

punchline_button = Button(
    button_frame,
    text="Show Punchline",
    font=("Arial", 12, "bold"),
    bg=PINK,
    fg=WHITE,
    activebackground=PINK,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=10,
    command=show_punchline
)
punchline_button.grid(row=0, column=0, padx=10)

next_button = Button(
    button_frame,
    text="Next Joke",
    font=("Arial", 12, "bold"),
    bg=GREEN,
    fg=WHITE,
    activebackground=GREEN,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=10,
    command=next_joke
)
next_button.grid(row=0, column=1, padx=10)

quit_button = Button(
    jokes_frame,
    text="Had enough?",
    font=("Arial", 11, "bold"),
    bg=BROWN,
    fg=WHITE,
    activebackground=BROWN,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=8,
    command=quit_app
)
quit_button.pack(pady=5)

root.mainloop()