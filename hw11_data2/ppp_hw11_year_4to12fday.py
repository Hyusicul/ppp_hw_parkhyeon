def get_weather_data(fname, col_idx):       
    weather_datas=[]
    with open(fname) as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas
def get_weather_dates(fname):               #날짜 구하기
    weather_dates=[]
    with open(fname) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.strip().split(",")
            #print(tokens[col_idx], type(tokens[col_idx]))
            #float(tokens[col_idx])
            weather_dates.append([int(tokens[0]),int(tokens[1]),int(tokens[2])])
    return weather_dates



def gdd_200(dates, tavg):
    gdd_over_200day=[]
    base_temp=5
    years=[]
    for date in dates:
        y=date[0]
        if y not in years:
            years.append(y)
            gdd_over_200day.append([0])

    
    
    for i in range(len(tavg)):
        t = tavg[i]
        month = dates[i][1]
        year = dates[i][0]

        if month in [4,5,6,7,8,9,10,11,12]:
            if t >= base_temp:
                gap = t - base_temp
                if gap>=200:
                    idx=years.index(year)
                    gdd_over_200day.append(idx)    

    return years,gdd_over_200day



def main():
    filename="weather(146)_2001-2022.csv"
    dates=get_weather_dates(filename)
    tavg=get_weather_data(filename,4)
    years, gdd_200=gdd_200(dates,tavg)
    for i in range(len(years)):
        print(f"{years[i]}년에서 gdd가 200이 최초로 넘은 날짜는 {gdd_200[i]}일입니다.")     #실패

if __name__=="__main__":
    main()