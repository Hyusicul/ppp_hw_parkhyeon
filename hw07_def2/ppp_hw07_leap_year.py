def is_leap_year(y):
    if y%400==0:            #100으로도 나누어 떨이지지만 400으로 나누어 떨어지면 윤년 ex:2000년도
        print("y")
    elif y%100==0:          #100으로만 나누어 떨어지면 윤년X
        print("n")
    elif y%4==0:            #4로 나누어 떨어지면 윤년년
        print("y")
    else:
        print("n")
 
def main():
    y= int(input("연도를 쓰세요"))
    is_leap_year(y)


if __name__=="__main__":
    main()