class Student:
    def __init__(self, name, surname, gender):
        self.name, self.surname, self.gender = name, surname, gender
        self.finished_courses, self.courses_in_progress, self.grades = [], [], {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name, self.surname, self.courses_attached = name, surname, []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor))
print(isinstance(reviewer, Mentor))
print(lecturer.courses_attached)
print(reviewer.courses_attached)