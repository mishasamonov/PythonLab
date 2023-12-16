import matplotlib.pyplot as plt
import numpy as np

# Створення масиву значень x від 0 до 4 з кроком 0.01 (або інший крок за необхідності)
x = np.linspace(0, 4, 400)

# Обчислення значень функції Y(x) = 5*sin(10*x)*sin(3*x)
y = 5 * np.sin(10 * x) * np.sin(3 * x)

# Побудова графіка з заданими параметрами
plt.plot(x, y, label='5*sin(10*x)*sin(3*x)', color='blue', linewidth=2, linestyle='solid')

# Додавання заголовка графіка
plt.title('Графік функції Y(x) = 5*sin(10*x)*sin(3*x)', fontsize=15)

# Позначення осі абсцис
plt.xlabel('x', fontsize=12, color='blue')

# Позначення осі ординат
plt.ylabel('Y(x)', fontsize=12, color='blue')

# Вставка легенди
plt.legend()

# Активація сітки
plt.grid(True)

# Виведення графіка
plt.show()
