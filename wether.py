# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.

import matplotlib.pyplot as plt

import numpy as np
x = []
v = []
n = []
m =[]
import random
from random import randint
b = 0
j = 0
w = 0
p =[]
for i in range (1, 366):
    a = randint(-10, 35)
    if a > 0:
        plt.scatter(i, a, color='red')
    if a > 25:
        j +=1
    b = b+a
    m.append(a)

for i in range(1, 365):
    if m[i]<0 and m[i-1]<0:

        x.append(m[i])


for i in range(-10,36):


    p.append(m.count(i))




print((b+a)/365, len(x), p)

for i in range (1, 366):
    n.append(i)


q = []
for i in range (-10, 36):
    q.append(i)



fig, axs = plt.subplots(1, 2, figsize=(10,4))
axs[0].plot(n, m, color='#2e264a')
axs[0].set_title('Погода')
axs[0].set_xlabel('Дни')
axs[0].set_ylabel('Градусы')

axs[1].bar(q,p)
axs[1].set_title('Распределение жарких дней')
axs[1].set_ylabel('Количество дней')
axs[1].set_xlabel('Градусы')

plt.show()