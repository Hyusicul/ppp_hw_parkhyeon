import random
import tkinter as tk

def gui_input():
    return entry.get()

def get_lotto():
    list = []
    while True:
        n = random.randint(1, 45)
        if n not in list:
            list.append(n)
        if len(list) == 6:
            break
    return sorted(list)

def generate_lotto():
    result_text.delete("1.0", tk.END)  
    try:
        count = int(gui_input())  
        for i in range(count):
            lotto_num = get_lotto()
            result_text.insert(tk.END, f"{i+1}번째: {lotto_num}\n")
    except ValueError:
        result_text.insert(tk.END, "숫자를 입력하세요.\n")


window = tk.Tk()
window.title("로또 번호 생성기")
window.geometry("400x400")

label = tk.Label(window, text="몇 개의 로또번호 세트를 뽑을까요?", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack()

generate_btn = tk.Button(window, text="로또 번호 생성", command=generate_lotto, font=("Arial", 14))
generate_btn.pack(pady=10)

result_text = tk.Text(window, height=15, font=("Arial", 12))
result_text.pack(pady=10)

window.mainloop()
