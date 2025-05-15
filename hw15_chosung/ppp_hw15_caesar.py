def caesar_encode_ch(ch, shift):
    return chr(ord(ch)+shift)

def caesar_encode(text: str, shift:int = 3, shift2:int=-23):
    list=[]
    caesar_list=[]
    for ch in text:
        list.append(ch)
    for ch2 in list:
        if ord(ch2)>=97 and ord(ch2)<=119 or ord(ch2)>=65 and ord(ch2)<=87:
            encoded_ch=chr(ord(ch2)+shift)
            caesar_list.append(encoded_ch)
        elif ord(ch2)>=120 and ord(ch2)<=122 or ord(ch2)>=88 and ord(ch2)<=90:
            encoded_ch=chr(ord(ch2)+shift2)
            caesar_list.append(encoded_ch)   
        else:
            print("영어를 입력하시오!!!!")         
            break
    return"".join(caesar_list)
def main():
    input_caesar=input("영어를 입력하시오.")
    caesar=caesar_encode(input_caesar)
    print(f"암호:{caesar}")
if __name__=="__main__":
    main()