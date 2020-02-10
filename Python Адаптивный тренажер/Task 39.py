"""
Поле для игры сапёр представляет собой сетку размером n×m.
В ячейке сетки может находиться или отсутствовать мина.
Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается число мин,
находящихся в соседних ячейках (учитывая диагональные направления)
Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤100, после чего в n строках содержится
описание поля в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка −
ячейку с миной.
Формат вывода:
n n строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"), при этом
число означает количество мин в соседних ячейках поля.

Sample Input:

4 4
..*.
**..
..*.
....

Sample Output:
23*1
**32
23*1
0111
"""


def find_neighbors(i, j):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ai, aj = i + di, j + dj
            if 0 <= ai < n and 0 <= aj < m and lst[ai][aj] == '*':
                count += 1
    return count


n, m = map(int, input().split())
#  получил начальное поле
start_field = [list(input()) for i in range(n)]
#  получил поле с 0 и * для более удобной работы
lst = [[0 if start_field[i][j] != '*' else '*' for j in range(m)] for i in range(n)]
#  поиск соседей вокруг мины
lst = [[find_neighbors(i, j) if lst[i][j] == 0 else '*' for j in range(m)] for i in range(n)]
#  вывод результата
[print(*row, sep='') for row in lst]
