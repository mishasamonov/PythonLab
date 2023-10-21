def PrintAllStudents(students):
    for i in students:
        print("Учень:", i, ". Проживає на вулиці:", students[i][0], ". В школі №:", students[i][1], ". Клас:", students[i][2])

def AddNewStudent(students):
    while True:

        name = input("Введіть Ім'я Прізвище учня ")
        if not name.isdigit():
            break
        else:
            print("Ім'я не повинно містити числових знаків! Спробуйте ще раз.")

    while True:

        address = input("Введіть вулицю учня ")
        if not address.isdigit():
            break
        else:
            print("Вулиця не повинна містити числових знаків! Спробуйте ще раз.")

    while True:

        schoolNum = input("Введіть школу учня ")
        if schoolNum.isdigit():
            break
        else:
            print("Ви ввели не числове значення! Спробуйте ще раз.")

    while True:
        classNum = int(input("Введіть клас учня "))
        if classNum == 10 or classNum == 11:
            break
        else:
            print("Клас учня повинен бути 10 або 11! Спробуйте ще раз.")

    students[name] = [address, schoolNum, classNum]
    print("Додано ", name)

def RemoveStudent(students):
    removeName = input("Ведіть ім'я яке бажаєте видалити: ")
    if removeName in students:
        del students[removeName]
        print("Видалено ", removeName)
    else:
        print("Учня в списку не знайдено! Спробуйте, ще раз!")

def PrintSortedList(students):
    students = {k: students[k] for k in sorted(students)}

    print("Відсортований список учнів: ")
    for i in students:
        print("Учень:", i, "-", "Проживає на вулиці:", students[i][0], ". В школі №:", students[i][1], ". Клас:", students[i][2])

def PrintOlderStudents(students):
    print("Список учнів, які навчаються в 11 класі:")

    for i in students:
        if students[i][2] == 11:
            print("Учень:", i, "-", "Проживає на вулиці:", students[i][0], ". В школі №:", students[i][1], ". Клас:", students[i][2])

def PrintYoungerStudents(students):
    print("Список учнів, які навчаються в 10 класі:")

    for i in students:
        if students[i][2] == 10:
            print("Учень:", i, "-", "Проживає на вулиці:", students[i][0], ". В школі №:", students[i][1], ". Клас:", students[i][2])

students = {
    "Misha Samonov": ["Chkalov", 5, 10] ,
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

while True:
    print("\t \t \t \t Меню")
    print("Вивести весь список учнів, натисніть -> 1 <- ")
    print("Додати нового учня до списку, натисніть -> 2 <- ")
    print("Видалити учня зі списку, натисніть -> 3 <- ")
    print("Відсортувати список учнів по алфавіту -> 4 <- ")
    print("Вивести список учнів, які навчаються в 10 класі, натисніть -> 5 <- ")
    print("Вивести список учнів, які навчаються в 11 класі, натисніть -> 6 <- ")
    print("Вийти з меню(завершити роботу програми) -> 7 <- ")
    print()

    choice = int(input("Введіть команду з меню: "))


    if choice == 1:
        PrintAllStudents(students)

    if choice == 2:
        AddNewStudent(students)

    if choice == 3:
        RemoveStudent(students)

    if choice == 4:
        PrintSortedList(students)

    if choice == 5:
        PrintYoungerStudents(students)

    if choice == 6:
        PrintOlderStudents(students)

    if choice == 7:
        break

    if choice > 7:
        print("Команди під таким номером не існує! Спробуйте ще раз.")

    if choice < 1:
        print("Команди під таким номером не існує! Спробуйте ще раз.")


    input("Натисніть Enter щоб продовжити ...")

