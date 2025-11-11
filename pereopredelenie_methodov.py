class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} does nothing")


class Employee(Person):
    def work(self):
        print(f"{self.name} works")


class Student(Person):
    def study(self):
        print(f"{self.name} study")


def act(person):
    if isinstance(person, Student):
        person.study()

    if isinstance(person, Employee):
        person.work()

    if isinstance(person, Person):
        person.do_nothing()


tom = Employee("Tom")
bob = Student("Bob")
sam = Person("Sam")

act(tom)
act(bob)
act(sam)
