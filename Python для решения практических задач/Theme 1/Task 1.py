"""
Мы сохранили страницу с википедии про языки программирования и сохранили по адресу baseurl/lect1/1.html
https://stepik.org/media/attachments/lesson/209717/1.html

Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++
(ответ должен быть одной из этих двух строк).
"""


from urllib.request import urlopen


html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
print("C++ -", str(html).count("C++"))
print("Python -", str(html).count("Python"))
