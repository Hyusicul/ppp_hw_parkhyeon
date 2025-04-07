def  total_calorie(fruits,fruits_calorie_dic):
    fru={}
    fru_list=fruits.split(",")
    for fru_list_2 in fru_list:
        fruit,amount=fru_list_2.split(":")
        fru[fruit.strip()] = int(amount.strip())
    total=0
    for fruit in fru:
        total+= fru[fruit]*fruits_calorie_dic[fruit]
    return(total)
    
def main():
    fruits=input("딸기와 한라봉을 얼만큼 드셨나요? (ex: 딸기:100, 한라봉:150)")
    
    fruits_calorie_dic={"딸기":34/100,"한라봉":50/100}
    
    sum_cal=total_calorie(fruits, fruits_calorie_dic)
    
    print(f"섭취하신 칼로리는 {sum_cal}입니다.")

if __name__=="__main__":
    main()