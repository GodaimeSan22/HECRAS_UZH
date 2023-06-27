import requests
from bs4 import BeautifulSoup
import csv

stations = {
    'Uzhgorod_id': {'id': '11', 'file': 'water_level_st_Uzhgorod_BUVR.csv'},
    'Zarichevo_id': {'id': '44', 'file': 'water_level_st_Zarichevo_BUVR.csv'},
    'Zhornava_id': {'id': '30', 'file': 'water_level_st_Zhornava_BUVR.csv'},
    'Simer_id': {'id': '43', 'file': 'water_level_st_Simer_BUVR.csv'},
    'Chornogolova_id': {'id': '25', 'file': 'water_level_st_Chornogolova_BUVR.csv'},
    'Berezniy_id': {'id': '29', 'file': 'water_level_st_Berezniy_BUVR.csv'}
}

url = 'http://gmc.uzhgorod.ua/fixdata.php?StNo='

for station_name, station_data in stations.items():
    station_id = station_data['id']
    file_name = station_data['file']

    url_st_BUVR = url + station_id
    response = requests.get(url_st_BUVR)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        new_records = []
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            existing_records = set(tuple(row) for row in reader)
            for row in rows[1:]:
                cells = row.find_all('td')
                date = cells[0].text.strip()
                time = cells[1].text.strip()
                water_level = cells[2].text.strip()
                record = (date, time, water_level)
                if record not in existing_records:
                    new_records.append(record)

        if new_records:
            with open(file_name, mode='a', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                for record in new_records:
                    writer.writerow(record)