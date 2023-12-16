import matplotlib.pyplot as plt
import numpy as np
import csv

# Модельні дані для України та США (освітні статистики)
years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
ukraine_data = np.array([3178357, 3006419, 2825876, 2646403, 2479822, 2334997, 2215471, 2120701, 2050008, 2000904, 1970807, 1960266, 1968206, 1988065, 2011250, 2031107])
us_data = np.array([345167, 336237, 324000, 309945, 296172, 284246, 274642, 267037, 261225, 256720, 253140, 250517, 248959, 248219, 247969, 247942])

# 2.1 Побудова графіків
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(years, ukraine_data, label='Ukraine', color='purple', marker='o')
plt.plot(years, us_data, label='USA', color='yellow', marker='o')
plt.title('Динаміка показників')
plt.xlabel('Рік')
plt.ylabel('Значення показника')
plt.legend()

# 2.2 Стовпчаста діаграма
plt.subplot(1, 2, 2)
country_name = input("Введіть назву країни (Ukraine або USA): ")
if country_name.lower() == 'ukraine':
    plt.bar(years, ukraine_data, color='purple')
elif country_name.lower() == 'usa':
    plt.bar(years, us_data, color='yellow')
else:
    print("Невірна назва країни")

plt.title(f'Значення показника для {country_name}')
plt.xlabel('Рік')
plt.ylabel('Значення показника')

plt.tight_layout()

# Збереження графіків у зображення
plt.savefig('education_statistics_plot.png')
plt.show()

# Збереження даних у CSV-файл
file_path = 'education_statistics_data.csv'
with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Запис заголовків
    csv_writer.writerow(['Year', 'Ukraine', 'USA'])

    # Запис даних
    for year, ukraine_val, us_val in zip(years, ukraine_data, us_data):
        csv_writer.writerow([year, ukraine_val, us_val])

print(f"Дані та графіки збережено у файли: {file_path}, education_statistics_plot.png")
