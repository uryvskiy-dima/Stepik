"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с
указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными
(можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял целую и дробную
часть чисел запятой. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx

Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня, названия продукта
и его количества в граммах. Для каждого дня посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и
углеводов. Числа округлите до целых вниз и введите через пробел. Информация о каждом дне должна выводиться в отдельной
строке.
"""


import xlrd
import math

read_file = xlrd.open_workbook('tab_for_task_5.xlsx')
sheet = read_file.sheet_by_index(1)

product = {int(sheet.row_values(row)[0]): [] for row in range(1, sheet.nrows)}
for row in range(1, sheet.nrows):
    key, *value = sheet.row_values(row)
    if value[0] in product[key]:
        product[key][product[key].index(value[0]) + 1] += value[1]
    else:
        product[key] += [value[0], value[1]]

sheet = read_file.sheet_by_index(0)
result = {}

for row in range(1, sheet.nrows):
    value_p = sheet.row_values(row)
    result[value_p[0]] = [value_p[1], value_p[2], value_p[3], value_p[4]]

res = {key: [0, 0, 0, 0] for key in product.keys()}
for key, value in product.items():
    for i in range(len(result[value[0]])):
        for index in range(1, len(value), 2):
            res[key][i] += result[value[index - 1]][i] * (value[index] / 100) if result[value[index - 1]][i] != '' else 0

for key, value in res.items():
    print(*map(math.floor, value))
