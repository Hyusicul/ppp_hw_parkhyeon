#calories=[26, 40, 297] #빨간 파프리카, 머스크멜론, 건포도
#red_paprika=int(input("빨간 파프리카를 얼만큼 드셨습니까? (100g단위)"))                            리스트 형식
#musk_melon=int(input("머스크 멜론을 얼만큼 드셨습니까? (100g단위)"))
#raisin=int(input("건포도를 얼만큼 드셨습니까? (100g단위)"))
#total_calories=calories[0]*(red_paprika/100)+calories[1]*(musk_melon/100)+calories[2]*(raisin/100)         
#print("당신은 총 {}kcal를 섭취하셨군요".format(total_calories))

calories={
    "빨간 파프리카": 26,
    "머스크 멜론": 40,
    "건포도": 297
}
red_paprika=int(input("빨간 파프리카를 얼만큼 드셨습니까? (100g단위)"))
musk_melon=int(input("머스크 멜론을 얼만큼 드셨습니까? (100g단위)"))                           #딕셔너리 형식
raisin=int(input("건포도를 얼만큼 드셨습니까? (100g단위)"))
total_calories=calories["빨간 파프리카"]*(red_paprika/100)+calories["머스크 멜론"]*(musk_melon/100)+calories["건포도"]*(raisin/100)
print("당신은 총 {}kcal를 섭취하셨군요".format(total_calories))