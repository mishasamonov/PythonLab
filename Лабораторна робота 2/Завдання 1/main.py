start = 5
end = 25
a, b = 1, 1

# Пропускаємо перші 4 числа Фібоначчі
for i in range(start - 1):
    a, b = b, a + b

# Виводимо ряд Фібоначчі від 5-го до 25-го члена і підраховуємо кількість чисел
print("Ряд Фібоначчі з {}-го до {}-го члена:".format(start, end))
count = 0
for i in range(start, end):
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print("\nКількість чисел у ряді:", count)