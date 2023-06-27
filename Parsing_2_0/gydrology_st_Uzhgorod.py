import pandas as pd

# Зчитуємо дані з файлу
data = pd.read_csv('water_level_st_Uzhgorod_BUVR.csv', header=None, names=['datetime', 'web_level', 'other'])

# Замінюємо NaN на 0
data.fillna(0, inplace=True)

# Функція для обробки третього числа
def process_third_value(value):
    if value != 'Time' :
        if float(value) :
            if int(value) != 0:
                return (float(value) + 11238) / 100
            else:
                return 'None'
        else:
            return 'None'
    else:
        return 'No Data'

# Застосовуємо функцію до стовпця 'value2' і створюємо новий стовпець 'value3' для зберігання результатів
data['absolute_level'] = data['web_level'].apply(process_third_value)

existing_data = pd.read_csv('water_level_Uzhgorod_st.csv', header=None, names=['datetime', 'web_level', 'other', 'absolute_level'])

# Вибираємо тільки ті дані, яких немає в існуючому файлі
new_data = data[~data['datetime'].isin(existing_data['datetime'])]

# Додаємо результат до існуючого файлу
with open('water_level_Uzhgorod_st.csv', 'a') as f:
    new_data.to_csv(f, index=False, header=False)
    print(new_data)