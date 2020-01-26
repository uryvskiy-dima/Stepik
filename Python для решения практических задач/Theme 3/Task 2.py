"""
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, возможно замкнутой)
и не иметь собственных тегов. Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm
фрагмента карты посчитайте, сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа
введите два числа, разделённых пробелом.
"""


import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('map1.osm')
root = tree.getroot()

count_tags = []
for val in root.findall('node'):
    tag = val.find('tag')
    count_tags.append('empty' if tag is None else 'have')

print(count_tags.count('have'), count_tags.count('empty'))
