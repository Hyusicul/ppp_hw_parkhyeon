import math
x=int(input("x좌표는?"))
y=int(input("y좌표는?"))
if x>0 and y>0:
    print("입력한 좌표({},{})는 1사분면 입니다.".format(x,y))
elif x>0 and y<0:
    print("입력한 좌표({},{})는 4사분면 입니다.".format(x,y))        
elif x<0 and y>0:
    print("입력한 좌표({},{})는 2사분면 입니다.".format(x,y))   
elif x<0 and y<0:
    print("입력한 좌표({},{})는 3사분면 입니다.".format(x,y))
elif x==0 and y!=0:
    print("입력한 좌표({},{})는 y축 위에 위치합니다.".format(x,y))
elif x!=0 and y==0:
    print("입력한 좌표({},{})는 x축 위에 위치합니다.".format(x,y))    
else:
    print("입력한 좌표({},{})는 원점에 위치합니다.".format(x,y)) 