class Student:
    def __init__(self, name):
        self.name = name
        self._grades = []

    @property
    def grades(self):
        return self._grades

    def add_grade(self, grade):
        if not isinstance(grade, Grade):
            raise TypeError('Only object of type Grade can be set')
        self._grades.append(grade)

    def show_grades(self):
        if not self._grades:
            raise ValueError('Student has no grades')
        else:
            print(f"Student {self.name}, grades: ")
            for g in self._grades:
                print(f"Lesson: {g.lesson.name} \tGrade: {g.value} \tTeacher: {g.teacher.name}")


class Teacher:
    def __init__(self, name):
        self.name = name

    def put_grade(self, student, lesson, value):
        grade = Grade(lesson, self, value)
        student.add_grade(grade)


class Lesson:
    def __init__(self, name):
        self.name = name


class Grade:
    def __init__(self, lesson, teacher, value):
        self.lesson = lesson
        self.teacher = teacher
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise TypeError('Only int can be set')
        if not 1 <= new_value <= 5:
            raise ValueError('Value must be between 1 and 5')
        self._value = new_value

    def __str__(self):
        return f'{self.lesson}, {self.teacher}, {self.value}'

math = Lesson("Математика")
physics = Lesson("Физика")

teacher = Teacher("Мария Петрова")
student = Student("Иван Иванов")

teacher.put_grade(student, math, 5)
teacher.put_grade(student, physics, 3)

student.show_grades()
