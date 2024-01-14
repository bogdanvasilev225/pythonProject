
"""
Факториал:
Напишите рекурсивную функцию для вычисления факториала числа.
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(6)
print(result)

"""
Сумма чисел:
Напишите рекурсивную функцию для вычисления суммы первых n натуральных чисел.
"""

def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

result = sum_n(4)
print(result)


"""
Числа Фибоначчи:
Напишите рекурсивную функцию для вычисления числа Фибоначчи для 
заданного индекса n в последовательности (последовательность начинается с 0, 1, 1, 2, 3, 5, ...).
"""
def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

result = fib(10)
print(result)

"""
Возведение в степень:
Напишите рекурсивную функцию для вычисления степени числа. Функция должна принимать два аргумента: основание и показатель степени.
"""

def power(n, b):
    if b == 0:
        return 1
    else:
        return n * power(n, b - 1)


result = power(5, 5)
print(result)


"""
Палиндром:
Напишите рекурсивную функцию, которая проверяет, 
является ли заданная строка палиндромом (читается одинаково слева направо и справа налево).
"""
def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

result = palindrome("шалаш")
print(result)