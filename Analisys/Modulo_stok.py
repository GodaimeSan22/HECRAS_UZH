import matplotlib.pyplot as plt

data = [
    {"id": 11, "voda_1": 1930, "voda_5": 1400, "voda_10": 1175, "voda_25": 870, "ploshcha": 1970},
    {"id": 44, "voda_1": 1390, "voda_5": 1010, "voda_10": 855, "voda_25": 656, "ploshcha": 1280},
    {"id": 29, "voda_1": 705, "voda_5": 502, "voda_10": 424, "voda_25": 320, "ploshcha": 653},
    {"id": 30, "voda_1": 372, "voda_5": 260, "voda_10": 215, "voda_25": 160, "ploshcha": 286}
]

ids = []
voda_ploshcha_1 = []
voda_ploshcha_5 = []
voda_ploshcha_10 = []
voda_ploshcha_25 = []

for item in data:
    id = item["id"]
    voda_1 = item["voda_1"]
    voda_5 = item["voda_5"]
    voda_10 = item["voda_10"]
    voda_25 = item["voda_25"]
    ploshcha = item["ploshcha"]

    voda_ploshcha_1.append(voda_1 / ploshcha)
    voda_ploshcha_5.append(voda_5 / ploshcha)
    voda_ploshcha_10.append(voda_10 / ploshcha)
    voda_ploshcha_25.append(voda_25 / ploshcha)
    ids.append(id)

# Побудова діаграми
x = range(len(ids))
width = 0.2

plt.bar(x, voda_ploshcha_1, width, label='1% павідень')
plt.bar([i + width for i in x], voda_ploshcha_5, width, label='5% павідень')
plt.bar([i + 2 * width for i in x], voda_ploshcha_10, width, label='10% павідень')
plt.bar([i + 3 * width for i in x], voda_ploshcha_25, width, label='25% павідень')

plt.xlabel('ID')
plt.ylabel('Співвідношення витрат до площі')
plt.title('Співвідношення витрат повені до площі водозбірних басейнів')
plt.xticks([i + 1.5 * width for i in x], ids)
plt.legend()

plt.show()