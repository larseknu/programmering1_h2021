user_input = ""

with open("text_files/my_novel.txt", "a") as f:
    while user_input != "q":
        user_input = input(": ")
        f.write(user_input + "\n")

