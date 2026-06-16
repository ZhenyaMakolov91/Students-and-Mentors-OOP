class Student:
    def __init__(self, name, surname, gender):
        self.name, self.surname, self.gender = name, surname, gender
        self.finished_courses, self.courses_in_progress, self.grades = [], [], {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _middle_grade(self):
        count_grades, total_grades = [], []
        for i in self.grades.values():
            count_grades.append(len(i)), total_grades.append(sum(i))
        if not count_grades:
            return 0
        return sum(total_grades) / sum(count_grades)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._middle_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._middle_grade() == other._middle_grade()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self._middle_grade() < other._middle_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, type(self)):
            return self._middle_grade() <= other._middle_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name, self.surname, self.courses_attached = name, surname, []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _middle_grade(self):
        return Student._middle_grade(self)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._middle_grade()}'

    def __eq__(self, other):
        return Student.__eq__(self, other)

    def __lt__(self, other):
        return Student.__lt__(self, other)

    def __le__(self, other):
        return Student.__le__(self, other)


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def middle_grades_all_students(students, course):
    res = sum(i._middle_grade() for i in students if course in i.courses_in_progress) / len(students)
    return f'Средняя оценка студентов за домашние задания по курсу {course}: {res}'

def middle_grades_all_lecturers(lecturers, course):
    res = sum(i._middle_grade() for i in lecturers if course in i.courses_attached) / len(lecturers)
    return f'Средняя оценка лекторов в рамках курса {course}: {res}'

student1, student2 = Student('Виктория', 'Панина', 'Ж'), Student('Владислав', 'Кузнецов', 'М')
lecturer1, lecturer2 = Lecturer('Иван', 'Плугарь'), Lecturer('Татьяна', 'Литвинова')
reviewer1, reviewer2 = Reviewer('Лидия', 'Стец'), Reviewer('Сергей', 'Коноваленко')

student1.add_courses('Анлийский язык'), student2.add_courses('Информатика')
student1.courses_in_progress += ['Python', 'SQL', 'C++']
student2.courses_in_progress += ['C++', 'Git', 'Python', 'JavaScript']
lecturer1.courses_attached.extend(['Python', 'C++']), lecturer2.courses_attached.extend(['C++', 'Python'])
reviewer1.courses_attached.append('Python'), reviewer2.courses_attached.append('Python')

student1.rate_lecture(lecturer1, 'C++', 10), student2.rate_lecture(lecturer2, 'C++', 7)
reviewer1.rate_hw(student1, 'Python', 10), reviewer2.rate_hw(student2, 'Python', 8)

print(reviewer1, reviewer2, sep='\n\n', end='\n\n')
print(lecturer1, lecturer2, sep='\n\n', end='\n\n')
print(student1, student2, sep='\n\n', end='\n\n')

print(student1 == student2, student1 < student2, student1 > student2, sep=', ')
print(lecturer1 == lecturer2, lecturer1 < lecturer2, lecturer1 > lecturer2, sep=', ')

print(middle_grades_all_students([student1, student2], 'Python'))
print(middle_grades_all_lecturers([lecturer1, lecturer2], 'C++'))