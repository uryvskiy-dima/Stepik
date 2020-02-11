"""
Напишите программу, вычисляющую следующее состояние поля для Game of life.
Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного
конца (поле представляет собой тор).
Формат ввода:
На первой строке указаны два целых числа через пробел -- высота и ширина поля.
В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.
Формат вывода:
Следующее состояние поля, используя те же обозначения, что использовались на вводе.

Sample Input 1:
5 5
.....
..X..
...X.
.XXX.
.....

Sample Output 1:
.....
.....
.X.X.
..XX.
..X..

Sample Input 2:
5 5
.....
.....
.XXX.
.....
.....

Sample Output 2:
.....
..X..
..X..
..X..
.....

Sample Input 3:
5 6
...XX.
.XX...
..X...
XX....
X..XX

Sample Output 3:
.X..XX
.XX...
X.X...
XXXX.X
XXXXX.
"""


def game_of_life(row, column):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if start_field[(row + i + n) % n][(column + j + m) % m] == 'X':
                    count += 1

    return 'X' if start_field[row][column] == 'X' and count == 2 or count == 3 else '.'


n, m = map(int, input().split())
#  получил начальное поле
start_field = [list(input()) for i in range(n)]
#  алгоритм поиска соседей
lst = [[game_of_life(i, j) for j in range(m)] for i in range(n)]
#  вывод результата
[print(*row, sep='') for row in lst]
