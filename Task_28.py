# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 

a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))


def recursive_sum(a, b):
    if b != 0:
        if a > b:  # выбор минимального числа для оптимизации    
            return recursive_sum(a + 1, b - 1) 
        else:
            return recursive_sum(b + 1, a - 1)
    return a
    
       





print(recursive_sum(a, b))