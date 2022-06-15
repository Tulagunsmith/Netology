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
                        f'Курсы в процессе изучения: {" ".join(x for x in self.courses_in_progress)}\n'
                        f'Завершенные курсы: {" ".join(x for x in self.finished_courses)}')
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
    res = round(total / count, 1)
    return res


chris_student = Student('Christopher', 'Morris', 'male')
chris_student.courses_in_progress += ['Python']
chris_student.courses_in_progress += ['C#']
chris_student.finished_courses += ['Введение в программирование']
leela_student = Student('Leela', 'Turanga', 'female')
leela_student.courses_in_progress += ['Python']
leela_student.courses_in_progress += ['JS']
leela_student.finished_courses += ['Введение в программирование']

collin_reviewer = Reviewer('Collin', 'Robinson')
collin_reviewer.courses_attached += ['Python']
collin_reviewer.courses_attached += ['JS']
bender_reviewer = Reviewer('Bender', 'Rodrigez')
bender_reviewer.courses_attached += ['Python']
bender_reviewer.courses_attached += ['C#']

ellen_lecturer = Lecturer('Ellen', 'Ripley')
ellen_lecturer.courses_attached += ['Python']
ellen_lecturer.courses_attached += ['C#']
ellen_lecturer.courses_attached += ['JS']
doc_lecturer = Lecturer('Doctor', 'Lector')
doc_lecturer.courses_attached += ['C#']
doc_lecturer.courses_attached += ['Python']
doc_lecturer.courses_attached += ['JS']

collin_reviewer.rate_hw(chris_student, 'Python', 10)
collin_reviewer.rate_hw(leela_student, 'JS', 8)
collin_reviewer.rate_hw(leela_student, 'JS', 7)
collin_reviewer.rate_hw(leela_student, 'Python', 8)
bender_reviewer.rate_hw(leela_student, 'Python', 6)
bender_reviewer.rate_hw(chris_student, 'C#', 7)
bender_reviewer.rate_hw(chris_student, 'C#', 6)
bender_reviewer.rate_hw(chris_student, 'Python', 8)

chris_student.rate_lecturer(ellen_lecturer, 'Python', 8)
chris_student.rate_lecturer(doc_lecturer, 'Python', 10)
chris_student.rate_lecturer(doc_lecturer, 'C#', 10)
chris_student.rate_lecturer(doc_lecturer, 'C#', 10)
leela_student.rate_lecturer(doc_lecturer, 'Python', 10)
leela_student.rate_lecturer(ellen_lecturer, 'Python', 7)
leela_student.rate_lecturer(ellen_lecturer, 'JS', 8)
leela_student.rate_lecturer(ellen_lecturer, 'JS', 7)


students = [chris_student, leela_student]
lecturers = [ellen_lecturer, doc_lecturer]


def avarage_course_grade(apprentices, course):
    count = 0
    common = 0
    for apprentice in apprentices:
        for keys, values in apprentice.grades.items():
            if course in keys:
                count += sum(values)
                common += len(values)
    total = round(count / common, 1)
    return total


print(chris_student.grades)
print()
print(leela_student.grades)
print()
print(ellen_lecturer.grades)
print()
print(doc_lecturer.grades)
print()
print(chris_student)
print()
print(leela_student)
print()
print(collin_reviewer)
print()
print(bender_reviewer)
print()
print(ellen_lecturer)
print()
print(doc_lecturer)
print()
print(ellen_lecturer < doc_lecturer)
print(ellen_lecturer > doc_lecturer)
print(chris_student > leela_student)
print(chris_student < leela_student)

print(avarage_course_grade(students, 'Python'))
print(avarage_course_grade(lecturers, 'Python'))
