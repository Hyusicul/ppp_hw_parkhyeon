import math
x_1=int(input("x1의 좌표는?"))
y_1=int(input("y1의 좌표는?"))
x_2=int(input("x2의 좌표는?"))
y_2=int(input("y2의 좌표는?"))

x_distance=abs(x_1-x_2)
y_distance=abs(y_1-y_2)

x_distance_pow=math.pow(x_distance,2)
y_distance_pow=math.pow(y_distance,2)
distance_pow=x_distance_pow+y_distance_pow

distance=math.sqrt(distance_pow)
print("({},{})와 ({},{})의 두 좌표 사이의 거리는 {}입니다.".format(x_1, y_1, x_2, y_2, distance))
print(f"두 점 사이의 거리는 {distance:.3f}입니다.")         #소수점 제한한     



# distance = math.sqrt((x_2-x_1)**2+(y_2-y_1)**2)         교수님 풀이
# print(distance)