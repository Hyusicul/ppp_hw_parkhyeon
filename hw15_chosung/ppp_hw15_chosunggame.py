import random
chosung_list="ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
def to_chosung_ch(ch):
    chosung_number=(ord(ch)-ord('가'))//588
    chosung=chosung_list[chosung_number]
    return chosung

def to_chosung(text):
    full_text = []
    for ch in text:
        full_text.append(to_chosung_ch(ch))
    return full_text
    
def main():
    problems=["바나나", "딸기", "토마토", "복숭아"]
    solution=problems[random.randrange(len(problems))]
    is_correct= False
   
    for _ in range(3):
        answer = input(f"{to_chosung(solution)}? => ")
        if answer == solution:
            print("정답입니다.")
            is_correct =True
            break
        else:
            print("오답입니다.")

    if is_correct:
        print("잘하셨습니다.")
    else:
        print("다시 해보세요.")
if __name__=="__main__":
    main()