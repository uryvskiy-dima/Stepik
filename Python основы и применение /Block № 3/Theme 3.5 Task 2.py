"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:
class A:
    pass

class B(A, C):
    pass

class C(A):
    pass
Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно
от одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.

Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:
A : 3
B : 1
C : 2
"""


import json


def find(parent):
    for value_child in dict_input[parent]:
        if value_child not in lst_top:
            if value_child not in dict_result.keys():
                dict_result[value_child] = 1
            else:
                dict_result[value_child] += 1
            lst_top.append(value_child)
        find(value_child)


dict_input = {}
dict_result = {}
js = json.loads(input())
for js_value in js:
    if js_value['name'] not in dict_input.keys():
        dict_input[js_value['name']] = js_value['parents']

for key, value in dict_input.items():
    lst_top = []
    if key not in dict_result:
        dict_result[key] = 1
    else:
        dict_result[key] += 1
    find(key)


for value_sort in sorted(dict_result.keys()):
    print(f"{value_sort} : {dict_result[value_sort]}")
