import pandas as pd

# Словник з лабораторної роботи №6
students = {
    "Misha Samonov": ["Chkalov", 5, 10],
    "Dima Medvid": ["Peremohy", 7, 11],
    "Sasha Krypskiy": ["Kyrska", 1, 10],
    "Anna Vasilenko": ["Jovtneva", 8, 11],
    "Misha Kolpakov": ["Malinovy", 4, 11],
    "Anastasia Ivanko": ["Sumy", 15, 10],
    "Artur Sachek": ["Muratov", 45, 11],
    "Ivan Bondarev": ["Sluvovy", 12, 11],
    "Jenya Herasymenko": ["Miry", 22, 10],
    "Kiril Hrolenko": ["Rebrov", 41, 11]
}

# Перетворення словника в датафрейм
df_students = pd.DataFrame(students).T
df_students.columns = ["Вулиця", "Школа №", "Клас"]

# Виведення датафрейму на екран
print("Датафрейм учнів:")
print(df_students)

# Агрегація і групування даних
grouped_data = df_students.groupby("Клас").agg({"Школа №": ["count", "min", "max"]})

# Виведення результату групування на екран
print("\nГрупування та агрегація:")
print(grouped_data)
