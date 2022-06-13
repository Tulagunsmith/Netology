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
        student_data = (f'Имя: {self.name}\n'
                        f'Фамилия: {self.surname}\n'
                        f'Средняя оценка за домашние задания: {avarage_grade(self.grades)}\n'
                        f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                        f'Завершенные курсы: {self.finished_courses}')
        return student_data

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение!')
            return
        return avarage_grade(self.grades) < avarage_grade(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        lecturer_data = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avarage_grade(self.grades)}'
        return lecturer_data

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение!')
            return
        return avarage_grade(self.grades) < avarage_grade(other.grades)



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_data = f'Имя: {self.name}\nФамилия: {self.surname}'
        return reviewer_data


def avarage_grade(grades_dict):
    total = 0
    count = 0
    for grades in grades_dict.values():
        for grade in grades:
            total += grade
            count += 1
    res = total / count
    return res


chris_student = Student('Christopher', 'Morris', 'male')
chris_student.courses_in_progress += ['Python']
chris_student.courses_in_progress += ['C#']
leela_student = Student('Leela', 'Turanga', 'female')
leela_student.courses_in_progress += ['Python']
leela_student.courses_in_progress += ['JS']

collin_reviewer = Reviewer('Collin', 'Robinson')
collin_reviewer.courses_attached += ['Python']
bender_reviewer = Reviewer('Bender', 'Rodrigez')
bender_reviewer.courses_attached += ['Python']

ellen_lecturer = Lecturer('Ellen', 'Ripley')
ellen_lecturer.courses_attached += ['Python']
doc_lecturer = Lecturer('Doctor', 'Lector')
doc_lecturer.courses_attached += ['C#']

collin_reviewer.rate_hw(chris_student, 'Python', 10)

chris_student.rate_lecturer(ellen_lecturer, 'Python', 8)
chris_student.rate_lecturer(ellen_lecturer, 'Python', 10)
chris_student.rate_lecturer(doc_lecturer, 'C#', 10)
chris_student.rate_lecturer(doc_lecturer, 'C#', 10)

print(chris_student.grades)
print()
print(ellen_lecturer.grades)
print()
print(doc_lecturer.grades)
print()
print(collin_reviewer)
print()
print(ellen_lecturer)
print()
print(doc_lecturer)
print()
print(chris_student)
print()
print(ellen_lecturer < doc_lecturer)