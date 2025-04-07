def main():
    n=int(input("1부터 몇까지의 합을 구하시겠습니까?"))
    def sum_n(n):
        a=(n*(n+1))/2
        return(a)



    print(f"1부터 {n}까지의 합은 {sum_n(n):.0f}입니다.")




if __name__=="__main__":
    main()