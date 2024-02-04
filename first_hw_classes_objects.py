class Student:
    students_items = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students_items.append(self)

    def lecturer_rate(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_hw(self):
        grades_list = list(self.grades.values())
        grades_list = sum(grades_list, start=[])
        average_grade = sum(grades_list) / len(grades_list)
        return average_grade

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.average_grade_hw()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):
        return self.average_grade_hw() == other.average_grade_hw()

    def __ne__(self, other):
        return self.average_grade_hw() != other.average_grade_hw()

    def __lt__(self, other):
        return self.average_grade_hw() < other.average_grade_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers_items = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturers_items.append(self)

    def average_grade(self):
        grades_list = list(self.grades.values())
        grades_list = sum(grades_list, start=[])
        average_grade = sum(grades_list) / len(grades_list)
        return average_grade

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} '
                f'\nСредняя оценка за лекции: {self.average_grade()}')

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['SQL']

other_student = Student('Mikky', 'Mouse', 'male')
other_student.courses_in_progress += ['Python']
other_student.courses_in_progress += ['Git']
other_student.courses_in_progress += ['Java']
other_student.finished_courses += ['HTML']

first_mentor = Mentor('Katy', 'Perry')
first_mentor.courses_attached += ['Python']

second_mentor = Mentor('Ariana', 'Grande')
second_mentor.courses_attached += ['Git']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

other_mentor = Lecturer('Tom', 'Ford')
other_mentor.courses_attached += ['Python']
other_mentor.courses_attached += ['Git']

some_reviewer = Reviewer('Mike', 'Ro')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

top_reviewer = Reviewer('Bradley', 'Pitt')
top_reviewer.courses_attached += ['Python']
top_reviewer.courses_attached += ['Git']

some_reviewer.rate_hw(best_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Python', 8)
some_reviewer.rate_hw(best_student, 'Git', 7)

some_reviewer.rate_hw(other_student, 'Python', 3)
some_reviewer.rate_hw(other_student, 'Python', 6)
some_reviewer.rate_hw(other_student, 'Git', 5)

top_reviewer.rate_hw(other_student, 'Python', 3)
top_reviewer.rate_hw(other_student, 'Python', 4)
top_reviewer.rate_hw(other_student, 'Git', 5)

top_reviewer.rate_hw(best_student, 'Python', 10)
top_reviewer.rate_hw(best_student, 'Python', 10)
top_reviewer.rate_hw(best_student, 'Git', 10)

best_student.lecturer_rate(cool_mentor, 'Python', 2)
best_student.lecturer_rate(cool_mentor, 'Python', 7)
best_student.lecturer_rate(cool_mentor, 'Git', 3)

other_student.lecturer_rate(cool_mentor, 'Python', 9)
other_student.lecturer_rate(cool_mentor, 'Python', 10)
other_student.lecturer_rate(cool_mentor, 'Git', 9)

print(best_student.average_grade_hw())

print(other_student.average_grade_hw())

best_student.lecturer_rate(other_mentor, 'Python', 1)
best_student.lecturer_rate(other_mentor, 'Python', 5)
best_student.lecturer_rate(other_mentor, 'Git', 4)

other_student.lecturer_rate(other_mentor, 'Python', 7)
other_student.lecturer_rate(other_mentor, 'Python', 4)
other_student.lecturer_rate(other_mentor, 'Git', 6)

print(cool_mentor.average_grade())

print(other_mentor.average_grade())

print(cool_mentor)
print(other_mentor)
print(some_reviewer)
print(top_reviewer)
print(best_student)
print(other_student)
print(other_mentor < cool_mentor)
print(other_mentor == cool_mentor)
print(other_mentor > cool_mentor)
print(other_mentor != cool_mentor)
print(other_student > best_student)
print(other_student != best_student)
print(other_student < best_student)
print(other_student == best_student)


def avarege_rate_students(students_list, course):
    full_sum_rates = 0
    full_number_rates = 0
    for student in students_list:
        if course in student.grades:
            full_sum_rates += sum(student.grades.get(course), start=0)
            full_number_rates += len(student.grades.get(course))
        else:
            return print(f'Нет оценок за курс {course}!')
    average_rate_students = full_sum_rates / full_number_rates
    print(f'Cредняя оценка за домашние задания по всем студентам '
          f'в рамках курса {course}: {average_rate_students}')


avarege_rate_students(Student.students_items, 'Python')
avarege_rate_students(Student.students_items, 'Git')
avarege_rate_students(Student.students_items, 'HTML')
avarege_rate_students(Student.students_items, 'Java')


def avarege_rate_lecturer(lecturers_list, course):
    full_sum_rates = 0
    full_number_rates = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            full_sum_rates += sum(lecturer.grades.get(course), start=0)
            full_number_rates += len(lecturer.grades.get(course))
        else:
            return print(f'Нет оценок за лекции курса {course}!')
    average_rate_lecturers = full_sum_rates / full_number_rates
    print(f'Cредняя оценка за лекции всех лекторов '
          f'в рамках курса {course}: {average_rate_lecturers}')


avarege_rate_lecturer(Lecturer.lecturers_items, 'Python')
avarege_rate_lecturer(Lecturer.lecturers_items, 'Git')
avarege_rate_lecturer(Lecturer.lecturers_items, 'HTML')
avarege_rate_lecturer(Lecturer.lecturers_items, 'Java')