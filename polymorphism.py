class Animal:
    def __init__(self, name):
        self._name = name

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Gav'


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Milk'


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Cow'


def make_sound(animal):
    print(animal.speak())


cow = Cow('Cow')
print(cow.speak())
cat = Cat('Cat')
print(cat.speak())
dog = Dog('Dog')
print(dog.speak())

make_sound(cow)
make_sound(cat)
make_sound(dog)

animals = [cat, cow, dog]
for animal in animals:
    print(animal.speak())
