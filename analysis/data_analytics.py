# import json
# import requests
import statistics
import pandas as pd
from pymongo import MongoClient

def amount_statistics(params):
    print("Среднее занчение: ", statistics.mean(params))
    print("Минимальное значение: ", min(params))
    print("Максимальное значение: ", max(params))

def unique_data(alldata):
    udata = []
    for item in alldata:
        if item not in udata:
            udata.append(item)
    return udata

def duplicates_counter(lst):
    counter = {}
    for item in lst:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter

# def duplicates_counter(lst):
#     counter = {}
#     if item in counter:
#         counter[item] += 1
#     else:
#         counter[item] = 1
#     return counter

# def map(new_dict, document):
#     for word in document:
#         new_dict.duplicates_counter(document)
#     return new_dict

# Подключаемся к базе данных MongoDB
client = MongoClient('127.0.0.1', 27017)
db_name = 'auto'
db = client[db_name]
carsCollection = db.cars

i = 0
region = []
geartype = []
engine = []
seller = []
price_segment = []
vendor = []
body = []
transmission = []
model = []


prices = []
year = []
power = []
mileage = []

# Считываем документы
cars = carsCollection.find({})
for document in cars:
    # print(document)
    i+=1
    year.append(document['Year'])
    prices.append(document['Price rub'])
    power.append(document['Power Hp'])
    mileage.append(document['Mileage'])
    region.append(document['Region'])
    geartype.append(document['Gear type'])
    engine.append(document['Engine type'])
    seller.append(document['Seller'])
    price_segment.append(document['Price segment'])
    vendor.append(document['Vendor country'])
    body.append(document['Body type'])
    transmission.append(document['Transmission'])
    model.append(document['Model'])

# # Уникальные значения городов
# unique_region = []
# unique_region = unique_data(region)
# dfreg = pd.DataFrame({'Region': unique_region})
# dfreg.to_csv('UniqueRegion.csv')
#
print("\nПроанализировано ", i, " объявлений")

print("\nДанные по годам")
amount_statistics(year)

print("\nДанные по стоимости")
amount_statistics(prices)

print("\nДанные о пробеге")
amount_statistics(mileage)

print("\nДанные по мощности авто")
amount_statistics(power)
#
# # Частота по городам
# region_freq = {}
# region_freq = duplicates_counter(region)
# frqreg = pd.DataFrame(list(region_freq. items()), columns=['City', 'Number of offers'])
# frqreg.to_csv("region_count.csv")
#
# # Частота по типам коробок передач
# gear_freq = {}
# gear_freq = duplicates_counter(geartype)
# frqgr = pd.DataFrame(list(gear_freq. items()), columns=['Gear type', 'Frequency'])
# frqgr.to_csv("gear_count.csv")
#
# # Частота по странам-производителям
# vendor_freq = {}
# vendor_freq = duplicates_counter(vendor)
# frqven = pd.DataFrame(list(vendor_freq. items()), columns=['Vendor', 'Frequency'])
# frqven.to_csv("vendor_count.csv")
#
# # Частота по типу двигателя
# engine_freq = {}
# engine_freq = duplicates_counter(engine)
# frqen = pd.DataFrame(list(engine_freq. items()), columns=['Engine type', 'Frequency'])
# frqen.to_csv("engine_count.csv")
#
# # Частота по типу кузова
# body_freq = {}
# body_freq = duplicates_counter(body)
# frqbod = pd.DataFrame(list(body_freq. items()), columns=['Body type', 'Frequency'])
# frqbod.to_csv("body_count.csv")
#
# # Частота по типу продавцов
# seller_freq = {}
# seller_freq = duplicates_counter(seller)
# frqsel = pd.DataFrame(list(seller_freq. items()), columns=['Seller type', 'Frequency'])
# frqsel.to_csv("seller_count.csv")
#
# # Частота по ценновым сегментам
# price_segment_freq = {}
# price_segment_freq = duplicates_counter(price_segment)
# frqpr = pd.DataFrame(list(price_segment_freq. items()), columns=['Gear type', 'Frequency'])
# frqpr.to_csv("segment_count.csv")
#
# # Частота по типу кпп
# transmission_freq = {}
# transmission_freq = duplicates_counter(transmission)
# frqtr = pd.DataFrame(list(transmission_freq. items()), columns=['Gear type', 'Frequency'])
# frqtr.to_csv("transmission_count.csv")

# Частота по моделям
# model_freq = {}
# model_freq = duplicates_counter(model)
# frqtr = pd.DataFrame(list(model_freq. items()), columns=['Model type', 'Frequency'])
# frqtr.to_csv("model_count.csv")