# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.


import matplotlib.pyplot as plt

import numpy as np


x =[]
a1 = 0
b1 =0
a2 = 0
b2 = 0
a3 = 0
b3 = 0
a4 = 0
b4 = 0
a5 = 0
b5 = 0
a6 = 0
b6 = 0

m =[]
import random
from random import randint


for i in range (1,1001):
    a = randint(1, 6)
    m.append(a)
    if a == 1:
        a1 +=1
    if a == 2:
        a2 += 1
    if a == 3:
        a3 += 1
    if a == 4:
         a4 += 1
    if a == 5:
        a5 += 1
    if a == 6:
        a6 += 1
d = m[0]
for i in range(0, 999):
    if d == m[i+1]:
        b1+=1
    else:
        d = m[i+1]
        x.append(b1)
        b1=0
s = max(x)

print('1:',a1/1000, '2:', a2/1000, '3:', a3/1000,  '4:',a4/1000, '5:', a5/1000, '6:', a6/1000, 'Количество повторов:',s)

v = ['1', '2','3', '4', '5','6']
n = [a1, a2, a3, a4, a5,a6]

plt.bar(v, n, color='#33CCCC' )
plt.xlabel("Значение")
plt.ylabel("Коичество бросков")

plt.title('КУБИК')
plt.show()