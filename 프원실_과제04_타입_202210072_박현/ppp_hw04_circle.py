import math
r=int(input("원의 반지름의 길이는?"))
circumference=r*2*math.pi
circle_area=pow(r,2)*math.pi
print("="*30)
print("원의 둘레는{:.1f}".format(circumference))
print("원의 넓이는{:.2f}".format(circle_area))
print("="*30)