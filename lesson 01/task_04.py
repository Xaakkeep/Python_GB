# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


def task():
    print("Задача 4")
    num = int(input("Введите число: "))
    temp = num % 3
    if temp == 0:
        num1 = num / 3
        girl = int(num - num1)
        man = int(num1 / 2)
        print(f'{num} -> {man} {girl} {man}')
        
    else:
        print("Условие задачи не выполнено")
