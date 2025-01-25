# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
from random import randint
import random
import matplotlib.pyplot as plt

import numpy as np

data = [
[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],
[0.01,0, 1, 0, 1, 0, 1, 0, 1, 0.01],
[0.01,1, 0, 1, 0, 1, 0, 1, 0, 0.01],
[0.01,0, 1, 0, 1, 0, 1, 0, 1, 0.01],
[0.01,1, 0, 1, 0, 1, 0, 1, 0, 0.01],
[0.01,0, 1, 0, 1, 0, 1, 0, 1, 0.01],
[0.01,1, 0, 1, 0, 1, 0, 1, 0, 0.01],
[0.01,0, 1, 0, 1, 0, 1, 0, 1, 0.01],
[0.01,1, 0, 1, 0, 1, 0, 1, 0, 0.01],
[0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
]

f = randint(0,7)
x = randint(0,7)
k = (f, x)








plt.imshow(data, cmap='hot')

print("Клетка, в которой находится ферзь", k)

plt.show()