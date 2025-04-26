def get_weather_data(fname, col_idx):     
    weather_datas=[]
    with open(fname) as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_weather_dates(fname):              
    weather_dates=[]
    with open(fname) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.strip().split(",")
            weather_dates.append([int(tokens[0]),int(tokens[1]),int(tokens[2])])
    return weather_dates
def maximum_temp_gap(dates, tmax, tmin):
    years=[]
    for date in dates:
        y=date[0]
        if y not in years:      #년도를 [0]으로 기본값(2001)으로 놓고 년도리스트내에서 반복하면서 같은게 나오지 않는다면 그 년도를 years에 추가가
            years.append(y)
    
    max_dates = []   
    max_gaps = []     

    for y in years:
        max_gap = 0  
        max_date = [0, 0, 0]
        for i in range(len(dates)):
            if dates[i][0] == y:            #[a,b,c]중 a만 꺼내는 함수
                gap = tmax[i] - tmin[i]
                if gap > max_gap:
                    max_gap = gap
                    max_date = dates[i]
        max_dates.append(max_date)
        max_gaps.append(max_gap)
    return years, max_dates, max_gaps
        
def main():
    filename="weather(146)_2001-2022.csv"   
    dates=get_weather_dates(filename)   
    tmax=get_weather_data(filename,3)
    tmin=get_weather_data(filename,5)   
    years, max_dates, max_gaps = maximum_temp_gap(dates, tmax, tmin)

    for i in range(len(years)):
        print(f"{years[i]}년 최대 일교차는 {max_gaps[i]:.1f}도이며, 날짜는 {max_dates[i][1]}월 {max_dates[i][2]}일입니다.")


if __name__=="__main__":
    main()