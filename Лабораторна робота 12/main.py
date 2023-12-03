import json

def add_student(data):
    print("Add student:")
    Surname = input("Surname:")
    Name = input("Name:")
    Adress = input("Adress:")
    while True:
        try:
            School = int(input("School:"))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            Class = int(input("Class:"))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    Day_of_week = input("Day of the week (Saturday or Sunday):")
    while Day_of_week.lower() not in ["saturday", "sunday"]:
        print("Invalid day. Please enter either Saturday or Sunday.")
        Day_of_week = input("Day of the week (Saturday or Sunday):")

    data.append({"Surname": Surname, "Name": Name, "Adress": Adress, "School": School, "Class": Class, "Day_of_week": Day_of_week})
    return data

def find_younger_students(data):
  result = [
      {"Surname": student["Surname"], "Name": student["Name"], "Adress": student["Adress"]}
      for student in data
      if student["Class"] in [7, 8] and student.get("Day_of_week", "").lower() == "saturday"
  ]

  if not result:
      print("No students found.")

  return result


# Load existing data from the file
try:
    with open("data.json", "rt") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []

while True:
    print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find younger students attending on Saturdays\n 4 - Exit")
    try:
        x = int(input("Choose an option:\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if x == 1:
        students = add_student(students)
        with open("data.json", "wt") as file:
            json.dump(students, file)

    elif x == 2:
        with open("data.json", "rt") as file:
            students = json.load(file)
            print(*students, sep='\n')

    elif x == 3:
        with open("data.json", "rt") as file:
            students = json.load(file)
            result = find_younger_students(students)
            print(*result, sep='\n')

    elif x == 4:
        quit(0)

    else:
        print("Invalid option. Please choose a number between 1 and 4.")

    input("Press Enter to continue...")
