from student import Student, Course

nils_nilsen = Student("Nils", "Nilsen", 22, "IT15652")
programmering1 = Course("Programmering 1", "ITF1205963", 10)
webutvikling = Course("Webutvikling", "ITF111111", 10)

nils_nilsen.enroll_in_course(programmering1)
nils_nilsen.enroll_in_course(webutvikling)

print(f"{nils_nilsen.get_full_name()} has {nils_nilsen.get_total_credits()} credits")