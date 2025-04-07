def main():
    dan=int(input("구구단 몇 단?"))
    def gugudan(dan):
        for i in range(9):
            i+=1                   
            print(f"{dan}*{i}={dan*i}")
    gugudan(dan)        #print가 함수안에 있으므로 print x 

if __name__=="__main__":
    main()