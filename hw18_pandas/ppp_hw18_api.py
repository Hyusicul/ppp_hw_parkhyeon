import requests
import os
import pandas as pd

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "utf-8"
        f.write(resp.text)


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

    rain_2012="weather_146_2012-2012.csv"
    max_t_2024="weather_146_2024-2024.csv"
    max_tx_tm="weather_146_2020-2020.csv" #2020년 자료csv파일은 직접 수정하였기에 csv파일을 삭제하고 다시 다운받으면 정상 실행 x
    jeonju_rain_2019="weather_146_2019-2019.csv"
    suwon_rain_2019="weather_119_2019-2019.csv"
    if not os.path.exists(rain_2012):
        download_weather(146, 2012, rain_2012)
    if not os.path.exists(max_t_2024):
        download_weather(146, 2024, max_t_2024)    

    if not os.path.exists(jeonju_rain_2019):
        download_weather(146, 2019, jeonju_rain_2019)      
    if not os.path.exists(suwon_rain_2019):
        download_weather(119, 2019, suwon_rain_2019)  

    df_2012=pd.read_csv(rain_2012, skipinitialspace=True)
    # print(round(df_2012["rainfall"].sum(),1))

    df_2024=pd.read_csv(max_t_2024, skipinitialspace=True)
    # print(df_2024["tmax"].max())
  
    df_2020=pd.read_csv(max_tx_tm, skipinitialspace=True)
    # print(df_2020["tdiff"].max())

    df_2019_jj=pd.read_csv(jeonju_rain_2019, skipinitialspace=True)
    jj2019=(df_2019_jj["rainfall"].sum())

    df_2019_sw=pd.read_csv(suwon_rain_2019, skipinitialspace=True)
    sw2019=(df_2019_sw["rainfall"].sum())

    # print(j_s_rainfall)





    name = "박현"
    affiliation = "스마트팜학과"
    student_id = "202210072"

    answer1 = round(df_2012["rainfall"].sum(), 1)
    answer2 = df_2024["tmax"].max()
    answer3 = df_2020["tdiff"].max()
    jj2019 = df_2019_jj["rainfall"].sum()
    sw2019 = df_2019_sw["rainfall"].sum()
    answer4 = jj2019 + sw2019


    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()