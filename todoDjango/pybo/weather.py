# https://newstroyblog.tistory.com/433

import requests
import xmltodict
import json
from datetime import datetime

# 현재 시간 불러오기
now = datetime.now().date()
# 오류 안나게 - 제거
tonow = str(now).replace('-','')

# 초단기예보
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
# 단기예보
# url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
params ={'serviceKey' : 'QCm74+CmnGEJDOzL+wIQlr5LUEwzfwgYfGGBPpAaEE2fkCqaJ7PKQD9dbuf0S5jOQxE5BRmyZmkO6cMDg+O72A==',
        'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : tonow, 'base_time' : '0500', 'nx' : '63', 'ny' : '110' }

def forecast():
    response = requests.get(url, params=params)

    xmlData = response.text  # xml데이터
    # xml 데이터 그대로 진행
    # dict = xmltodict.parse(xmlData)

    # xml 데이터 json으로 변환
    jsonStr = json.dumps(xmltodict.parse(xmlData), indent=4) # xml to json
    dictdata = json.loads(jsonStr)

    #값 가져오기
    weather_data = dict()
    for item in dictdata['response']['body']['items']['item']:
        # 기온
        if item['category'] == 'T1H':
            weather_data['tmp'] = item['fcstValue']
        # 습도
        if item['category'] == 'REH':
            weather_data['hum'] = item['fcstValue']
        # 하늘상태: 맑음(1) 구름많은(3) 흐림(4)
        if item['category'] == 'SKY':
            weather_data['sky'] = item['fcstValue']
        # 강수형태: 없음(0), 비(1), 비/눈(2), 눈(3), 빗방울(5), 빗방울눈날림(6), 눈날림(7)
        if item['category'] == 'PTY':
            weather_data['sky2'] = item['fcstValue']
        # 시간
        weather_data['time'] =  item["fcstTime"][:2]+":"+item["fcstTime"][2:]
        weather_data['date'] =  item["fcstDate"][:4] + "년" + item["fcstDate"][4:6] + "월" + item["fcstDate"][6:] + "일"

    return weather_data

def proc_weather():
    dict_sky = forecast()

    str_sky = "천안시 동남구 / \n"

    if dict_sky['sky'] != None or dict_sky['sky2'] != None:

        str_sky = str_sky + "날씨 : "

        if dict_sky['sky2'] == '0':
            if dict_sky['sky'] == '1':
                str_sky = str_sky + "맑음"
            elif dict_sky['sky'] == '3':
                str_sky = str_sky + "구름많음"
            elif dict_sky['sky'] == '4':
                str_sky = str_sky + "흐림"
        elif dict_sky['sky2'] == '1':
            str_sky = str_sky + "비"
        elif dict_sky['sky2'] == '2':
            str_sky = str_sky + "비와 눈"
        elif dict_sky['sky2'] == '3':
            str_sky = str_sky + "눈"
        elif dict_sky['sky2'] == '5':
            str_sky = str_sky + "빗방울이 떨어짐"
        elif dict_sky['sky2'] == '6':
            str_sky = str_sky + "빗방울과 눈이 날림"
        elif dict_sky['sky2'] == '7':
            str_sky = str_sky + "눈이 날림"
        str_sky = str_sky + " / \n"
    if dict_sky['tmp'] != None:
        str_sky = str_sky + dict_sky['tmp'] + 'ºC / \n'
    # if dict_sky['hum'] != None:
    #     str_sky = str_sky + "습도 : " + dict_sky['hum'] + '% \n'
    
    if dict_sky['date'] != None:
        str_sky = str_sky + dict_sky['date'] + ' / \n'
    if dict_sky['time'] != None:
        str_sky = str_sky + dict_sky['time']
        
    return str_sky
    
print(proc_weather())

# 출처: https://dalseobi.tistory.com/130 [달에 앉아있는 서비:티스토리]


# response = requests.get(url, params=params)

# xmlData = response.text  # xml데이터
# # xml 데이터 그대로 진행
# # dict = xmltodict.parse(xmlData)

# # xml 데이터 json으로 변환
# jsonStr = json.dumps(xmltodict.parse(xmlData), indent=4) # xml to json
# dict = json.loads(jsonStr)

# for item in dict["response"]["body"]["items"]["item"]:
#     # category가 기온에 해당하는 tmp가 아닐 시 건너뛰기
#     # if item["category"] != "TMP":   # 단기
#     if item["category"] != "T1H":   # 초단기
#         continue
#     result= []
#     result.append({
#                "날짜" : item["fcstDate"][:4] + "년" + item["fcstDate"][4:6] + "월" + item["fcstDate"][6:] + "일",
#                "시간대" : item["fcstTime"][:2]+":"+item["fcstTime"][2:],
#                "기온" : item["fcstValue"]+"℃",
#                "하늘상태" : item["fcstValue"]
#                })
# print(result)


# Python3 샘플 코드 #


# import requests

# url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
# # params ={'serviceKey' : 'QCm74%2BCmnGEJDOzL%2BwIQlr5LUEwzfwgYfGGBPpAaEE2fkCqaJ7PKQD9dbuf0S5jOQxE5BRmyZmkO6cMDg%2BO72A%3D%3D',
# params ={'serviceKey' : 'QCm74+CmnGEJDOzL+wIQlr5LUEwzfwgYfGGBPpAaEE2fkCqaJ7PKQD9dbuf0S5jOQxE5BRmyZmkO6cMDg+O72A==',
#          'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : '20240624', 'base_time' : '0600', 'nx' : '55', 'ny' : '127' }

# response = requests.get(url, params=params)
# print(response.content)