import random

mainStack = []
def randomNumber():
    return random.randint(1, 1000)

for i in range(126):
    mainStack.append(randomNumber())

parniStack = []
neParniStack = []

for number in mainStack:
    if number % 2 == 0:
        parniStack.append(number)
    else:
        neParniStack.append(number)

print("Головний стек: ", mainStack)

print("Елементи парного стеку: ")
for number in parniStack:
    print(number)

print()

print("Елементи непарного стеку: ")
for number in neParniStack:
    print(number)