"""
Создайте функцию calculate_sum, которая принимает два числа и возвращает их сумму.
Создайте функцию is_even, которая принимает число и возвращает True, если оно четное,
и False в противном случае.
Создайте функцию print_info, которая принимает имя, возраст и город,
и выводит информацию о человеке.
Создайте функцию find_max, которая принимает список чисел и возвращает максимальное из них.
Создайте функцию reverse_string, которая принимает строку и возвращает ее в обратном порядке.
"""

def calculate_sum(x, y):
    result = x + y
    return result
# Пример вызова функции
x = 5
y = 6
sum_result = calculate_sum(x, y)
print(f"Сумма чисел {x} и {y} равна: {sum_result}")

def is_even(x):
    if x % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"

x = 4
result = is_even(x)
print(f"Число {x} {result}")

def print_info(name, age, city):
    man = name, age, city
    return man
name = "Bogdan"
age = 30
city = "Moscow"
man_info = print_info(name, age, city)

print(f"Hello, my name is {man_info[0]}."
      f" I am {man_info[1]} years old, and I live in {man_info[2]}")

def print_info(name, age, city):
    print(f"Hello, my name is {name}. I am {age} years old, and I live in {city}")

print_info("Bogdan", 30, "Moscow")

def find_max(numbers):
    return max(numbers)
numbers_list = [1, 2, 3, 4, 5, 6, 7]
result = find_max(numbers_list)
print(f"Максимальное число {result}")

def reverse_string(s):
    return s[::-1]

input_string = "Bogdan"
result = reverse_string(input_string)
print(result)


