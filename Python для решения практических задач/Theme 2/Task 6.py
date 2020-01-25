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
import zipfile

person = {}

with zipfile.ZipFile('for_task_6.zip', 'r') as archive:
    for name in archive.infolist():
        read_file = xlrd.open_workbook(file_contents=archive.read(name.filename))
        sheet = read_file.sheet_by_index(0)
        person[sheet.row_values(1)[1]] = int(sheet.row_values(1)[3])

with open('output_task_6.txt', 'w') as file:
    file.writelines(f"{key} {str(value)}" + '\n' for key, value in sorted(person.items()))
