class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        student_data = f'Имя: {self.name}\nФамилия: {self.surname}'
        return student_data


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


test_student = Student('Ruoy', 'Eman', 'your_gender')
test_student.courses_in_progress += ['Python']

test_reviewer = Reviewer('Some', 'Buddy')
test_reviewer.courses_attached += ['Python']

test_lecturer = Lecturer('John', 'Smith')
test_lecturer.courses_attached += ['Python']

test_reviewer.rate_hw(test_student, 'Python', 10)

test_student.rate_lecturer(test_lecturer, 'Python', 8)

print(test_student.grades)
print(test_lecturer.grades)
print(test_student)