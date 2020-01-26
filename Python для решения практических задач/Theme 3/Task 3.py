"""
Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в интересующем
его районе. Вася скачал интересующий его кусок карты OSM https://stepik.org/media/attachments/lesson/245681/map2.osm и
хочет посчитать, сколько на нём отмечено точечных объектов (node), являющихся заправкой.
В качестве ответа вам необходимо вывести одно число - количество АЗС.

"Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать,
как обозначается заправка в OpenStreetMap.
"""


import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('map2.osm')
root = tree.getroot()

count_fuel = 0
for val in root.findall('node'):
    el_tag = val.find('tag')
    if el_tag is not None:
        if el_tag.attrib['k'] == 'amenity' and el_tag.attrib['v'] == 'fuel':
            count_fuel += 1

print(count_fuel)
