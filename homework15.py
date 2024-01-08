"""
Создайте два множества set1 и set2 с разными элементами.
Добавьте элемент в set1.
Удалите элемент из set2.
Проверьте наличие элемента в set1.
Объедините set1 и set2 в новое множество combined_set.
Найдите пересечение set1 и set2 в новом множестве intersection_set.
Найдите разность set1 и set2 в новом множестве difference_set.
"""
#двас пособа создания множества
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8}

set1.add(6)
set2.remove(6)

print("Проверка наличия добленного элемента:", *set1)

combined_set = set1 | set2
print("Вывод объедененных множеств:", *combined_set)

intersection_set = set1 & set2
print("Пересечение set1 и set2 в новом множестве:", *intersection_set)

difference_set = set1 - set2
print("Разность множеств", *difference_set)

