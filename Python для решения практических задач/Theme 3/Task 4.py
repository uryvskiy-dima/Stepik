"""
Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой.
Вася предполагает, что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре.
Определите, сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты
https://stepik.org/media/attachments/lesson/245681/map2.osm
"""


import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('map2.osm')
root = tree.getroot()

count_fuel = 0
for val in root.iter():
    if 'fuel' in val.attrib.values():
        count_fuel += 1

print(count_fuel)
