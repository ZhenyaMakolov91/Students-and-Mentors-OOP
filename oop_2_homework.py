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

    def middle_grade(self):
        count_grades, total_grades = [], []
        for i in self.grades.values():
            count_grades.append(len(i)), total_grades.append(sum(i))
        if not count_grades:
            return 0
        return sum(total_grades) / sum(count_grades)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.middle_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.middle_grade() == other.middle_grade()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.middle_grade() < other.middle_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, type(self)):
            return self.middle_grade() <= other.middle_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name, self.surname, self.courses_attached = name, surname, []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def middle_grade(self):
        return Student.middle_grade(self)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grade()}'

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