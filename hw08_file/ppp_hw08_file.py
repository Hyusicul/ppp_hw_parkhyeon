def read_nb(filename):
    numbers_2=[]
    with open(filename, encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            numbers_2.append(int(line))
    return numbers_2


def main():
    numbers=read_nb("./hw08_numbers.txt")
    numbers.sort()
    n_len=len(numbers)
    n_average=sum(numbers)/len(numbers)
    n_max=max(numbers)
    n_min=min(numbers)
    n_median=len(numbers)
    if n_median%2==1:           #길이가 홀수
        n_m=n_median/2
    else:                       #길이가 짝수
        n_m=((n_median//2-1)+(n_median//2))/2
        
    print(f"총 숫자의 개수는 {n_len}개입니다.")
    print(f"숫자의 평균은 {n_average}입니다.")
    print(f"숫자의 최댓값은 {n_max}입니다.")
    print(f"숫자의 최솟값은 {n_min}입니다.")
    print(f"숫자의 중앙값은 {n_m}입니다.")
if __name__=="__main__":
    main()