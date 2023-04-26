import requests
from bs4 import BeautifulSoup
import csv

# URL-адреса сторінки з даними
url = 'https://buvrtysa.gov.ua/newsite/?page_id=329&sn=1'

# Відправляємо GET-запит на сервер і зберігаємо відповідь
response = requests.get(url)

# Перевіряємо, що запит був успішним
if response.status_code == 200:
    # Розбираємо HTML-сторінку з використанням BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Отримуємо дані графіка
    chart_script = soup.find_all('script')[1]
    if chart_script.string:
        chart_data = chart_script.string.split('\n')[5].replace('data: [','').replace('],','').replace('{','').replace('y:','').replace('a:','').replace('}','').split(',')
        # Створюємо файл для зберігання даних
        with open('chart_data.csv', mode='w', newline='') as file:
            # Записуємо заголовки стовпців у файл
            writer = csv.writer(file)
            writer.writerow(['Час', 'Рівень води, см'])
            # Перебираємо дані графіка та записуємо їх у файл
            for i in range(0, len(chart_data), 2):
                time = chart_data[i].strip().replace('\'', '')
                water_level = chart_data[i+1].strip().replace('\'', '')
                writer.writerow([time, water_level])
