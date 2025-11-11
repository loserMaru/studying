class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f'Name: {self.__name}')


class Employee(Person):

    def work(self):
        print(f'{self.name} is working')


bob = Employee('Bob')
print(bob.name)
bob.display_info()
bob.work()

                # Вариант обычного класса без наследования
# class Employee:
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Name: {self.__name}')
#
#     def work(self):
#         print(f'{self.__name} is working')