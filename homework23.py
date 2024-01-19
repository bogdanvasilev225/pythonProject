import time

def timer(func):  # Определение декоратора
    def wrapper(*args, **kwargs):  # Внутренняя функция декоратора
        start_time = time.time()  # Засекаем время начала выполнения функции
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        end_time = time.time()  # Засекаем время окончания выполнения функции
        print(f"Время выполнения {func.__name__}: {end_time - start_time} секунд")  # Выводим результат
        return result  # Возвращаем результат выполнения оригинальной функции
    return wrapper  # Возвращаем внутреннюю функцию как результат декоратора

@timer  # Применяем декоратор к функции
def slow_function():  # Оригинальная функция
    time.sleep(2)  # Имитация долгой операции
    print("Функция выполнена")

slow_function()  # Вызываем декорированную функцию



def repeat(n):  # Определение декоратора с параметром
    def decorator(func):  # Внутренняя функция декоратора, принимающая оригинальную функцию
        def wrapper(*args, **kwargs):  # Внутренняя функция, заменяющая вызов оригинальной функции
            for _ in range(n):  # Повторяем вызов оригинальной функции n раз
                func(*args, **kwargs)
        return wrapper  # Возвращаем внутреннюю функцию как результат декоратора
    return decorator  # Возвращаем внутреннюю функцию как результат внешней функции декоратора

@repeat(3)  # Применяем декоратор с параметром к функции
def say_hello():  # Оригинальная функция
    print("Привет!")

say_hello()  # Вызываем декорированную функцию


def log(func):  # Определение декоратора
    def wrapper(*args, **kwargs):  # Внутренняя функция декоратора
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию и сохраняем результат
        with open("log.txt", "a") as f:  # Открываем файл лога для добавления информации
            f.write(f"Вызвана функция {func.__name__} с аргументами {args} и ключевыми аргументами {kwargs}\n")  # Записываем информацию в лог
        return result  # Возвращаем результат выполнения оригинальной функции
    return wrapper  # Возвращаем внутреннюю функцию как результат декоратора

@log  # Применяем декоратор к функции
def add(a, b):  # Оригинальная функция
    return a + b  # Возвращаем сумму аргументов

add(3, 5)  # Вызываем декорированную функцию


def logged(message):  # Определение декоратора с параметром
    def decorator(func):  # Внутренняя функция декоратора, принимающая оригинальную функцию
        def wrapper(*args, **kwargs):  # Внутренняя функция, заменяющая вызов оригинальной функции
            with open("log.txt", "a") as f:  # Открываем файл лога для добавления информации
                f.write(f"{message}\n")  # Записываем пользовательское сообщение в лог
            result = func(*args, **kwargs)  # Вызываем оригинальную функцию и сохраняем результат
            return result  # Возвращаем результат выполнения оригинальной функции
        return wrapper  # Возвращаем внутреннюю функцию как результат декоратора
    return decorator  # Возвращаем внутреннюю функцию как результат внешней функции декоратора

@logged("Функция add1 вызвана:")  # Применяем декоратор с пользовательским сообщением к функции
def add1(a, b):  # Оригинальная функция
    return a + b  # Возвращаем сумму аргументов

add1(3, 5)  # Вызываем декорированную функцию


