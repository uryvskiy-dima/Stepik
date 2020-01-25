"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с
указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными
(можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял целую и
дробную часть чисел запятой. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx

Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и его
количества в граммах. Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов.
Числа округлите до целых вниз и введите через пробел.
"""


import xlrd
import math

read_file = xlrd.open_workbook('tab_for_task_4.xlsx')
sheet = read_file.sheet_by_index(1)
count_product = {}

for row in range(1, sheet.nrows):
    if sheet.row_values(row)[0] in count_product.keys():
        count_product[sheet.row_values(row)[0]] = sheet.row_values(row)[1] * 2
    else:
        count_product[sheet.row_values(row)[0]] = sheet.row_values(row)[1]


sheet = read_file.sheet_by_index(0)
result = {}

for row in range(1, sheet.nrows):
    value_p = sheet.row_values(row)
    result[value_p[0]] = [value_p[1], value_p[2], value_p[3], value_p[4]]

res = [0, 0, 0, 0]

for key, value in count_product.items():
    for i in range(len(result[key])):
        if result[key][i] != '':
            res[i] += result[key][i] * (value / 100)
        else:
            res[i] += 0



for element in res:
    print(math.floor(element), end=' ')




