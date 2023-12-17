import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calendar

# Зчитуємо дані
data = pd.read_csv("comptagevelo2011.csv")

# Конвертуємо стовпець "Date" у формат дати з рядка у форматі "%d/%m/%Y"
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")

# Створюємо графік для кожної велодоріжки
plt.figure(figsize=(10, 5))
for column in ["Rachel / Papineau", "Berri1", "Maisonneuve_1", "Maisonneuve_2", "Brébeuf", "Parc",
               "CSC (Côte Sainte-Catherine)", "PierDup"]:
    plt.plot(data["Date"], data[column], label=column)

plt.title('Загальна популярність велодоріжок за кожен день')
plt.xlabel('Дата')
plt.ylabel('Популярність')

# Змінюємо формат позначень на осі x, щоб відображалися назви місяців
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

plt.legend()
plt.grid(True)
plt.show()

# Конвертуємо стовпець "Date" у формат дати з рядка у форматі "%d/%m/%Y" та додаємо стовпець місяця
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
data["Month"] = data["Date"].dt.month

# Обчислюємо загальну популярність велодоріжок у кожному місяці, знаходимо найпопулярніший місяць загалом
sum_total = data.groupby("Month")[["Rachel / Papineau", "Berri1","Maisonneuve_1", "Maisonneuve_2", "Brébeuf", "Parc",
                                   "CSC (Côte Sainte-Catherine)", "PierDup"]].sum().sum(axis=1)
most_popular_month_in_total = sum_total.idxmax()

print(f"\nНайпопулярніший місяць у велосипедистів: {calendar.month_name[most_popular_month_in_total]} з кількістю : {sum_total.max()}")
