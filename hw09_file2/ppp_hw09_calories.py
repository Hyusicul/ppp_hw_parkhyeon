def read_db(filename):
    calories_dic=dict()
    with open(filename, encoding="utf-8") as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.split(",")            
            line=line.strip()
            tokens_1=int(tokens[1])
            tokens_2=int(tokens[2])
            calories_dic[tokens[0]]=tokens_1*(tokens_2/100)
    return calories_dic


def main():
    calories=read_db("./calorie_db.csv")
    total=0
    for i in calories:
        total+=calories[i]
    print(f"총 칼로리는 {total}kcal 입니다.")
if __name__=="__main__":
    main()