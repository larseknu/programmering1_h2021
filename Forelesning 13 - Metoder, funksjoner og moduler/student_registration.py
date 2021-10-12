from student import Student, Course
import courses

nils_nilsen = Student("Nils", "Nilsen", 22, "IT15652")
programmering1 = Course("Programmering 1", "ITF1205963", 10)
webutvikling = Course("Webutvikling", "ITF111111", 10)
databaser = Course("Databaser", "ITF213123", 10)

all_courses = [programmering1, webutvikling, databaser]

nils_nilsen.enroll_in_course(programmering1)
nils_nilsen.enroll_in_course(webutvikling)

print("Got total credits with the use of a method:")
print(f"{nils_nilsen.get_full_name()} has {nils_nilsen.get_total_credits()} credits")

print("\nGot total credits with the use of a function:")
print(f"{nils_nilsen.get_full_name()} has {courses.calculate_total_credit(nils_nilsen.courses)} credits")

print("\nAll total credits for all the courses in the BsC:")
print(courses.calculate_total_credit(all_courses))