# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из
# 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.


from random import randint
import random
import matplotlib.pyplot as plt

import numpy as np
fig, ax = plt.subplots()
x =10
y =10
a = 0
b = 0
x1 =(0,0)
c1 = plt.Circle((0, 0), 0.1, color= 'red')



plt.grid(True)
x1 =(b,a)
c1 = plt.Circle((0, 0), 0.1, color= 'red')
ax.add_patch(c1)

f ="вверх"
g ='вниз'
h='влево'
j='вправо'

q = [f, g, h, j]
w = []
r =[]
for i in range(0,100):
    n = random.choice(q)
    if n == f:
        plt.plot([0,0],[0,1])
    if n == g:
        plt.plot([0,0],[0,-1])
    if n == h:
        plt.plot([0, 1],[0,0])
    if n == j:
        plt.plot([0,-1],[0,0])



plt.show()
