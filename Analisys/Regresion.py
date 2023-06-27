import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Дані про станції
data = [
    {"id": 11, "voda_1": 1930, "voda_5": 1400, "voda_10": 1175, "voda_25": 870, "ploshcha": 1970},
    {"id": 44, "voda_1": 1390, "voda_5": 1010, "voda_10": 855, "voda_25": 656, "ploshcha": 1280},
    {"id": 29, "voda_1": 705, "voda_5": 502, "voda_10": 424, "voda_25": 320, "ploshcha": 653},
    {"id": 30, "voda_1": 372, "voda_5": 260, "voda_10": 215, "voda_25": 160, "ploshcha": 286}
]

# Виділення даних
voda_1 = [item["voda_1"] for item in data]
voda_5 = [item["voda_5"] for item in data]
voda_10 = [item["voda_10"] for item in data]
voda_25 = [item["voda_25"] for item in data]
ploshcha = [item["ploshcha"] for item in data]

# Конвертація в numpy arrays
X = np.array(ploshcha).reshape(-1, 1)
y_1 = np.array(voda_1)
y_5 = np.array(voda_5)
y_10 = np.array(voda_10)
y_25 = np.array(voda_25)

# Побудова моделі лінійної регресії
model_1 = LinearRegression()
model_1.fit(X, y_1)

model_5 = LinearRegression()
model_5.fit(X, y_5)

model_10 = LinearRegression()
model_10.fit(X, y_10)

model_25 = LinearRegression()
model_25.fit(X, y_25)

# Візуалізація результатів
plt.figure(figsize=(10, 6))

plt.scatter(ploshcha, voda_1, color='b', label='1%')
plt.scatter(ploshcha, voda_5, color='g', label='5%')
plt.scatter(ploshcha, voda_10, color='r', label='10%')
plt.scatter(ploshcha, voda_25, color='c', label='25%')

plt.plot(X, model_1.predict(X), color='b', linestyle='--')
plt.plot(X, model_5.predict(X), color='g', linestyle='--')
plt.plot(X, model_10.predict(X), color='r', linestyle='--')
plt.plot(X, model_25.predict(X), color='c', linestyle='--')

plt.xlabel('Водозбірна площа')
plt.ylabel('Витрати води')
plt.title('Залежність витрат води від водозбірної площі')
plt.legend()

plt.show()