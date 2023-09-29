n = int(input("Введіть розмір масиву, n = "))
arr = []
sum = 0

print(f"Введіть елементи масиву({n}): ")

for i in range(n):
    num = int(input())
    arr.append(num)

for num in arr:
    if num > 0 and num % 3 == 0:
        sum += num
print("Сума додатніх елементів кратних трьом = ", sum)


