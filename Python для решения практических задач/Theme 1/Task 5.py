"""
В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица. Просуммируйте все числа в ней.
Теперь мы добавили разных тегов для изменения стиля отображения.
Для доступа к ячейкам используйте возможности BeautifulSoup.
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209723/4.html").read().decode('utf-8')
soup = BeautifulSoup(str(html), 'html.parser')

print(sum([int(table.text) for table in soup.find_all('td')]))
