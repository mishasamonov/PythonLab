n = int(input("Введіть число n: "))
while n < 1 or n > 9:
    print("Число повинно бути в межах 1 < n < 9")
    n = int(input("Введіть число n ще раз: "))

for i in range (1, n+1):
    for j in range (i, 0, -1):
        print(j, end = " ")
    print()
