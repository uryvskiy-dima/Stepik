"""
В этой задаче нужно просто установить библиотеку xmltodict, скачать файл
https://stepik.org/media/attachments/lesson/245571/map1.osm, создать в директории с файлом скрипт со следующим
содержанием: и ввести в качестве ответа вывод этого скрипта.
"""


import xmltodict
import wget
import os

filename = wget.download('https://stepik.org/media/attachments/lesson/245571/map1.osm')
os.rename(filename, f'{os.getcwd()}/{filename}')

with open('map1.osm', 'r', encoding='utf8') as fin:
    xml = fin.read()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
