"""
Цикл For и строки:

Создайте строку "Python".
Используя цикл for, выведите каждую букву строки, а затем ее индекс в строке.
"""
string = "Python"
for index, char in enumerate(string):
    print(f"Index: {index}, Character: {char}")
