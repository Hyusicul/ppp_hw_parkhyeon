def main():
    t_c=int(input("섭씨 몇℃?"))
    f_t=int()
    def c2f(t_c):
        f_t=t_c*9/5+32
        print(f"섭씨{t_c}℃는 화씨{f_t}Ｆ입니다.")
    c2f(t_c)        #print가 함수안에 있으므로 print x 
        


if __name__=="__main__":
    main()