from ppp_hw07_average import average


        
def main():

    text_input= input("숫자를 적으시오(ex: 1,2,3)")
    nums=[int(x) for x in text_input.split(",")]

    print(f"숫자의 평균값은 {average(nums)}입니다.")

if __name__=="__main__":
    main()