for number in range(5):
    print(f"Iteration {number+1}")

for number in range(6, 11):
    print(f"Number {number}")

print("\nWith steps: ")
for number in range(3, 11, 2):
    print(f"Number: {number}")


print("\nWith variable: ")
number_of_iterations = 5
for number in range(number_of_iterations):
    print(f"Iteration {number+1}")


print("\nGames:")
videogames = ['Tetris', 'Mario Bros.', 'Legend of Zelda']
for videogame in videogames:
    print(f"{videogame} is a cool game!")

print("\nWord:")
word = 'Spooky!'
for character in word:
    print(character)

iteration = 0
while iteration <= 5:
    print(f"Iteration {iteration}")
    iteration += 1

correct = False
while not correct:
    answer = input("What's a man's best friend?: ")
    print(answer)

    if answer.lower() == "dog":
        print("Correct!")
        correct = True
    else:
        print("Incorrect! Try again!")