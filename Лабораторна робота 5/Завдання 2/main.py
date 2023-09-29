rows = 7
columns = 7
temp = 0

for i in range(rows):
    for j in range(columns-i, columns):
        print(j, end = "  ")
    for k in range(columns, temp, -1):
        print(k, end = "  ")

    temp += 1
    print()