# Задача 8: 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

def task():
    print("Задача 8")
    n = int(input("Введите длину шоколадки: "))
    m = int(input("Введите ширину шоколадки: "))
    k = int(input("Количество долек: "))
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print(f'Длина[{n}] Ширина[{m}] Количество долек[{k}] -> YES')
    else:
        print(f'Длина[{n}] Ширина[{m}] Количество долек[{k}] -> NO')
