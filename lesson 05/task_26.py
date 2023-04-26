# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def task():
    print("Задача 26")
    
    def exponent(a, b):
        if b == 0:
            return 1
        return a*exponent(a, b - 1)
    
    
    A_num = int(input("Введите число А: "))
    B_num = int(input("Введите число B: "))
    
    print(f'A = {A_num}; B = {B_num} -> {exponent(A_num, B_num)} <- ({A_num} в степени {B_num})')


   





