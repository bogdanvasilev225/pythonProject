"""
Создайте двумерный список, представляющий собой матрицу 4x4, и заполните его числами от 1 до 16.
Напишите код, который выведет сумму каждой строки в вашей матрице.
Создайте функцию, которая принимает двумерный список и возвращает сумму всех его элементов.
"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print(f"Сумма равна: {sum(row)}")

def sum_of_matrix(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum

# Пример использования
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

result = sum_of_matrix(matrix)
print(result)




