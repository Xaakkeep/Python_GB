# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

def task():
    print("Задача 18") 
    
    N = abs(int(input('Введите количество элементов списка А: ')))
    
    list_mass = []
    for j in range(N):
        list_mass.append(random.randint(1, 10))

    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min_num = abs(X - list_mass[0])
    index = 0
    for i in range(N):
        count = abs(X - list_mass[i])
        if count < min_num:
            min_num = count
            index = i
    print(f'Массив - {list_mass}\nЧисло {list_mass[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - list_mass[index])}')
    
task()   