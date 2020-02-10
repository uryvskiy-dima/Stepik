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


def find(x, y, el, el1):
    try:
        count = 0
        for k in range(el, x):
            for g in range(el1, y):
                if field[k][g] == '*':
                    count += 1
    except IndexError:
        if j != m - 1:
            find((j + 1) - 2, j + 1, i, j)
        elif m <= 2:
            return find(2, 2, i, j - 1)
    return count


n, m = map(int, input().split())
field = [list(input()) for i in range(n)]


for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            continue
        else:
            if i == 0 and j == 0:  # +
                field[i][j] = find(2, 2, i, j)
            elif i == 0 and j == m - 1:  # +
                field[i][j] = find(2, 3, i, j - 1)
            elif (i == 0 and j != 0) and (j != m - 1):  # +
                if j < 3:
                    field[i][j] = find(2, 3, i, j - 1)
                else:
                    field[i][j] = find((j + 1) - 2, j + 3, i, j - 1)
            elif i != 0 and j == 0:  # +
                field[i][j] = find(3, 2, i - 1, j)
            else:
                field[i][j] = find(3, 3, i - 1, j - 1)  # +


for element in field:
    for j in element:
        print(j, end='')
    print()


