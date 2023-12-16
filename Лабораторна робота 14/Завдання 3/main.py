import numpy as np
import matplotlib.pyplot as plt
import csv

# Зчитуємо дані з CSV файлу
csv_file = "ExportsGDP2015-2019_updated.csv"

# Користувач вводить рік
year = input("Введіть рік (наприклад, '2015 [YR2015]'): ")

with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    header = next(reader)  # Читаємо заголовок

    # Витягуємо дані з рядка
    countries, data = zip(*[(row['Country Name'], float(row[year])) for row in reader if row[year] != '..'])

# Конвертуємо списки у numpy arrays
countries = np.array(countries)
data = np.array(data)

# Графік
fig, ax = plt.subplots()
ax.pie(data, labels=countries, autopct='%1.1f%%')
ax.axis("equal")

plt.title(f"Exports GDP {year}")
plt.show()
