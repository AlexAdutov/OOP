class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def add_course(self, course):
        self.finished_courses.append(course)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                # print(lecturer.name)
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __aver_grade(self):
        sum_loc = count = 0
        for v in self.grades.values():
            sum_loc += sum(v)
            count += len(v)
        return round((sum_loc / count), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.__aver_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        # f'Курсы в процессе изучения: {[cours for cours in self.courses_in_progress]}\n' \
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.__aver_grade() < other.__aver_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def attached_course(self, course):
        self.courses_attached.append(course)


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def __aver_grade(self):
        sum_loc = count = 0
        for v in self.grades.values():
            sum_loc += sum(v)
            count += len(v)
        return round((sum_loc / count), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__aver_grade()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.__aver_grade() < other.__aver_grade()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


def aver_grade_ex(obj_list, course):
    sum_loc = count = 0
    for obj in obj_list:
        sum_loc += sum(obj.grades[course])
        count += len(obj.grades[course])
    return f'Средняя оценка по курсу {course} для {obj.name} {obj.surname} равна {round(sum_loc / count, 2)}'


best_student = Student('Вася', 'Иванов', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Basic']

good_student = Student('Соня', 'Мармеладова', 'female')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Basic']

super_lecturer = Lecturer('Тимофей', 'Хирьянов')
super_lecturer.courses_attached += ['Python']
super_lecturer.courses_attached += ['Basic']

bad_lecturer = Lecturer('Сергей', 'Немчинский')
bad_lecturer.courses_attached += ['Java']
bad_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Basic']

cool_reviewer = Reviewer('Мужик', 'В пиджаке')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Basic']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Basic', 4)
cool_reviewer.rate_hw(best_student, 'Basic', 5)
cool_reviewer.rate_hw(best_student, 'Basic', 5)

cool_reviewer.rate_hw(good_student, 'Python', 5)
cool_reviewer.rate_hw(good_student, 'Python', 5)
cool_reviewer.rate_hw(good_student, 'Python', 5)
cool_reviewer.rate_hw(good_student, 'Basic', 7)
cool_reviewer.rate_hw(good_student, 'Basic', 8)
cool_reviewer.rate_hw(good_student, 'Basic', 8)

best_student.rate_hw(super_lecturer, 'Python', 8)
best_student.rate_hw(super_lecturer, 'Python', 10)
best_student.rate_hw(super_lecturer, 'Python', 7)

best_student.rate_hw(super_lecturer, 'Basic', 4)
best_student.rate_hw(super_lecturer, 'Basic', 3)
best_student.rate_hw(super_lecturer, 'Basic', 5)

good_student.rate_hw(super_lecturer, 'Python', 8)
good_student.rate_hw(super_lecturer, 'Python', 5)
good_student.rate_hw(super_lecturer, 'Python', 7)

good_student.rate_hw(super_lecturer, 'Basic', 4)
good_student.rate_hw(super_lecturer, 'Basic', 4)
good_student.rate_hw(super_lecturer, 'Basic', 5)

best_student.rate_hw(bad_lecturer, 'Basic', 1)
best_student.rate_hw(bad_lecturer, 'Basic', 2)
best_student.rate_hw(bad_lecturer, 'Basic', 5)

good_student.rate_hw(bad_lecturer, 'Python', 2)
good_student.rate_hw(bad_lecturer, 'Python', 2)
good_student.rate_hw(bad_lecturer, 'Python', 3)

# print(best_student.grades, best_student.name, best_student.surname)
# print(good_student.grades, good_student.name, good_student.surname)
# print(super_lecturer.grades, super_lecturer.name, super_lecturer.surname)
# print(bad_lecturer.grades, bad_lecturer.name, bad_lecturer.surname)

best_student.add_course('C++')
best_student.add_course('En')

good_student.add_course('Массаж')
good_student.add_course('Кройка и шитье')

# __lt__
print(good_student.__lt__(best_student))
print(good_student > best_student)

print(super_lecturer.__lt__(bad_lecturer))
print(super_lecturer > bad_lecturer)

# __str__
print(cool_reviewer)
print(super_lecturer)
print(bad_lecturer)
print(best_student)
print(good_student)

# средняя оценка по курсу
print(aver_grade_ex(Student.student_list, 'Python'))
print(aver_grade_ex(Lecturer.lecturer_list, 'Python'))
