class Student:
    def __init__(self, name):
        self.name = name
        self._grades = []

    @property
    def grades(self):
        return self._grades

    def add_grade(self, grade):
        if not isinstance(grade, Grade):
            raise TypeError('Grade must be of type Grade')
        self._grades.append(grade)

    def show_grades(self):
        if not self._grades:
            raise ValueError('Student must have at least one grade')
        else:
            print(f"Student {self.name} grades: ")
            for grade in self._grades:
                print(f"Lesson: {grade.lesson.name} \tGrade: {grade.value} \tTeacher: {grade.teacher.name}")
            print('\n')

class Lesson:
    def __init__(self, name):
        self.name = name


class Teacher:
    def __init__(self, name):
        self.name = name

    def put_grade(self, student, lesson, value):
        grade = Grade(lesson, value, self)
        student.add_grade(grade)



class Grade:
    def __init__(self, lesson, value, teacher):
        self.lesson = lesson
        self.value = value
        self.teacher = teacher

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise TypeError('Value must be of type int')
        if not 1 <= value <= 5:
            raise ValueError('Value must be between 1 and 5')
        self._value = value

    def __str__(self):
        return f'{self.lesson.name}, {self.value}, {self.teacher.name}'


student = Student('Mark Pavlov')
student2 = Student('Maeln Osnv')

teacher = Teacher('Olge Petrovich')
teacher2 = Teacher('Petr Olgvch')

phys = Lesson('Physics')
math = Lesson('Math')

teacher.put_grade(student, math, 5)
teacher.put_grade(student, phys, 4)
teacher2.put_grade(student, math, 3)
teacher2.put_grade(student, phys, 2)

teacher.put_grade(student2, phys, 2)
teacher.put_grade(student2, math, 2)
teacher2.put_grade(student2, phys, 2)
teacher2.put_grade(student2, math, 2)


student.show_grades()
student2.show_grades()
