class Person:
    # default_name = 'Undefined'
    #
    # def __init__(self, name):
    #     if name:
    #         self.name = name
    #     else:
    #         self.name = Person.default_name

    name = 'Undefined'

    def print_name(self):
        print(self.name)

# tom = Person(input())
# bob = Person(input())
# print(tom.name)
# print(bob.name)

tom = Person()
bob = Person()
tom.print_name()
bob.print_name()

Person.name = 'Some person'
bob.name = 'Bob'
tom.print_name()
bob.print_name()


class Human:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Human.__type)


Human.print_type()

tom = Human()
tom.print_type()