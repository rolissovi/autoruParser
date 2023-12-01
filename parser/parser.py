import json
import os
import pandas as pd
import requests
from pymongo import MongoClient

# Подключаемся к базе данных MongoDB
client = MongoClient('127.0.0.1', 27017)
db_name = 'auto'
db = client[db_name]
carsCollection = db.cars

# Считываем JSON с сайта
URL = "https://auto.ru/-/ajax/desktop/listing/"

COOKIE = os.getenv('COOKIE')
HEADERS = '''
Host: auto.ru
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://auto.ru/cars/omoda/all/?page=2
x-client-app-version: 538.0.12961658
x-client-date: 1701009743900
x-csrf-token: 9f1ecff6b9562b40647c10692b85fd9f9edb38d4214547bc
x-requested-with: XMLHttpRequest
x-page-request-id: 25c5d18fec63d1d5b5b31a1fc152d5d4
x-retpath-y: https://auto.ru/cars/omoda/all/?page=2
x-yafp: {"a1":"+2JpUdefBw+mQw==;0","a2":";1","a3":"CR1iSOw5ZFnf1oiRJa8ONg==;2","a4":"XmSeogOZPJigHvkWSjDUAQ==;3","a5":"efQhBLCQhSsxpA==;4","a6":"zUQ=;5","a7":"LaPKR10wWrkTNQ==;6","a8":"lyC41aWoAlA=;7","a9":"AEBIrYwoc7AWFA==;8","b1":"aMDZWjhsPxLmow==;9","b2":"jp9ybD5ZGZU3Bg==;10","b3":"QIeIjuD7DkJdnQ==;11","b4":"f/z/XcPksWw=;12","b5":"MT6+pGxVWsFvyw==;13","b6":"UrFx1sfo2XI=;14","b7":"ooig26o0klKXQw==;15","b8":"7mZBKceNehvWoQ==;16","b9":"CqYxi2EHQNeo6Q==;17","c1":"4yLkIg==;18","c2":"1mL9YTI1+qXa6kxVKCxxz3Zv;19","c3":"+vs0Eck3wTCjf/7De51WnUSm;20","c4":"OaQtMb6hrfg=;21","c5":"mkm2AkHS+fw=;22","c6":"XAoOdg==;23","c7":"R2dsTGyA18s=;24","c8":"0s1YXh94c4s=;25","c9":"nzzZ+vABuSg=;26","d1":"CDQRYAY42Qk1WvCafD4nsdbLhC4HI7jBatKqTvB6Q0byMC7nzCyrbQuW9U6WrOAEpfeQWe7I;27","d2":"zkM=;28","d3":"tX8SFK4uRF9Ecw==;29","d4":"vDd4c4yqOug=;30","d5":"TO56FwYbORK86w==;31","d7":"oiUrUdzBHzU=;32","d8":"IjxCVaCEkMp3r0h5ZZ2tuKMIm845JogF38s=;33","d9":"LQV8Jy8xTSc=;34","e1":"EA+wKf+MpzyiBA==;35","e2":"Ai9Aclzi5UtTFg==;36","e3":"hDYHRlXx66yW+A==;37","e4":"9dpuIhE8kDM=;38","e5":"4epE+th/uRNlsg==;39","e6":"OLAqX7gemac=;40","e7":"iMmioNI+R8juwA==;41","e8":"nJ68q1JdrmM=;42","e9":"ZWqsw/GpjA4=;43","f1":"3Xos9hvePerwZA==;44","f2":"bDL7Syzkews=;45","f3":"SYVLQxshGpN1tw==;46","f4":"2jBBvRS5UXo=;47","f5":"BuO2+Q8ydUJrpg==;48","f6":"m7M7ssmz8SCBbQ==;49","f7":"l5gtqlw351/SCg==;50","f8":"DVd9TLTeIHCXKQ==;51","f9":"zDwHcCFHwGY=;52","g1":"DenuDViAySc=;53","g2":"OzsMGX5BaN+w0A==;54","g3":"29PDF+qHQ4M=;55","g4":"m+b4whk8jogU+A==;56","g5":"Z+yaxPTs7ao=;57","g6":"DalRDNykAkv9XQ==;58","g7":"PJ82Hy9Ufqs=;59","g8":"v6nc5RgVv2s=;60","g9":"jTEzjHiMoXw=;61","h1":"Ooa7p/A6AGeLvA==;62","h2":"4o5OADgTxLj3TA==;63","h3":"Gaira8dkH8O0Dg==;64","h4":"li7UQACCspc8Sw==;65","h5":"gsTG1TkiRKY=;66","h6":"kR80QHsOIcek0A==;67","h7":"xyX0+QfHcQd3X5bbhECNQLdv8ZrkY/B7j4mYp8bs7D7u3hvvNQczlkKu5RWrVzx9C/RuKNDQ6cNRtPrIRly/H4Il+fkHx2YHI1/U25FAlkCzb8mapWPge4WJk6fW7LU+p95U7yIHcpZHruQVvlc0fU70bCjb0KfDRLS0yA9cvh+UJfb5EMdjBzZfl9uAQN5Ak2/ImuFj7XuFibWnyuz7Pr3eXu8uByaWAK4=;68","h8":"rVCSdkKV+AFFgA==;69","h9":"mHUD/bRxvaF+Pg==;70","i1":"1YGMat/K/2s=;71","i2":"DPGpSfqNXgkLtQ==;72","i3":"QFKQPXH6kyZRmg==;73","i4":"x02iMF1Un2hvzQ==;74","i5":"mxSAWdgxXMQjFg==;75","z1":"gr4SXtJRTk6Mg6Z6Ql1an9hwq8H4M8nQtM9v++/iIFxuBeRbRVUc+JJn2FEYk5M39f4ke2GjcuhikY3/I+Cbcw==;76","z2":"rDzhP1FELZ8rsd7Bb/TdyxaDdV+ocY6+W2hstam1IAcLbvyaAJtZVbk6wOzVztdFor4nC4qu315QUkZbJjbyUg==;77","z3":"02msL6NXT9pbzA==;78","z9":"JDz4oQbz6GO45Q==;79","y1":"LT8y7Ih4AzxKZw==;80","y2":"HWkPt8zLssZ9Rw==;81","y3":"Bfu8h28PBY+q5w==;82","y4":"+BTfNdrdHkavwQ==;83","y5":"IpQNURqvb54EFg==;84","y6":"S1bI4+wwPG01dw==;85","y8":"r7GNta7PE/00lg==;86","y9":"GgLqB9HKBA0AeQ==;87","y10":"Y/NW7AjWIHkylQ==;88","x1":"1iAcPKd83o/HQA==;89","x2":"cM1fsc2hhwmNPQ==;90","x3":"fDKbSmBQgGDWCw==;91","x4":"IKtz9IfpOgK+xA==;92","z5":"1dljZ7s//K4=;93","z6":"szwG8ex+hrJUlWuV;94","z7":"AYlenYG0iuq5Z5j3;95","z8":"hOJWhE2HNooTLIuc;96","y7":"pNNnbPQneCfVcidK;97","x5":"BSI04Pohfr75UJu2;98","z4":"tBM0Eaj6BKlwDY3YV+4=;99","v":"6.3.1","pgrdt":"WMq5JI/TeIxNK6pA8JqWi+BqUj0=;100","pgrd":"NDViwRiN6qqK4JbiR+SK2yuISlvukXGIlMabDSomd3gd9699+OJP+22l8nC1uMaLCmB6G+LGmvMXMwIJaYD2z4ArolRXaptOtbbcPSUICbNtQMj/hjDBLLNwFnnlFoeotBDJuy0uDWQEhgtgimWbsmrOj/4PIfxayrqZmf3MX36Gfex50nzgb8PW/haiLIfQ9rPJ9tZYphwyUXH7Y73p1Bn3vls="}
content-type: application/json
Content-Length: 92
Origin: https://auto.ru
Connection: keep-alive
Cookie: _yasc=8pT7FEVdr2/bTkCsbt8yQhSaCk5lNA1ESPRgMFD9LsaPvKYXBZiuqHHgd50+TdH+pFM=; suid=ff409c7b77c1d601eaf0d084f6f34d8f.b6ba187ed00f3364fa1d2a8c86f5573f; autoru_sid=61759984%7C1697921933413.7776000.qIF1SqIReu7-p3VHgeaSuQ.D-DE_bLBipSKly4mSO_jzcTsGbbvh4EW1aa8myQPZh8; Session_id=3:1701009705.5.0.1697921927698:tMhcXQ:15.1.2:1|159514163.-1.2.3:1697921927|61:10017896.983824.ERSmD1RacDIwDY1QWnAm_hz3rSY; sessar=1.1184.CiBoBwOowfHAkVwxpwiBwMvGSbMLYlTn_SaQvtCE3-OYHw.niuMef93iXAYvIjhDzOOp9L99ADaNBQnUm73u74A8Sc; yandex_login=sasha-malahov2013; i=mVZxaH2cjjtPY/ASqyAYlkv2u7xv7WyitMpg20aSmYhZcRETCb2+0XoKOmtyopDFqzC4yz8pO7AQVgVByIubkAMaBl4=; yandexuid=5888769311697918409; mda2_beacon=1701009706014; layout-config={"screen_height":1080,"screen_width":1920,"win_width":1920,"win_height":697}; fp=721adb798a2bbb56a3f2cf9e1cea9941%7C1701009711939; gids=; gradius=0; L=BnF/dmNPCExid31GRFNZA0V6QEVFdQlBI1kLAjhZBSJVAAcfPUpBUnA=.1697921927.15502.366835.145572b65f62fc85798aa37886755183; autoruuid=g65342dc9242b3r00vv791muipjo72t5.d03d2d1bb31cf123162d4155b8841be7; _csrf_token=9f1ecff6b9562b40647c10692b85fd9f9edb38d4214547bc; from_lifetime=1701009741181; from=direct; autoru_sso_blocked=1; ys=udn.czo0NDE4NTI4OnZrOtCg0L7QvNCwINCb0LjRgdC%2B0LLQuNC6#c_chck.2078545486; sso_status=sso.passport.yandex.ru:synchronized; crookie=Hw/h5gFrBDMNunz1QlRHPyb7ndPSuKpU6TVq6l1PKHvASiYpUEx16ET8+0SN22UlkfPOzStNHl0HX6haIWG+1HsO0mM=; cmtchd=MTcwMTAwOTcwOTMwNA==; count-visits=2; yaPassportTryAutologin=1; popups-dr-shown-count=1; gdpr=0; _ym_uid=1701009712444929320; _ym_d=1701009712; _ym_isad=2
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
TE: trailers
'''.strip().split("\n")
dict_header = {}
for header in HEADERS:
    key, value = header.split(': ')
    dict_header[key] = value

# Парсим данные
offers = []
for i in range(1, 11):
    params = {
        "catalog_filter": [{"mark": f"BMW"}],
        "section": "all",
        "category": "cars",
        "page": i,
    }
    response = requests.post(URL, json = params, headers = dict_header)
    print("Now parcing page number", i)
    data = response.json()
    if 'offers' in data:
        offers.extend(data['offers'])

# Статус-код запроса
print(response.status_code)
# print(response.content)
# print(response.text)
# print(response.json())

# Записываем данные в JSON-файл
with open("temp.json", "w") as f:
    json.dump(offers, f)

# Считываем содержимое JSON-файла
with open("temp.json", "r") as f:
    data = json.load(f)
print(len(data))

# Списки нужных нам данных
mark = []
model = []
body = []
engine = []
power = []
transmission = []
gear = []
vendor = []
price_segment = []
price = []
year = []
pts = []
region = []
seller = []
mileage = []

# Заполняем списки
for offer in data:
    if offer['vehicle_info']:
        mark.append(offer['vehicle_info']['mark_info']['name'])
        model.append(offer['vehicle_info']['model_info']['name'])
        body.append(offer['vehicle_info']['configuration']['human_name'])
        engine.append(offer['vehicle_info']['tech_param']['engine_type'])
        power.append(offer['vehicle_info']['tech_param']['power'])
        transmission.append(offer['vehicle_info']['tech_param']['transmission'])
        gear.append(offer['vehicle_info']['tech_param']['gear_type'])
        vendor.append(offer['vehicle_info']['vendor'])
        price_segment.append(offer['vehicle_info']['super_gen']['price_segment'])

    if offer['price_info']:
        price.append(offer['price_info']['price'])

    if offer['documents']:
        year.append(offer['documents']['year'])
        # pts.append(offer['documents']['pts'])

    if offer['seller']:
        region.append(offer['seller']['location']['region_info']['name'])

    if offer['seller_type']:
        seller.append(offer['seller_type'])

    if offer['state']:
        mileage.append(offer['state']['mileage'])



# Создаём дата-фрейм с данными
df = pd.DataFrame({
    'Mark': mark,
    'Model': model,
    'Year': year,
    'Price rub': price,
    'Mileage': mileage,
    'Region': region,
    'Seller': seller,
    'Power Hp': power,
    'Engine type': engine,
    'Gear type': gear,
    'Transmission': transmission,
    'Body type': body,
    'Vendor country': vendor,
    'Price segment': price_segment

})

# Выгружаем данные в MongoDB
data_dict = df.to_dict("records")
carsCollection.insert_many(data_dict)


# Сохраняем в эксель и csv
# df.to_excel('JETOUR.xlsx')
df.to_csv(f'BMW.CSV')

# Очищаем JSON
with open("temp.json", "w") as f:
    pass

