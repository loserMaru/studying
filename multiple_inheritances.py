class Worker:
    def do(self):
        print("Employee works")


class Student:
    def do(self):
        print("Student studies")


# class WorkingStudent(Student,Employee):
class WorkingStudent(Worker, Student):
    pass


tom = WorkingStudent()
tom.do()  # ?
print(WorkingStudent.__mro__)
print(WorkingStudent.mro())


# Метод super
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, company):
        # вызов конструкторя родителя
        super().__init__(name, age)
        self.company = company

    def info(self):
        # вызов метода родителя
        super().info()
        print(f"Company: {self.company}")


tom = Employee('Tom', 22, 'Google')
tom.info()


# Сложный пример множественного наследования и применения метода super()
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(B):
    def show(self):
        super().show()
        print("C")

c = C()
c.show()
print(C.__mro__)