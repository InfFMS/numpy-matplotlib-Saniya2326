# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
#
from random import randint
import random
import matplotlib.pyplot as plt

import numpy as np

m =[]
data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

while len(m)!=15:
    a = randint(0,9)
    b = randint(0, 9)
    k =(a,b)

    if k not in m:
        m.append(k)
    data[a][b]=10





for i in range (1,9):
    for j in range(1, 9):
        if data[i][j]==10:
            if data[i][j-1]!=10:
                data[i][j-1]+=1

            if data[i][j + 1] != 10:
                data[i][j + 1] += 1
            if data[i - 1][j + 1] != 10:
                data[i - 1][j + 1] += 1
            if data[i - 1][j] != 10:
                data[i - 1][j] += 1
            if data[i - 1][j - 1] != 10:
                data[i - 1][j - 1] += 1
            if data[i + 1][j] != 10:
                data[i + 1][j] += 1
            if data[i+1][j+1]!=10:
                data[i+1][j+1]+=1
            if data[i+1][j-1]!=10:
                data[i+1][j-1]+=1

for i in range(1,9):
    if data[i][0]==10:
        if data[i][1]!=10:
            data[i][1]+=1
        if data[i-1][0]!=10:
            data[i-1][0]+=1
        if data[i-1][1]!=10:
            data[i-1][1]+=1
        if data[i+1][0]!=10:
            data[i+1][0]+=1
        if data[i+1][1]!=10:
            data[i+1][1]+=1
    if data[i][9]==10:
        if data[i][8]!=10:
            data[i][8]+=1
        if data[i-1][8]!=10:
            data[i-1][8]+=1
        if data[i-1][9]!=10:
            data[i-1][9]+=1
        if data[i+1][8]!=10:
            data[i+1][8]+=1
        if data[i+1][9]!=10:
            data[i+1][9]+=1
    if data[0][i]==10:
        if data[0][i-1]!=10:
            data[0][i-1]+=1
        if data[0][i+1]!=10:
            data[0][i+1]+=1
        if data[1][i-1]!=10:
            data[1][i-1]+=1
        if data[1][i]!=10:
            data[1][i]+=1
        if data[1][i+1]!=10:
            data[1][i+1]+=1
    if data[9][i]==10:
        if data[9][i-1]!=10:
            data[9][i-1]+=1
        if data[9][i+1]!=10:
            data[9][i+1]+=1
        if data[8][i-1]!=10:
            data[8][i-1]+=1
        if data[8][i]!=10:
            data[8][i]+=1
        if data[8][i+1]!=10:
            data[8][i+1]+=1

if data[0][0]==10:
    if data[0][1]!=10:
        data[0][1]+=1
    if data[1][0]!=10:
        data[1][0]+=1

if data[9][0]==10:
    if data[9][1]!=10:
        data[9][1]+=1
    if data[8][0]!=10:
        data[8][0]+=1
if data[0][9]==10:
    if data[0][8]!=10:
        data[0][8]+=1
    if data[1][9]!=10:
        data[1][9]+=1
if data[9][9]==10:
    if data[9][8]!=10:
        data[9][8]+=1
    if data[8][9]!=10:
        data[8][9]+=1


for i in data:
    print (i)

fig = plt.figure(figsize=(10,6))
ax = plt.subplot()

plt.imshow(data, cmap="binary")
for i in range(0,10):
    for j in range(0,10):
        plt.text(j, i, str(data[i][j]), color='red')
        # if data[i][j] == 1:
        #     plt.text(j,i, '1', color='red')
        # if data[i][j] == 2:
        #     plt.text(j, i, '2', color='red')
        # if data[i][j]== 3:
        #     plt.text(j,i, '3', color='red')
        # if data[i][j] == 4:
        #     plt.text(j, i, '4', color='red')
        # if data[i][j] == 5:
        #     plt.text(j,  i,'5', color='red')
        # if data[i][j] == 6:
        #     plt.text(j,i, '6', color='red')
        # if data[i][j] == 7:
        #     plt.text(j, i,'7', color='red')
        # if data[i][j] == 8:
        #     plt.text(j, i,'9', color='red')

        if data[i][j] == 10:
            cil = plt.Circle((j,i), 0.42, color='red')
            ax.add_patch(cil)


plt.show()

