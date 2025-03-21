import math
a=int(input("사다리꼴 밑변의 길이는?"))
b=int(input("사다리꼴 윗변의 길이는?"))
h=int(input("사다리꼴 높이는?"))
trapezoide_area=((a+b)*h)/2
print("밑변이 {}이고 윗변이 {}, 높이가 {}인 사다리꼴의 넓이는 {}이다.".format(a, b, h, trapezoide_area))