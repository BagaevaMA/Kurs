import os
from datetime import datetime
print('СТУДЕНТЫ')

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            current_datetime = datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(path, "a") as f:
                f.write(f'Date and time:{current_datetime}\n'
                        f'Name of function: {func_name}\n'
                        f'Arguments {args} {kwargs}\n'
                        f'Result {result}\n')
            return result

        return new_function

    return __logger

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades_student(self):
        grade = 0
        for value in self.grades.values():
            grade +=value
        average = round(grade/len(self.grades), 2)
        return average

    def __str__(self):
        courses_in_progress = ",".join(self.courses_in_progress)
        finished_courses = ",".join(self.finished_courses)
        res =  f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания: {self.average_grades_student()}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'
        return res

    def __lt__(self, other):
        return self.average_grades_student() < other.average_grades_student()


olga_babich = Student('Ольга', 'Бабич', 'ж')
olga_babich.courses_in_progress = ['Бухгалтер', 'Аналитик', 'Физика']
olga_babich.finished_courses = ['Менеджер']
olga_babich.grades = {'Бухгалтер': 10, 'Аналитик': 7, 'Менеджер': 6, 'Физика': 4}

ivan_fursov = Student('Иван', 'Фурсов', 'м')
ivan_fursov.courses_in_progress = ['Геймдизайнер', 'Аналитик', 'Математика']
ivan_fursov.finished_courses = ['Фотограф']
ivan_fursov.grades = {'Геймдизайнер': 8, 'Аналитик': 2, 'Фотограф': 4, 'Математика': 8}

sergey_lotc = Student('Сергей', 'Лотц', 'м')
sergey_lotc.courses_in_progress = ['Геймдизайнер', 'Менеджер', 'Химия']
sergey_lotc.finished_courses = ['Аналитик']
sergey_lotc.grades = {'Геймдизайнер': 9, 'Менеджер': 8, 'Аналитик': 4, 'Химия': 5}

elena_lazareva = Student('Елена', 'Лазарева', 'ж')
elena_lazareva.courses_in_progress = ['Геймдизайнер', 'Менеджер', 'Геометрия']
elena_lazareva.finished_courses = ['Аналитик']
elena_lazareva.grades = {'Геймдизайнер': 6, 'Менеджер': 7, 'Аналитик': 2, 'Геометрия': 7}

mariya_zakharova = Student('Мария', 'Захарова', 'ж')
mariya_zakharova.courses_in_progress = ['Геймдизайнер', 'Фотограф', 'Математика']
mariya_zakharova.finished_courses = ['Аналитик']
mariya_zakharova.grades = {'Геймдизайнер': 10, 'Фотограф': 8, 'Аналитик': 9, 'Математика': 8}


if mariya_zakharova<olga_babich:
    print(f'У студента с именем {mariya_zakharova.name} средний бал меньше ')
else:
    print(f'У студента с именем {olga_babich.name} средний бал меньше ')

print('\nЛЕКТОРЫ')
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def average_grades_lecturer(self):
        grade = 0
        for value in self.grades.values():
            grade +=value
        average = round(grade/len(self.grades), 2)
        return average

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grades_lecturer()}'
        return res

    def __lt__(self, other):
        return self.average_grades_lecturer() < other.average_grades_lecturer()

max_firsov = Lecturer('Максим', 'Фирсов')
max_firsov.courses_attached = ['Менеджер','Аналитик', 'Физика']
max_firsov.grades = {'Менеджер': 10, 'Аналитик': 8, 'Физика': 7}

stas_kuznecov = Lecturer('Станислав', 'Кузнецов')
stas_kuznecov.courses_attached = ['Геймдизайнер','Фотограф', 'Математика', 'Геометрия']
stas_kuznecov.grades = {'Геймдизайнер': 7, 'Фотограф': 6, 'Математика':9, 'Геометрия': 7}

sergey_visotskiy = Lecturer('Сергей', 'Высоцкий')
sergey_visotskiy.courses_attached = ['Бухгалтер','Фотограф', 'Химия']
sergey_visotskiy.grades = {'Бухгалтер': 5, 'Фотограф': 7, 'Химия': 8}

if sergey_visotskiy<stas_kuznecov:
    print(f'У лектора с именем {sergey_visotskiy.name} {sergey_visotskiy.surname} средний бал меньше ')
else:
    print(f'У лектора с именем {stas_kuznecov.name} {stas_kuznecov.surname} средний бал меньше ')

print('\nПРОВЕРЯЮЩИЕ')
class Reviewer(Mentor):
    def rate_hw(self, mentor, course, grade):
        if isinstance(mentor, Mentor) and course in self.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

nadezda_golatova = Reviewer('Надежда', 'Голатова')
nadezda_golatova.courses_attached = ['Менеджер', 'Аналитик','Физика']

stas_sibrin = Reviewer('Станислав', 'Сибрин')
stas_sibrin.courses_attached = ['Геймдизайнер', 'Фотограф', 'Математика', 'Геометрия']

vladimir_vovko = Reviewer('Владимир', 'Вовко')
vladimir_vovko.courses_attached = ['Бухгалтер', 'Фотограф','Химия']

print(nadezda_golatova)

print('\nЗадание № 4. Полевые испытания')
list_students = [olga_babich, ivan_fursov, sergey_lotc, elena_lazareva, mariya_zakharova]

@logger('mydecorator.log')
def average_grades_student_in_course(list_students, course):
    grade = 0
    count = 0
    for i in list_students:
        for key, value in i.grades.items():
            if key == course:
                grade += value
                count +=1
    average = round(grade / count, 2)
    print(average)
    return average

average_grades_student_in_course(list_students, 'Геймдизайнер')

list_lecturer = [max_firsov, stas_kuznecov, sergey_visotskiy]

@logger('mydecorator.log')
def average_grades_lecturer_in_course(list_lecturer, course):
    grade = 0
    count = 0
    for i in list_lecturer:
        for key, value in i.grades.items():
            if key == course:
                grade += value
                count +=1
    average = round(grade / count, 2)
    print(average)
    return average

average_grades_student_in_course(list_lecturer, 'Фотограф')
