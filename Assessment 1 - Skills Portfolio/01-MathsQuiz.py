from tkinter import *
import random

operations = ["+", "-", "*",]

def random_operation():
    return random.choice(operations)



def difficulty(level):
    if level == "Easy":
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)
        return num1, num2
    elif level == "Medium":
        num1 = random.randint(100, 1000)
        num2 = random.randint(100, 1000)
        return num1, num2
    elif level == "Hard":
        num1 = random.randint(1000, 10000)
        num2 = random.randint(1000, 10000)
        return num1, num2

def random_question(current_level):
    if current_level == "easy":
        num1, num2 = difficulty("Easy")
        operation = random_operation()
        question_label.config(text=f"What is {num1} {operation} {num2}?")
        return num1, num2
    elif current_level == "medium":
        num1, num2 = difficulty("Medium")
        operation = random_operation()
        question_label.config(text=f"What is {num1} {operation} {num2}?")
        return num1, num2
    elif current_level == "hard":
        num1, num2 = difficulty("Hard")
        operation = random_operation()
        question_label.config(text=f"What is {num1} {operation} {num2}?")
        return num1, num2

def switch_frame(frame):
    if frame == "easy":
        frameeasy.tkraise()
    elif frame == "medium":
        framemedium.tkraise()
    elif frame == "hard":
        framehard.tkraise()
    elif frame == "results":
        frameresults.tkraise()

def check_answer(level):
    user_answer = user_answer_easy.get()
    num1, num2 = difficulty(level)
    correct_answer = num1 + num2
    if user_answer == str(correct_answer):
        result_label.config(text="Correct!")
    else:
        result_label.config(text=f"Incorrect! The correct answer is {correct_answer}.")
    switch_frame("results")



root = Tk()
root.title("Maths Quiz")

mainframe = Frame(root, bg="#FFFFFF")
mainframe.place(x=0, y=0, width=400, height=400)

frameeasy = Frame(root, bg="#FFFFFF")
frameeasy.place(x=0, y=0, width=400, height=400)

label_easy = Label(frameeasy, text="Easy Level", font=("Helvetica", 16))
label_easy.pack(pady=10)

question_label_easy = Label(frameeasy, text="Solve", font=("Helvetica", 14))
question_label_easy.pack(pady=10)

user_answer_easy = Entry(frameeasy)
user_answer_easy.pack(pady=10)

framemedium = Frame(root, bg="#FFFFFF")
framemedium.place(x=0, y=0, width=400, height=400)

label_medium = Label(framemedium, text="Medium Level", font=("Helvetica", 16))
label_medium.pack(pady=10)

user_answer_medium = Entry(framemedium)
user_answer_medium.pack(pady=10)

framehard = Frame(root, bg="#FFFFFF")
framehard.place(x=0, y=0, width=400, height=400)

frameresults = Frame(root, bg="#FFFFFF")
frameresults.place(x=0, y=0, width=400, height=400)

result_label = Label(frameresults, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

title_label = Label(root, text="Welcome to the Maths Quiz!", font=("Helvetica", 16))
title_label.pack(pady=10)

label2 = Label(root, text="Select a difficulty level to start the quiz.", font=("Helvetica", 12))
label2.pack(pady=10)

question_label = Label(root, text="", font=("Helvetica", 14))
question_label.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

button1 = Button(button_frame, text="Easy", command=lambda: switch_frame("easy"))
button1.pack(pady=5)

button2 = Button(button_frame, text="Medium", command=lambda: switch_frame("medium"))
button2.pack(pady=5)

button3 = Button(button_frame, text="Hard", command=lambda: switch_frame("hard"))
button3.pack(pady=5)

root.geometry("400x300")

root.mainloop()
