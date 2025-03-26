a=int(input("빨간 파프리카를 얼만큼 드셨습니까?"))
b=int(input("머스크 멜론을 얼만큼 드셨습니까?"))
c=int(input("건포도를 얼만큼 드셨습니까?"))
calories={                                              #과일 100g당 칼로리
    "빨간 파프리카": 26/100,
    "머스크 멜론": 40/100,
    "건포도": 297/100
}
eat_fru={                                               #먹은 과일의 양(g)
    "빨간 파프리카": a,
    "머스크 멜론": b,
    "건포도": c
}
fru_list=["빨간 파프리카","머스크 멜론","건포도"]
total=0
for item in fru_list:
    total+=calories[item]*eat_fru[item]
print(f"섭취하신 총 칼로리는 {total}kcal입니다.")