"""Цикл While:

Создайте переменную number и присвойте ей значение 1.
Используя цикл while, выведите квадраты чисел от 1 до 5 (1, 4, 9, 16, 25).
"""
number = 1
while number <= 5:
    square = number ** 2
    print("Число:", number, ",возведенное во вторую степень равно:", square)
    number += 1

