"""
Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой.
К счастью, у него сохранились расчётные листки всех сотрудников.
Помогите по этим расчётным листкам восстановить зарплатную ведомость.
Архив с расчётными листками доступен по ссылке https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
(вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его зарплата.
Сотрудники должны быть упорядочены по алфавиту.
"""


import xlrd
import zipfile
import wget
import os

filename = wget.download('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip')
os.rename(filename, f'{os.getcwd()}/{filename}')

person = {}
with zipfile.ZipFile('rogaikopyta.zip', 'r') as archive:
    for name in archive.infolist():
        read_file = xlrd.open_workbook(file_contents=archive.read(name.filename))
        sheet = read_file.sheet_by_index(0)
        person[sheet.row_values(1)[1]] = int(sheet.row_values(1)[3])

with open('output_task_6.txt', 'w') as file:
    file.writelines(f"{key} {str(value)}" + '\n' for key, value in sorted(person.items()))
