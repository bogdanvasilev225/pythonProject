"""
Создайте список чисел и отсортируйте его в порядке убывания.
Создайте список строк и отсортируйте его по длине строк (от самой короткой к самой длинной).
Создайте список кортежей, где каждый кортеж содержит имя и возраст.
 Отсортируйте этот список по возрасту (от старшего к младшему).
Создайте функцию, которая принимает список слов и возвращает новый список,
 содержащий слова, отсортированные в порядке убывания их длины.
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_r = sorted(numbers, reverse=True)
print(numbers_r)

words = ["банан", "апельсин", "клубника", "киви"]
words_sort = sorted(words, key=len)
print(words_sort)


people = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
print(sorted_people)

def sort(value):
    return len(value)
words = ["Богдан", "Кристина", "Николай", "Елена", "Макс"]
words_sort = sorted(words, key=sort, reverse=True)
print(words_sort)

