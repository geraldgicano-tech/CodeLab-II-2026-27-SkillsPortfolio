from tkinter import *
import random

operations =  ["-", "+",]
quiz_questions = 10
attempts = 2
FRAME_BG = "#1E0E5A"
TEXT_BG = "#2A1770"
TEXT_FG = "#F2F0FF"
BUTTON_HOVER = "#4A399E"

def randomized_operation():
    return random.choice(operations)


def style_button(button):
    button.config(
        bg=TEXT_BG,
        fg=TEXT_FG,
        activebackground=BUTTON_HOVER,
        activeforeground=TEXT_FG,
        relief="raised",
        cursor="hand2",
    )
    button.bind("<Enter>", lambda event: button.config(bg=BUTTON_HOVER))
    button.bind("<Leave>", lambda event: button.config(bg=TEXT_BG))


def randint(difficulty):
    if difficulty == "Easy":
        minimum = 0
        maximum = 10
    elif difficulty in "Moderate":
        minimum = 10
        maximum = 100
    elif difficulty == "Hard":
        minimum = 1000
        maximum = 9999
    else:
        raise ValueError("Unknown difficulty")

    num1 = random.randint(minimum, maximum)
    num2 = random.randint(minimum, maximum)
    return num1, num2

def correct_answer(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2

def switch_frame(frame):
    global current_level, current_question_number, tries_remaining, score, quiz_advancing

    if frame == "home":
        main_frame.tkraise()
        return

    if frame == "easy":
        easy_frame.tkraise()
    elif frame == "moderate":
        moderate_frame.tkraise()
    elif frame == "hard":
        hard_frame.tkraise()
    elif frame == "results":
        results_frame.tkraise()
        return

    current_level = frame
    current_question_number = 1
    tries_remaining = attempts
    score = 0
    quiz_advancing = False
    random_question(frame)
    update_progress(frame)

def check_answer(num1, num2, operation, user_answer):
    correct = correct_answer(num1, num2, operation)
    return correct == user_answer

def submit_answer(current_level):
    global tries_remaining, score, quiz_advancing

    if quiz_advancing:
        return

    if current_level == "easy":
        answer_entry = easy_answer_user
    elif current_level == "moderate":
        answer_entry = moderate_answer_user
    else:
        answer_entry = hard_answer_user

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_labels[current_level].config(text="Solve the Question!")
        return

    num1, num2, operation = current_question
    if check_answer(num1, num2, operation, user_answer):
        score += 1
        feedback_labels[current_level].config(text="Correct!")
        answer_entry.delete(0, END)
        advance_question(current_level)
    elif tries_remaining > 1:
        tries_remaining -= 1
        feedback_labels[current_level].config(
            text=f"Oops thats wrong ({tries_remaining} more attempt left)."
        )
        attempts_labels[current_level].config(
            text=f"{tries_remaining} attempt left"
        )
        answer_entry.delete(0, END)
    else:
        answer = correct_answer(num1, num2, operation)
        feedback_labels[current_level].config(
            text=f"Ah so close The correct answer is {answer}."
        )
        answer_entry.delete(0, END)
        advance_question(current_level)


def advance_question(current_level):
    global quiz_advancing
    quiz_advancing = True
    root.after(700, lambda: next_question(current_level))


def next_question(current_level):
    global current_question_number, tries_remaining, quiz_advancing

    current_question_number += 1

    if current_question_number > quiz_questions:
        result_label.config(
            text=f"Quiz complete!\nYou scored {score} out of {quiz_questions}."
        )
        quiz_advancing = False
        results_frame.tkraise()
        return

    tries_remaining = attempts  
    quiz_advancing = False
    random_question(current_level)
    update_progress(current_level)


def update_progress(current_level):
    progress_labels[current_level].config(
        text=f"Question {current_question_number} of {quiz_questions}"
    )
    attempts_labels[current_level].config(
        text=f"{tries_remaining} attempt{'s' if tries_remaining != 1 else ''} left"
    )

def random_question(current_level):
    global current_question

    if current_level == "easy":
        num1, num2 = randint("Easy")
        operation = randomized_operation()
        easy_label_question.config(text=f"Solve {num1} {operation} {num2}?")
        current_question = (num1, num2, operation)
    elif current_level == "moderate":
        num1, num2 = randint("Moderate")
        operation = randomized_operation()
        moderate_label_question.config(text=f"Solve {num1} {operation} {num2}?")
        current_question = (num1, num2, operation)
    elif current_level == "hard":
        num1, num2 = randint("Hard")
        operation = randomized_operation()
        hard_label_question.config(text=f"Solve {num1} {operation} {num2}?")
        current_question = (num1, num2, operation)

    feedback_labels[current_level].config(text="")





root = Tk()
root.title("Maths Quiz")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg=FRAME_BG)

main_frame = Frame(root, bg=FRAME_BG)
main_frame.place(x=0, y=0, relwidth=1, relheight=1)

easy_frame = Frame(root, bg=FRAME_BG)
easy_frame.place(x=0, y=0, relwidth=1, relheight=1)

easy_label = Label(easy_frame, text="Easy Level", font=("Arial", 18), bg=TEXT_BG, fg=TEXT_FG)
easy_label.pack(pady=20)


easy_label_question = Label(easy_frame, text="", font=("Arial", 16), bg=TEXT_BG, fg=TEXT_FG)
easy_label_question.pack(pady=10)

easy_label_progress = Label(easy_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
easy_label_progress.pack()

easy_label_attempts = Label(easy_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
easy_label_attempts.pack(pady=2)

easy_label_feedback = Label(easy_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
easy_label_feedback.pack(pady=5)

easy_answer_user = Entry(easy_frame, font=("Arial", 14), width=20, bg=TEXT_BG, fg=TEXT_FG, insertbackground=TEXT_FG)
easy_answer_user.pack(pady=10)

moderate_frame = Frame(root, bg=FRAME_BG)
moderate_frame.place(x=0, y=0, relwidth=1, relheight=1)

submit = Button(easy_frame, text="Submit", font=("Arial", 12), width=12, command=lambda: submit_answer("easy"))
style_button(submit)
submit.pack(pady=2)

moderate_label = Label(moderate_frame, text="Moderate Level", font=("Arial", 18), bg=TEXT_BG, fg=TEXT_FG)
moderate_label.pack(pady=20)

moderate_label_question = Label(moderate_frame, text="", font=("Arial", 16), bg=TEXT_BG, fg=TEXT_FG)
moderate_label_question.pack(pady=10)

moderate_label_progress = Label(moderate_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
moderate_label_progress.pack()

moderate_label_attempts = Label(moderate_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
moderate_label_attempts.pack(pady=2)

moderate_label_feedback = Label(moderate_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
moderate_label_feedback.pack(pady=5)

moderate_answer_user = Entry(moderate_frame, font=("Arial", 14), width=20, bg=TEXT_BG, fg=TEXT_FG, insertbackground=TEXT_FG)
moderate_answer_user.pack(pady=10)

submit_moderate = Button(moderate_frame, text="Submit", font=("Arial", 12), width=12, command=lambda: submit_answer("moderate"))
style_button(submit_moderate)
submit_moderate.pack(pady=2)

hard_frame = Frame(root, bg=FRAME_BG)
hard_frame.place(x=0, y=0, relwidth=1, relheight=1)

hard_label = Label(hard_frame, text="Hard Level", font=("Arial", 18), bg=TEXT_BG, fg=TEXT_FG)
hard_label.pack(pady=20)

hard_label_question = Label(hard_frame, text="", font=("Arial", 16), bg=TEXT_BG, fg=TEXT_FG)
hard_label_question.pack(pady=10)

hard_label_progress = Label(hard_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
hard_label_progress.pack()

hard_label_attempts = Label(hard_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
hard_label_attempts.pack(pady=2)

hard_label_feedback = Label(hard_frame, text="", font=("Arial", 12), bg=TEXT_BG, fg=TEXT_FG)
hard_label_feedback.pack(pady=5)

hard_answer_user = Entry(hard_frame, font=("Arial", 14), width=20, bg=TEXT_BG, fg=TEXT_FG, insertbackground=TEXT_FG)
hard_answer_user.pack(pady=10)

submit_hard = Button(hard_frame, text="Submit", font=("Arial", 12), width=12, command=lambda: submit_answer("hard"))
style_button(submit_hard)
submit_hard.pack(pady=2)

results_frame = Frame(root, bg=FRAME_BG)
results_frame.place(x=0, y=0, relwidth=1, relheight=1)

result_label = Label(results_frame, text="", font=("Arial", 16), bg=TEXT_BG, fg=TEXT_FG)
result_label.pack(pady=(100, 20))

menu_button = Button(results_frame, text="Back to Menu", font=("Arial", 12), width=14, command=lambda: switch_frame("home"))
style_button(menu_button)
menu_button.pack(pady=10)

title_label = Label(main_frame, text="Serious Math Quiz!", font=("Arial", 18), bg=TEXT_BG, fg=TEXT_FG)
title_label.pack(pady=(50, 10))

label2 = Label(main_frame, text="Choose your level, wisely", font=("Arial", 14), bg=TEXT_BG, fg=TEXT_FG)
label2.pack(pady=10)

question_label = Label(main_frame, text="", font=("Arial", 16), bg=TEXT_BG, fg=TEXT_FG)
question_label.pack(pady=10)

button_frame = Frame(main_frame, bg=FRAME_BG)
button_frame.pack(pady=10)

button1 = Button(button_frame, text="Easy", font=("Arial", 12), width=14, command=lambda: switch_frame("easy"))
style_button(button1)
button1.pack(pady=5)

button2 = Button(button_frame, text="Moderate", font=("Arial", 12), width=14, command=lambda: switch_frame("moderate"))
style_button(button2)
button2.pack(pady=5)

button3 = Button(button_frame, text="Hard", font=("Arial", 12), width=14, command=lambda: switch_frame("hard"))
style_button(button3)
button3.pack(pady=5)

progress_labels = {
    "easy": easy_label_progress,
    "moderate": moderate_label_progress,
    "hard": hard_label_progress,
}

attempts_labels = {
    "easy": easy_label_attempts,
    "moderate": moderate_label_attempts,
    "hard": hard_label_attempts,
}

feedback_labels = {
    "easy": easy_label_feedback,
    "moderate": moderate_label_feedback,
    "hard": hard_label_feedback,
}

main_frame.tkraise()

root.mainloop()
