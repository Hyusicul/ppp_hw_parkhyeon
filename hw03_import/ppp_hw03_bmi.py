import math
height=int(input("키는 몇입니까?(cm)"))
weight=int(input("몸무게는 몇입니까?(kg)"))
height_m=height/100
bmi=weight/math.pow(height/100,2)
print("키{}cm에 몸무게가 {}kg인 사람의 bmi는 {}입니다.".format(height, weight, bmi))