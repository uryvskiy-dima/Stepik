"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"
Вхождения строки t в строку s:
abababa
abababa
abababa

Sample Input 1:
abababa
aba
Sample Output 1:
3
Sample Input 2:
abababa
abc
Sample Output 2:
0
Sample Input 3:
abc
abc
Sample Output 3:
1
Sample Input 4:
aaaaa
a
Sample Output 4:
5
"""


string_input, substring = input(), input()
count = 0
for index, value in enumerate(string_input):
    if string_input[index: index + len(substring)] == substring:
        count += 1
print(count)
