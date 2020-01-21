"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
Файл с данными:
Crimes.csv
"""


import csv

dictionary = {}
with open("Crimes.csv") as f_open:
    reader = csv.DictReader(f_open)
    for row in reader:
        if row['Date'][6:10] == '2015':
            if row['Primary Type'] not in dictionary.keys():
                dictionary[row['Primary Type']] = 1
            else:
                dictionary[row['Primary Type']] += 1

for value_key, value_max in dictionary.items():
    if max(dictionary.values()) == dictionary[value_key]:
        print(f"{value_key} : {value_max}")
# print(dict) словарь для проверки
