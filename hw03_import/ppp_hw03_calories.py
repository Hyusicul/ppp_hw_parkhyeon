red_paprika=int(input("빨간 파프리카를 얼만큼 드셨습니까? (100g단위)"))
musk_melon=int(input("머스크 멜론을 얼만큼 드셨습니까? (100g단위)"))
raisin=int(input("건포도를 얼만큼 드셨습니까? (100g단위)"))

red_paprika_kcal=(red_paprika/100)*26
musk_melon_kcal=(musk_melon/100)*40
raisin_kcal=(raisin/100)*297

eat_kcal = red_paprika_kcal + musk_melon_kcal + raisin_kcal

print()                       #가시성
print()                       #가시성
print("빨간 파프리카의 100g당 칼로리=>26kcal, {}g을 드셨다면 {}kcal입니다.".format(red_paprika, red_paprika_kcal))
print("머스크 멜론의 100g당 칼로리=>40kcal, {}g을 드셨다면 {}kcal입니다.".format(musk_melon, musk_melon_kcal))
print("건포도의 100g당 칼로리=>297kcal, {}g을 드셨다면 {}kcal입니다.".format(raisin, raisin_kcal))
print()                       #가시성
print("따라서 당신은 총 {}kcal를 드셨습니다.".format(eat_kcal))
print()                       #가시성