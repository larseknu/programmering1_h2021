def calculate_total_credit(courses):
    total_credits = 0
    for course in courses:
        total_credits += course.credits
    return total_credits
