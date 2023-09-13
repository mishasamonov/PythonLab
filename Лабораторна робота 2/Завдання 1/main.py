from cmath import sin
def finding():
    z = sin(a+b) * sin(a-b)
    return z
def sportsmanNorma(M,K):
    M = (M * K / 100) + M
    return M

a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))

print("Значення виразу z = ", finding())


day = 1
M = float(input("Введіть скільки кілометрів пробігає спортсмен в 1-й день: "))
K = float(input("Введіть відсоток з яким буде збільшено норму пробігу спортсмена: "))

while M < 50:
    day += 1
    M = sportsmanNorma(M,K)

print("Норма пробігу спортсмена становить більше 50км через: ", day, " днів")





