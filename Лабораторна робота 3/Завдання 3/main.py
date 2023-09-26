sentence = input("Введіть речення: ")
words = sentence.split()
flag = 0
print("Слова які містять 3 літери 'e': ")
for word in words:
    if word.count('e') == 3:
        print(word)
        flag += 1

if flag == 0:
    print("Не знайдено слів, які містять 3 літери 'e'")