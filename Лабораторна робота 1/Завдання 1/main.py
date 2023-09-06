a = int(input("Введіть число a: "))

while a < 0 :
    print("Число a повинно бути більше за 0!")
    a = int(input("Введіть ще раз число a: "))

b = int(input("Введіть число b: "))

while b < 0 :
    print("Число b повинно бути більше за 0!")
    b = int(input("Введіть ще раз число b: "))

if a > b :
    result = a * b + 21

elif a == b :
    result = -5

else:
    result = 3 * a / b + 1

print("Результат виразу X: " , result)
