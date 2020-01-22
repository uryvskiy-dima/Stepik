"""
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
В этой статье есть теги code, которыми выделяются конструкции на языке Python.
Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего
и вывести их в алфавитном порядке, разделяя пробелами.

Например, если исходный текст страницы выглядел бы так:

<code>a</code>
<a>bracadabr</a>
<code>c</code>
<code>b</code>
<code>b</code>
<code>c</code>
то в ответ надо было бы ввести строку "b c".
"""


from urllib.request import urlopen
from re import findall
import collections

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
result = collections.Counter()
for word in sorted(findall('<code>(.*?)</code>', str(html))):
    result[word] += 1

for value in result.most_common(3):
    print(value[0], end=' ')
