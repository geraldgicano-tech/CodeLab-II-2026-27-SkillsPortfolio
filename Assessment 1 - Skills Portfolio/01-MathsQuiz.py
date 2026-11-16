from tkinter import *
import random

def difficulty(level):
    if level == "Easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == "Medium":
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)
    elif level == "Hard":
        num1 = random.randint(100, 1000)
        num2 = random.randint(100, 1000)
    return num1, num2

def random_question():
    level = random.choice(["Easy", "Medium", "Hard"])
    num1, num2 = difficulty(level)
    question_label.config(text=f"What is {num1} + {num2}?")


root = Tk()
root.title("Maths Quiz")

mainframe = Frame(root, bg="#FFFFFF")
mainframe.place(x=0, y=0, width=400, height=400)

frameeasy = Frame(root, bg="#FFFFFF")
frameeasy.place(x=0, y=0, width=400, height=400)

framemedium = Frame(root, bg="#FFFFFF")
framemedium.place(x=0, y=0, width=400, height=400)

framehard = Frame(root, bg="#FFFFFF")
framehard.place(x=0, y=0, width=400, height=400)

frameresults = Frame(root, bg="#FFFFFF")
frameresults.place(x=0, y=0, width=400, height=400)

title_label = Label(root, text="Welcome to the Maths Quiz!", font=("Helvetica", 16))
title_label.pack(pady=10)

question_label = Label(root, text="", font=("Helvetica", 14))
question_label.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

button1 = Button(button_frame, text="Easy", command=random_question)
button1.pack(pady=5)

button2 = Button(button_frame, text="Medium", command=random_question)
button2.pack(pady=5)

button3 = Button(button_frame, text="Hard", command=random_question)
button3.pack(pady=5)

root.geometry("400x300")

root.mainloop()
