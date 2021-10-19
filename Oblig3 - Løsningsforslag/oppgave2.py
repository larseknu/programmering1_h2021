import random


def print_random_number():
    number = random.randrange(0, 101)
    print("\n*********")
    print(f"***{number:03}***")
    print("*********")


print_random_number()
print_random_number()
print_random_number()
