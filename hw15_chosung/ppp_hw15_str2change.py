def toggle_text(text: str):
    list=[]
    str_list=[]
    for ch in text:
        list.append(ch)
    for ch2 in list:
        if ord(ch2)>=92 and ord(ch2)<=122:
            str_list.append(chr(ord(ch2)-32))
        elif ord(ch2)>=65 and ord(ch2)<=90:
            str_list.append(chr(ord(ch2)+32))
        else:
            print("영어만 써주세요!!!")
            break
    return"".join(str_list)

def main():
    user_input=input("영어를 입력하시오")
    change_str=toggle_text(user_input)
    print(change_str)

if __name__=="__main__":
    main()

