import requests
import os
def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "utf-8"
        f.write(resp.text)


def rainfall(fname, col):
    rain=[]
    with open(fname) as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            rain.append(float(tokens[col]))
    rainsum=sum(rain)
    return rainsum

def max_of_tavg(fname, col):
    tavg=[]
    with open(fname) as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            tavg.append(float(tokens[col]))
    max_t=max(tavg)
    return max_t


def tmax_tmin(fname, ttx, ttm):
    tmax=[]
    tmin=[]
    t_list=[]
    with open(fname) as f:
        lines=f.readlines()[1:]
        for line in lines:
            tokens=line.strip().split(",")
            tmax.append(float(tokens[ttx]))
            tmin.append(float(tokens[ttm]))

    for i in range(len(tmax)):
        t_list.append(tmax[i]-tmin[i])
    tx_tm=sorted(t_list)[-1]
    return tx_tm

def suwon_jeonju_rain(fname_s, fname_j, col):
    rain_s=[]
    rain_j=[]
    with open(fname_s) as fs:
        lines_s=fs.readlines()[1:]
        for line in lines_s:
            tokens=line.strip().split(",")
            rain_s.append(float(tokens[col]))
    with open(fname_j) as fj:
        lines_j=fj.readlines()[1:]
        for line in lines_j:
            tokens=line.strip().split(",")
            rain_j.append(float(tokens[col]))
    sum_suwon=sum(rain_s)
    sum_jeonju=sum(rain_j)
    if sum_suwon>sum_jeonju:
        rain_s_j=sum_suwon-sum_jeonju
    else:
        rain_s_j=sum_jeonju-sum_suwon   

    return rain_s_j 

def submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=False):
    base_url = "http://sfarm.digitalag.kr:8800/submission/create"
    params = {
        "name": name,
        "affiliation": affiliation,
        "student_id": student_id,
        "param1": answer1,
        "param2": answer2,
        "param3": answer3,
        "param4": answer4,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        if verbose:
            print("응답 코드:", response.status_code)
            print("제출 성공! 응답:", response.text)
        return True
    except requests.exceptions.RequestException as e:
        if verbose:
            print("제출 중 오류 발생:", e)
        return False

def main():

    rain_2015="weather_146_2015-2015.csv"
    max_t_2022="weather_146_2022-2022.csv"
    max_tx_tm="weather_146_2024-2024.csv"
    suwon_rain_2024="weather_119_2024-2024.csv"
    if not os.path.exists(rain_2015):
        download_weather(146, 2015, rain_2015)
    if not os.path.exists(max_t_2022):
        download_weather(146, 2022, max_t_2022)    
    if not os.path.exists(max_tx_tm):
        download_weather(146, 2024, max_tx_tm)    
    if not os.path.exists(suwon_rain_2024):
        download_weather(119, 2024, suwon_rain_2024)  

    y_rain=rainfall(rain_2015, 9)
    tavg_2022=max_of_tavg(max_t_2022, 4)
    tx_tm=tmax_tmin(max_tx_tm, 3, 5)
    
    suwon_jeonju_2024=suwon_jeonju_rain(suwon_rain_2024, max_tx_tm, 9)
    s_j_2024=round(suwon_jeonju_2024,1)
    # print(y_rain)
    # print(tavg_2022)
    # print(tx_tm)     
    #print(s_j_2024)







    name = "박현"
    affiliation = "스마트팜학과"
    student_id = "202210072"

    answer1 = y_rain
    answer2 = tavg_2022
    answer3 = tx_tm
    answer4 = s_j_2024


    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()