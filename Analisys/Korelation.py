import numpy as np

# Дані станцій: ідентифікатор, витрати води при різних рівнях (наприклад, 1%, 5%, 10%, 25%)
data = [
    {"id": 11, "voda_1": 1930, "voda_5": 1400, "voda_10": 1175, "voda_25": 870, "ploshcha": 1970},
    {"id": 44, "voda_1": 1390, "voda_5": 1010, "voda_10": 855, "voda_25": 656, "ploshcha": 1280},
    {"id": 29, "voda_1": 705, "voda_5": 502, "voda_10": 424, "voda_25": 320, "ploshcha": 653},
    {"id": 30, "voda_1": 372, "voda_5": 260, "voda_10": 215, "voda_25": 160, "ploshcha": 286}]

# Витягування даних в окремі списки
ids = [station["id"] for station in data]
voda_1 = [station["voda_1"] for station in data]
voda_5 = [station["voda_5"] for station in data]
voda_10 = [station["voda_10"] for station in data]
voda_25 = [station["voda_25"] for station in data]
ploshcha = [station["ploshcha"] for station in data]

# Обчислення кореляції для різних рівнів витрат води
correlation_1 = np.corrcoef(voda_1, ploshcha)[0, 1]
correlation_5 = np.corrcoef(voda_5, ploshcha)[0, 1]
correlation_10 = np.corrcoef(voda_10, ploshcha)[0, 1]
correlation_25 = np.corrcoef(voda_25, ploshcha)[0, 1]

# Виведення результатів
print("Коефіцієнт кореляції для 1% витрати води:", correlation_1)
print("Коефіцієнт кореляції для 5% витрати води:", correlation_5)
print("Коефіцієнт кореляції для 10% витрати води:", correlation_10)
print("Коефіцієнт кореляції для 25% витрати води:", correlation_25)
import matplotlib.pyplot as plt

# Код для отримання даних та обчислення кореляції (як описано в попередньому прикладі)

# Візуалізація кореляції
plt.figure(figsize=(10, 6))

plt.scatter(ploshcha, voda_1, color='b', label='1%')
plt.scatter(ploshcha, voda_5, color='g', label='5%')
plt.scatter(ploshcha, voda_10, color='r', label='10%')
plt.scatter(ploshcha, voda_25, color='c', label='25%')

plt.xlabel('Водозбірна площа')
plt.ylabel('Витрати води')
plt.title('Кореляція між водозбірною площею та витратами води')
plt.legend()

plt.show()