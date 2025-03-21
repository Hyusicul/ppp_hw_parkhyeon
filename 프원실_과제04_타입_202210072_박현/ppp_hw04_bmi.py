import math
bm=""
height=int(input("키는 몇입니까?(cm)"))
weight=int(input("몸무게는 몇입니까?(kg)"))
height_m=height/100
bmi=weight/math.pow(height/100,2)
if bmi<23:
    bm="정상체중"
elif bmi>=23 and bmi<24.9:
    bm="비만 전단계"
elif bmi>=25 and bmi<29.9:
    bm="1단계 비만"
elif bmi>=30 and bmi<34.9:
    bm="2단계 비만"
elif bmi>=35:
    bm="3단계 비만"
print("키{}cm에 몸무게가 {}kg인 사람의 bmi는 {}이고, {}입니다.".format(height, weight, bmi,bm))