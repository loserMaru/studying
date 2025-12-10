class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, txt):
        name, age = txt.split('-')
        return cls(name, int(age))


p1 = Person('John', 25)
p2 = Person.from_string('Mary-30')

print(p1.name, p1.age)
print(p2.name, p2.age)


# Метод from_string получает сам класс (cls = Person) и возвращает новый экземпляр, созданный через cls(...)
# Это позволяет удобно создавать объекты не только из аргументов конструктора, но и из других источников (строка, файл и т. д.)


class Animal:
    species = 'Animal'

    @classmethod
    def show_species(cls):
        print("Type:", cls.species)


class Dog(Animal):
    species = 'Dog'


class Cat(Animal):
    species = 'Cat'

Dog.show_species()
Cat.show_species()

# Здесь метод show_species() получает ссылку на сам класс, а не на Animal напрямую
# Это значит, что при вызове от подкласса (Dog или Cat), он обращается к его версии переменной species


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        d, m, y = date_str.split('.')
        return cls(int(d), int(m), int(y))

    @classmethod
    def today(cls):
        return cls(12, 11, 2025)

d1 = Date(1, 1, 2024)
d2 = Date.from_string('31.12.2025')
d3 = Date.today()

print(d1.day, d2.month, d3.year)

# ✅ from_string и today оба создают экземпляры класса, но делают это по-разному
# Это как несколько «входов» к одному и тому же конструктору