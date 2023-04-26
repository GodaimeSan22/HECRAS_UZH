import requests
from bs4 import BeautifulSoup
import csv

# URL-адреса сторінки з даними
url = 'http://gmc.uzhgorod.ua/fixdata.php?StNo=11'

# Відправляємо GET-запит на сервер і зберігаємо відповідь
response = requests.get(url)

# Перевіряємо, що запит був успішним
if response.status_code == 200:
    # Розбираємо HTML-сторінку з використанням BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Отримуємо таблицю з даними
    table = soup.find('table')
    # Отримуємо рядки таблиці
    rows = table.find_all('tr')
    # Створюємо файл для зберігання даних
    with open('water_level_data.csv', mode='w', newline='') as file:
        # Записуємо заголовки стовпців у файл
        writer = csv.writer(file)
        writer.writerow(['Дата', 'Час', 'Рівень води'])
        # Перебираємо рядки таблиці та записуємо дані у файл
        for row in rows[1:]:
            # Отримуємо комірки рядка
            cells = row.find_all('td')
            # Отримуємо значення дати, часу та рівня води
            date = cells[0].text.strip()
            time = cells[1].text.strip()
            water_level = cells[2].text.strip()
            # Записуємо значення у файл
            writer.writerow([date, time, water_level])