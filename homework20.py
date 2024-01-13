"""
Создайте двумерный список, представляющий собой таблицу умножения от 1 до 5.
Выведите эту таблицу в удобочитаемом формате.
"""

# Создание матрицы
matrix = []
for i in range(1, 6):
    row = []  # Создаем пустую строку для каждого числа
    for j in range(1, 6):
        row.append(i * j)  # Заполняем строку результатами умножения
    matrix.append(row)  # Добавляем строку в матрицу

# Вывод матрицы
for row in matrix:
    print(row)



"""
Напишите функцию transpose(matrix), которая принимает на вход двумерный список (матрицу) и возвращает транспонированную матрицу. 
Транспонированная матрица получается путем замены строк на столбцы (первая строка становится первым столбцом, вторая строка - вторым столбцом и так далее).
"""

# Создание матрицы
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Создание новой матрицы для транспонирования
transposed_matrix = []
for i in range(len(original_matrix[0])):
    new_row = []  # Создаем пустую строку для каждого столбца
    for row in original_matrix:
        new_row.append(row[i])  # Заполняем строку элементами из столбца
    transposed_matrix.append(new_row)  # Добавляем строку в новую матрицу

# Вывод исходной и транспонированной матриц
print("Исходная матрица:")
for row in original_matrix:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed_matrix:
    print(row)

"""
Создайте двумерный список, представляющий собой шахматную доску размером 8x8. 
Заполните его символами "X" и "O" для представления шахматной раскраски. 
Выведите шахматную доску на экран.
"""
# Создание матрицы
chess_board = []
for i in range(8):
    row = []  # Создаем пустую строку для каждой строки доски
    for j in range(8):
        if (i + j) % 2 == 0:
            row.append("X")  # Добавляем "X" для четных ячеек
        else:
            row.append("O")  # Добавляем "O" для нечетных ячеек
    chess_board.append(row)  # Добавляем строку в матрицу

# Вывод шахматной доски
for row in chess_board:
    print(row)

"""
Напишите функцию find_max(matrix), которая принимает на вход двумерный список (матрицу) и возвращает максимальный элемент в этой матрице.
"""
# Инициализация переменной
max_value = float('-inf')

# Поиск максимального элемента
for row in matrix:
    for element in row:
        if element > max_value:
            max_value = element  # Обновляем максимальное значение, если находим больший элемент

# Вывод максимального элемента
print(max_value)


"""
Создайте двумерный список, представляющий собой календарь на месяц. 
Заполните его днями месяца, используя числа от 1 до 31. 
Выведите календарь на экран, разделяя недели и обозначая текущий день (например, выделением цветом).
"""

# Создание матрицы
calendar = []
days_in_month = 31  # Пример, для упрощения возьмем месяц с 31 днем

for i in range(6):
    row = []  # Создаем пустую строку для каждой строки календаря
    for j in range(7):
        day = i * 7 + j + 1
        if day <= days_in_month:
            row.append(day)  # Заполняем строку числами от 1 до 31
        else:
            row.append(" ")  # Если день выходит за пределы месяца, добавляем пустую ячейку
    calendar.append(row)  # Добавляем строку в матрицу

# Вывод календаря
for row in calendar:
    print(row)