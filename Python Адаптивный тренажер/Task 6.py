"""
Напишите программу, которая вычисляет долю студентов, получивших оценку A.
Используется пятибальная система оценивания с оценками A, B, C, D, F.
Формат ввода:
Строка, в которой через пробел записаны оценки студентов. Оценок всегда не меньше одной.
Формат вывода:
Дробное число с ровно двумя знаками после запятой.

Sample Input 1:
F B A A B C A D

Sample Output 1:
0.38

Sample Input 2:
B C B

Sample Output 2:
0.00

Sample Input 3:
A D

Sample Output 3:
0.50
"""


string = input().replace(' ', '')
print('{0:.2f}'.format(string.count('A') / len(string)))
