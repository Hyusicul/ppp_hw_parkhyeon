import random
import tkinter as tk

def new_problem():
    global dan, mul, problem_count
    if problem_count < total_problem:
        dan = random.randint(2, 9)
        mul = random.randint(1, 9)
        problem_label.config(text=f"{dan} x {mul} = ?")
    else:
        show_score()

def submit_answer():
    global score, problem_count
    try:
        ans = int(entry.get())
    except:
        result_label.config(text="숫자를 입력하세요!")
        return

    if ans == dan * mul:
        score += 1
        result_label.config(text="정답!")
    else:
        result_label.config(text=f"오답! 정답은 {dan * mul}")

    problem_count += 1
    entry.delete(0, tk.END)
    new_problem()

def show_score():
    problem_label.config(text="문제 끝!")
    result_label.config(text=f"총점: {score} / {total_problem} ({score/total_problem*100:.0f}점)")
    submit_btn.config(state="disabled")

score = 0
problem_count = 0
total_problem = 5
dan = 0
mul = 0

window = tk.Tk()
window.title("랜덤 구구단 게임")
window.geometry("400x300")

problem_label = tk.Label(window, text="", font=("Arial", 24))
problem_label.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 18))
entry.pack()

submit_btn = tk.Button(window, text="제출", command=submit_answer, font=("Arial", 14))
submit_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=20)


new_problem()

window.mainloop()