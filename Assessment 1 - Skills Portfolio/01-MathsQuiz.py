from tkinter import *
import random

operations = ["+", "-", "*",]

def random_operation():
    return random.choice(operations)


def randint(difficulty):
    if difficulty == "Easy":
        min_value = 10
        max_value = 100
    elif difficulty == "Medium":
        min_value = 100
        max_value = 1000
    elif difficulty == "Hard":
        min_value = 1000
        max_value = 10000
    else:
        raise ValueError("Unknown difficulty")

    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    return num1, num2

def correct_answer(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2

def switch_frame(frame):
    if frame == "easy":
        frameeasy.tkraise()
        random_question("easy")
    elif frame == "medium":
        framemedium.tkraise()
        random_question("medium")
    elif frame == "hard":
        framehard.tkraise()
        random_question("hard")
    elif frame == "results":
        frameresults.tkraise()

def check_answer(num1, num2, operation, user_answer):
    correct = correct_answer(num1, num2, operation)
    return correct == user_answer

def submit_answer(current_level):
    global current_question

    if current_level == "easy":
        answer_entry = user_answer_easy
    elif current_level == "medium":
        answer_entry = user_answer_medium
    else:
        answer_entry = user_answer_hard

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        result_label.config(text="Please enter a number.")
        frameresults.tkraise()
        return

    num1, num2, operation = current_question
    if check_answer(num1, num2, operation, user_answer):
        result_label.config(text="Correct!")
    else:
        result_label.config(text=f"Incorrect. The answer is {correct_answer(num1, num2, operation)}.")

    frameresults.tkraise()

def random_question(current_level):
    global current_question

    if current_level == "easy":
        num1, num2 = randint("Easy")
        operation = random_operation()
        question_label_easy.config(text=f"What is {num1} {operation} {num2}?")
        current_question = (num1, num2, operation)
    elif current_level == "medium":
        num1, num2 = randint("Medium")
        operation = random_operation()
        question_label_medium.config(text=f"What is {num1} {operation} {num2}?")
        current_question = (num1, num2, operation)
    elif current_level == "hard":
        num1, num2 = randint("Hard")
        operation = random_operation()
        question_label_hard.config(text=f"What is {num1} {operation} {num2}?")
        current_question = (num1, num2, operation)





root = Tk()
root.title("Maths Quiz")

mainframe = Frame(root, bg="#FFFFFF")
mainframe.place(x=0, y=0, width=400, height=400)

frameeasy = Frame(root, bg="#FFFFFF")
frameeasy.place(x=0, y=0, width=400, height=400)

label_easy = Label(frameeasy, text="Easy Level", font=("Helvetica", 16))
label_easy.pack(pady=10)


question_label_easy = Label(frameeasy, text="", font=("Helvetica", 14))
question_label_easy.pack(pady=10)

user_answer_easy = Entry(frameeasy)
user_answer_easy.pack(pady=10)

framemedium = Frame(root, bg="#FFFFFF")
framemedium.place(x=0, y=0, width=400, height=400)

submit = Button(frameeasy, text="Submit", command=lambda: submit_answer("easy"))
submit.pack(pady= 2)

label_medium = Label(framemedium, text="Medium Level", font=("Helvetica", 16))
label_medium.pack(pady=10)

question_label_medium = Label(framemedium, text="", font=("Helvetica", 14))
question_label_medium.pack(pady=10)

user_answer_medium = Entry(framemedium)
user_answer_medium.pack(pady=10)

submit_medium = Button(framemedium, text="Submit", command=lambda: submit_answer("medium"))
submit_medium.pack(pady=2)

framehard = Frame(root, bg="#FFFFFF")
framehard.place(x=0, y=0, width=400, height=400)

label_hard = Label(framehard, text="Hard Level", font=("Helvetica", 16))
label_hard.pack(pady=10)

question_label_hard = Label(framehard, text="", font=("Helvetica", 14))
question_label_hard.pack(pady=10)

user_answer_hard = Entry(framehard)
user_answer_hard.pack(pady=10)

submit_hard = Button(framehard, text="Submit", command=lambda: submit_answer("hard"))
submit_hard.pack(pady=2)

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
