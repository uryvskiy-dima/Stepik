"""
Последовательность n \gt 0 n>0 целых чисел называется jolly jumper в случае, если значения абсолютных разностей
последовательных элементов принимают все возможные значения между 1 1 и n-1 n−1.
Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, так как абсолютные разности равны
4 1 3 2, соответственно, а  n-1 = 4 n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.
Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.
Формат ввода:
Строка, содержащая 1 \le n \le 10000 1≤n≤10000 целых чисел, разделённых пробелом.
Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и "Not jolly"
в противном случае.

Sample Input 1:
1 -3 -4 -1 1

Sample Output 1:
Jolly

Sample Input 2:
1 3 5

Sample Output 2:
Not jolly

Sample Input 3:
4

Sample Output 3:
Jolly
"""


lst = list(map(int, input().split()))
result = []

index = 0
while index < len(lst) - 1:
    result.append(abs(lst[index] - lst[index + 1]))
    index += 1

flag = False
if len(result) == len(lst) - 1:
    for value in range(1, len(lst)):
        if value in result:
            flag = True
        else:
            flag = False
            break
else:
    flag = False

if flag or len(lst) == 1:
    print("Jolly")
else:
    print("Not jolly")

