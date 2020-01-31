"""
Напишите программу, которая принимает на вход список чисел и число, после чего выводит все позиции, на которых это
число встречается в переданном списке.
Позиции в списке нумеруются с нуля.
Если число x не найдено в списке, нужно вывести строку "None" (без кавычек, с большой буквы).
Формат ввода:
На первой строке содержатся значения списка -- целые числа, разделённые пробелом. На второй строке содержится целое
число, позиции которого нужно найти.
Формат вывода:
Одна строка, в которой содержится слово "None" или через пробел перечислены числа -- позиции, на которых число x
встречается в списке lst. Позиции должны быть выведены в порядке возрастания.

Sample Input 1:
5 8 2 7 8 8 2 4
8

Sample Output 1:
1 4 5

Sample Input 2:
5 8 2 7 8 8 2 4
10

Sample Output 2:
None
"""


lst = input().split()
x = input()
if x in lst:
    [print(i) for i in range(len(lst)) if x == lst[i]]
else:
    print('None')
