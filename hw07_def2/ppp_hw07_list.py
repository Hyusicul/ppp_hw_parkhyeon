def get_range_list(n):
    a=[]
    for i in range(n+1):
        a.append(i)
    del a[0]
    return a


def main():
    n=int(input("1부터 몇까지의 숫자를 리스트로 반환하겠습니까?"))
    print(get_range_list(n))
if __name__=="__main__":
    main()