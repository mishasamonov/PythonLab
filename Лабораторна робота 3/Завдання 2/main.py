s = str(input("Введіть будь-яке слово: "))

sum = 0

for i in range(len(s)):
    sum += ord(s[i])

print("Сума ASСII кодів символів слова = ", sum)