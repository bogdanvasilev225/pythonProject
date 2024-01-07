"""
Создайте две переменные num1 и num2 и присвойте им значения.
Используя операторы сравнения, выведите результаты следующих выражений:
num1 равно num2?
num1 не равно num2?
num1 меньше num2?
num1 больше или равно num2?
"""
num1 = int(input("Введите целое число:"))
num2 = int(input("Введите целое число:"))
a = num1 == num2
b = num1 != num2
c = num1 < num2
d = num1 >= num2
print("num1 == num2:", a)
print("num1 != num2:", b)
print("num1 < num2:", c)
print("num1 >= num2:", d)