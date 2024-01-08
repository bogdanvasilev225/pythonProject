"""
Создайте строку sentence и выведите её.
Выведите первый символ строки sentence.
Выведите последний символ строки sentence.
Создайте еще одну строку new_sentence и объедините её с sentence.
Используя форматированную строку, создайте строку greeting,
 которая приветствует пользователя по имени и возрасту.
Используя метод replace(), замените все буквы 'a' в строке sentence на 'x'.
"""
sentence = "Bogdan"
print("Вывод строки:", sentence)
print("Вывод первого символа:", sentence[0])
print("Вывод последнего символа:", sentence[-1])

new_sentence = "Vasilev"
combined_sentence = sentence + " " + new_sentence
print("Вывод объедененных строк", combined_sentence)

modified_sentence = sentence.replace('a', 'x')
print("Строка после замены:", modified_sentence)


name = input("Введите имя:")
age = int(input("Введите возраст:"))
greeting = f"Привет, меня зовут {name} мне {age} лет"
print(greeting)



