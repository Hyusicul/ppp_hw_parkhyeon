def get_weather_data(fname, col_idx):       
    weather_datas=[]
    with open(fname) as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            tokens[col_idx]
            #print(tokens[col_idx], type(tokens[col_idx]))
            #float(tokens[col_idx])
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_rain_events(rainfalls):
    events=[]
    c_days=0
    for rain in rainfalls:
        if rain >0:
            c_days+=1
        else:
            if c_days>0:
                events.append(c_days)
            c_days=0
    if c_days>0:                
        events.append(c_days)                    
    return events 


def get_rain_all_events(rainfalls):
    events=[]
    c_days=0
    for rain in rainfalls:
        if rain >0:
            c_days+=rain
        else:
            if c_days>0:
                events.append(c_days)
            c_days=0
    if c_days>0:                       
        events.append(c_days)           
    return events

def get_weather_data_int(fname, col_idx):
    weather_datas=[]
    with open(fname) as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            tokens[col_idx]
            #print(tokens[col_idx], type(tokens[col_idx]))
            #float(tokens[col_idx])
            weather_datas.append(int(tokens[col_idx]))
    return weather_datas

def sumifs(rainfall, months, selected=[6,7,8]):
    total=0
    for i in range(len(rainfall)):
        rain=rainfall[i]
        month=months[i]
        if month in selected:
            total += rain
    return total

def main():
    filename="./weather(146)_2022-2022.csv"
    rainfall=get_weather_data(filename,9)
    print(f"최장연속강우일수={max(get_rain_events(rainfall))}") 
    print(f"최대강수량={max(get_rain_all_events(rainfall)):.2f}")
    tmax=sorted(get_weather_data(filename, 3))[-3:][::-1]               
    print(f"가장 높았던 최고기온 3개는 {tmax}입니다.")
    months=get_weather_data_int(filename, 1)
    print(f"여름철 강수량은{sumifs(rainfall, months, selected=[6,7,8]):.2f}mm입니다.")



    filename_20yr="./weather(146)_2001-2022.csv"                              #2021년과 2022년의 강수량
    years=get_weather_data_int(filename_20yr, 0)
    rainfalls=get_weather_data(filename_20yr,9)
    print(f"2021년 총 강수량은 {sumifs(rainfalls, years, selected=[2021]):.1f}입니다.") 
    print(f"2022년 총 강수량은 {sumifs(rainfalls, years, selected=[2022]):.1f}입니다.") 

if __name__=="__main__":
    main()