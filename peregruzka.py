class Counter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value - other

    def __bool__(self):
        return self.value > 0

    def __eq__(self, other): return self.value == other.value
    def __ne__(self, other): return not (self == other)

    def __gt__(self, other): return self.value > other.value
    def __le__(self, other): return not (self > other)

    def __lt__(self, other): return self.value < other.value
    def __ge__(self, other): return not (self < other)


def test(counter):
    if counter:
        print('Counter = True')
    else:
        print('Counter = False')


# counter1 = Counter(5)
# counter2 = Counter(15)
# result = counter1 + 4
# print(result)

counter1 = Counter(3)
counter2 = Counter(-3)
test(counter1)
test(counter2)

while counter1:
    print("Counter1", counter1.value)
    counter1.value -= 1


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __getitem__(self, prop):
        if prop == 'name':
            return self.__name
        elif prop == 'age':
            return self.__age
        return None

    def __contains__(self, prop):
        if prop == 'name' or prop == 'age': return True
        return False


tom = Person('Tom', 18)

print("Name", tom['name'])
print("Age", tom['age'])
print("Id", tom['id'])

print("name" in tom)
print("age" in tom)
print("id" in tom)
