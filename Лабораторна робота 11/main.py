import csv
import os

def find_exports(csv_file, output_file):
    flag = False

    try:
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')

            # Вивід заголовків
            print("Country Name: 2015 [YR2015] 2016 [YR2016] 2017 [YR2017] 2018 [YR2018] 2019 [YR2019]")

            for row in reader:
                # Вивід інформації за вказані роки
                print(row['Country Name'], ':', row['2015 [YR2015]'], row['2016 [YR2016]'], row['2017 [YR2017]'], row['2018 [YR2018]'], row['2019 [YR2019]'])

            # Повертаємо файловий об'єкт на початок для повторного читання
            csvfile.seek(0)
            next(reader)  # Пропускаємо заголовок

            indicator = input("\nВведіть назви країн (через кому), для яких ви хочете знайти показники: ")
            countries_to_search = [country.strip() for country in indicator.split(',')]

            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile2:
                writer = csv.writer(csvfile2, delimiter=',')

                # Запис результатів пошуку у новий .csv файл
                writer.writerow(["Country Name", "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2018 [YR2018]", "2019 [YR2019]"])

                for row in reader:
                    if row['Country Name'] in countries_to_search:
                        writer.writerow([row['Country Name'], row['2015 [YR2015]'], row['2016 [YR2016]'], row['2017 [YR2017]'], row['2018 [YR2018]'], row['2019 [YR2019]']])
                        flag = True

                if not flag:
                    print(f"\nДля жодної з введених країн не знайдено показників за 2015-2019 роки.")

            print(f"\nРезультати пошуку збережено у файлі {output_file}")

    except FileNotFoundError:
        print(f"Файл {csv_file} не знайдено!")

if __name__ == "__main__":
    # Вхідні дані
    csv_file_path = "ExportsGDP2015-2019_updated.csv"
    output_file_path = "result.csv"

    # Виклик функції для знаходження та запису результатів
    find_exports(csv_file_path, output_file_path)
