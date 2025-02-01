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
[0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 1, 0, 1, 0]
]


f = randint(0,7)
x = randint(0,7)
k = (f, x)
data[f][x]=0.056

for i in range (0,8):
    data[f][i]=0.553
    data[i][x]=0.553

a=x
b=f

c=f
d=x

e=f
r=x
m=f
n=x


while f !=0 and x!=7:
    data[f-1][x+1]=0.553
    f = f-1
    x = x+1

while b !=0 and a!=0:
    data[b-1][a-1]=0.553
    a = a-1
    b = b-1

while c != 7 and d != 7:
    data[c + 1][d + 1] = 0.553
    d = d + 1
    c = c + 1

while e != 7 and r != 0:
    data[e + 1][r - 1] = 0.553
    e = e + 1
    r = r - 1

fig, ax = plt.subplots()
data[m][n]=0.056



plt.imshow(data, cmap='gist_stern')
plt.xticks(range(8), labels=[i for i in 'ABCDEFGH'])
plt.yticks(range(8), labels=[i for i in range (8, 0, -1)])
print("Клетка, в которой находится ферзь", k)

plt.show()