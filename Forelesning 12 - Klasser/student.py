class Student:
    def __init__(self, first_name, last_name, age, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def enroll_in_course(self, course):
        self.courses.append(course)

    def get_total_credits(self):
        total_credits = 0
        for course in self.courses:
            total_credits += course.credits
        return total_credits


class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

