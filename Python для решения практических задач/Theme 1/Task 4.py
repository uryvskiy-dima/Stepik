"""
В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица.
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму.
Для доступа к ячейкам используйте возможности BeautifulSoup.
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209723/3.html").read().decode('utf-8')
soup = BeautifulSoup(str(html), 'html.parser')

print(sum([int(table.text) for table in soup.find_all('td')]))
