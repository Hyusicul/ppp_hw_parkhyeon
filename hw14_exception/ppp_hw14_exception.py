def number():
    numbers_list=[]
    while True:
        input_n=input("자연수를 입력하시오")    
        try:
            num = int(input_n)

            if num == -1:
                break
            elif num > 0:
                numbers_list.append(num)
            else:
                print("!!!!!!!!!자연수가 아닙니다!!!!!!!!!")

        except ValueError:
            print("!!!!!!!!!정수가 아닙니다!!!!!!!!!")
            
    return numbers_list    

def main():
    numbers=number()
    
    a=0
    for i in numbers:
        a=a+i
    ave_num=a/len(numbers)
    
    l_num=len(numbers)

    print(numbers)
    print(f"평균은:{ave_num:.2f}")
    print(f"총 개수는:{l_num}")


if __name__=="__main__":
    main()