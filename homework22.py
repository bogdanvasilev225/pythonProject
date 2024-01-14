"""
Задача 1: Создание класса и объекта
Создайте класс Car.
Добавьте конструктор, который принимает параметры make (марка) и model (модель) и инициализирует атрибуты объекта.
Создайте объект my_car с маркой "Toyota" и моделью "Camry".
Выведите на экран марку и модель вашего автомобиля.
"""
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Camry")
print(my_car.make, my_car.model)

"""
Задача 2: Наследование и переопределение методов
Создайте класс Vehicle с методом drive(), который возвращает строку "Vehicle is moving".
Создайте класс Car на основе класса Vehicle.
Переопределите метод drive() в классе Car так, чтобы он возвращал строку "Car is moving".
Создайте объект my_car типа Car и вызовите метод drive(). Выведите результат.
"""
class Vehicle:
    def drive(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def drive(self):
        return "Car is moving"

# Создаем объект my_car класса Car
my_car = Car()
print(my_car.drive())

"""
Задача 3: Инкапсуляция
Создайте класс Person.
Добавьте атрибуты name и age, инициализируйте их через конструктор.
Сделайте атрибут age приватным (используйте подчеркивание в начале имени).
Создайте метод get_age(), который возвращает значение атрибута age.
Создайте объект person с именем "John" и возрастом 25.
Выведите имя и возраст объекта, используя метод get_age().
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

person = Person("John", 25)
print(f"My name is {person.name}, and I am {person.get_age()} years old.")

"""
Задача 4: Полиморфизм
Создайте класс Animal с методом make_sound(), который возвращает строку "Some sound".
Создайте классы Dog и Cat, которые наследуются от класса Animal.
Переопределите метод make_sound() в классах Dog и Cat так, чтобы он возвращал "Woof!" и "Meow!" соответственно.
Создайте функцию animal_sound(animal), которая вызывает метод make_sound() объекта типа Animal.
Создайте объекты dog и cat, передайте их в функцию animal_sound() и выведите результат.
"""
class Animal:

    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_sound(animal):
    return animal.make_sound()

dog = Dog()

cat = Cat()

print(animal_sound(dog), animal_sound(cat))