import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Завантаження даних
data = {
    'Назва станції': ['Уж-Жорнава', 'Уж - Зарічово', 'Тур\'я - Сімер', 'Уж - Ужтород'],
    'Середньорічна витрата': [79.3, 247.9, 102.1, 341],
    'Водозбірна площа': [286, 1280, 540, 1970]
}

df = pd.DataFrame(data)

# Обчислення кореляції
correlation = df['Середньорічна витрата'].corr(df['Водозбірна площа'])
mean_line_slope = correlation * (df['Середньорічна витрата'].std() / df['Водозбірна площа'].std())

# Графік розсіювання
sns.scatterplot(data=df, x='Водозбірна площа', y='Середньорічна витрата')
plt.title('Залежність Середньорічної витрати від Водозбірної площі')

# Додавання тексту з коефіцієнтом кореляції
plt.text(df['Водозбірна площа'].max(), df['Середньорічна витрата'].min(),
         f"Кореляція: {correlation:.2f}", verticalalignment='bottom', horizontalalignment='right')

# Додавання лінії середніх показників
plt.axline((df['Водозбірна площа'].mean(), df['Середньорічна витрата'].mean()),
           slope=mean_line_slope, color='r', linestyle='--')

# Додавання назв станцій
for i in range(len(df)):
    plt.text(df['Водозбірна площа'][i], df['Середньорічна витрата'][i], df['Назва станції'][i], verticalalignment='bottom', horizontalalignment='right')

plt.show()
