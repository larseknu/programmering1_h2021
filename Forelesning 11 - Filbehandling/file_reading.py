# file = open("zen_of_python.txt")
# content = file.read()
# print(content)
import random


def pick_random_quote(quotes):
    index = random.randrange(len(quotes))
    return quotes[index]


with open("text_files/zen_of_python.txt") as file:
    content = file.read()  # Leser alt innholdet i fila til en string
    print(content)

print(type(content))

with open("text_files/zen_of_python.txt") as file:
    line_list = file.readlines()  # Gir en liste med hver linje i fila

print(line_list)
print(pick_random_quote(line_list[2:]))
print(type(line_list))

with open("text_files/zen_of_python.txt") as file:
    print(f"\n{file.readline().rstrip()} - first line in the file")
    print(f"{file.readline().rstrip()} - second line in the file")
    print(f"{file.readline().rstrip()} - third line in the file")


filename = "this_file_does_not_exist.txt"

try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print(f"\nThe file {filename}, does not exist")
