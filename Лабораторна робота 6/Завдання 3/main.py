def addVowelsToSet(inputSet):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    inputSet.update(vowels)

c = input('Введіть значення c: ')
d = input('Введіть значення d: ')
# Початкова множина
mySet = {c,d}

# Виклик функції, щоб додати голосні літери
addVowelsToSet(mySet)

# Вивід оновленої множини
print(mySet)
