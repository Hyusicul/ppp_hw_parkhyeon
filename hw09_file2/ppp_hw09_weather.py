def read_wt(filename):
    t_a=[]
    with open(filename, encoding="utf-8") as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            tem=float(tokens[4])
            t_a.append(tem)

    return t_a
        
def read_water(filename):
    water=[]
    with open(filename, encoding="utf-8") as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            w_all=float(tokens[9])
            if w_all>=5:
                water.append(w_all)

    return water

def read_allwater(filename):
    al_w=[]
    with open(filename, encoding="utf-8") as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            w_lines=float(tokens[9])
            al_w.append(w_lines)
 
    return(al_w)
            

def main():
    year_average=read_wt("weather(146)_2022-2022.csv")
    up_5mm=read_water("weather(146)_2022-2022.csv")
    all_water=read_allwater("weather(146)_2022-2022.csv")

    total_tem=0
    for i in year_average:
        total_tem+=i
    tem_len=len(year_average)
    print(f"연 평균 기온은{(total_tem/tem_len):.2f}℃이다.")
    
    water_len=len(up_5mm)
    print(f"연 강수량이 5mm이상인 날짜는 {water_len}일 이다.")

    total_water=sum(all_water)
    print(f"연 강수량은 총{total_water}mm입니다.")

if __name__=="__main__":
    main()