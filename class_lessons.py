# Здесь я разобрал классы, аттрибуты, методы и инкапсуляцию. Так же присутствуют геттеры и сеттеры
# свойства-геттеры и свойства-сеттеры

class Person:
    # конструктор
    def __init__(self, name, age):  # Конструктор
        self.__name = name  # Инкапсуляция
        self.__age = age  # Инкапсуляция
        print('This person created')

    def set_age(self, age):  # Сеттер
        if 0 < age < 100:
            self.__age = age
        else:
            print('Invalid age')

    def get_age(self):  # Геттер
        return self.__age

    def get_name(self):
        return self.__name  # Геттер

    def say_hello(self, msg):  # Method
        print(f'{self.__name} say "{msg}"')

    def __str__(
            self):  # Магический метод, который определяет как будет выводиться объект класса (print(user = Person()))
        print(f'Name: {self.__name}, age: {self.__age}')

    def __del__(
            self):  # Деструктор, выполняет то что внутри деструктора перед удалением объекта, на который больше нет ссылок
        print('This person deleted')


def create_person():
    user = Person(input('Enter your name: '), input('Enter your age: '))
    user.say_hello(input('What you want to say?: '))
    print(user)
    user.set_age(55)
    print(user)


create_person()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"This auto: {self.brand} {self.model} {self.year} year"


auto1 = Car('Ford', 'Focus', 2009)
auto2 = Car('Porsche', 911, 2021)
print(auto1)
print(auto2)


# Свойства-геттеры и свойства-сеттеры
class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # свойство-геттер, пишется @property (ОПРЕДЕЛЯЕТСЯ ВСЕГДА ПЕРВЫМ)
    @property
    def age(self):
        return self.__age

    # свойство-сеттер, аннотация устанавливается имя_свойство_геттера.setter
    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Invalid age")

    @property
    def name(self):
        return self.__name

    def print_info(self):
        print(f'Name: {self.__name}, Age: {self.__age}')


tom = Human('Tom', 20)
tom.print_info()
tom.age = -12323
print(tom.age)
tom.age = 25
tom.print_info()
print(tom.age)
