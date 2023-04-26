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
    with open('water_level_data.csv', mode='a', newline='') as file:
        # Записуємо заголовки стовпців у файл
        writer = csv.writer(file)
        writer.writerow(['Date', 'Time', 'Level'])
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

csv_filename = 'water_level_data.csv'

# Відкриття файлу у режимі читання
with open(csv_filename, 'r') as file:
    # Зчитування вмісту файлу
    content = file.read()

# Розбиття вмісту на рядки
lines = content.split('\n')

# Видалення дублікатів рядків, перетворення списку рядків назад у рядок
unique_lines = '\n'.join(list(set(lines)))

# Відкриття файлу у режимі запису
with open(csv_filename, 'w') as file:
    # Запис оновленого вмісту у файл
    file.write(unique_lines)


csv_filename = 'water_level_data.csv'

# Зчитування даних з файлу
with open(csv_filename, 'r', newline='') as file:
    reader = csv.reader(file)
    lines = list(reader)

# Сортування рядків за першим стовпцем (наприклад, за датою)
sorted_lines = sorted(lines[1:], key=lambda x: x[0])

# Збереження відсортованих даних у файл
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(lines[0])  # Запис заголовка
    writer.writerows(sorted_lines)  # Запис відсортованих рядків