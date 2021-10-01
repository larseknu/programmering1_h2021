import random

number_of_players = int(input("How many players are going to play? "))
number_of_darts = 3

player_score = 0

for player_number in range(1, number_of_players+2):
    for throw in range(number_of_darts):
        score = random.randrange(0, 61)
        player_score += score
        print(f"Throw: {score}")
    print(f"Player {player_number} end score: {player_score}\n")
    player_score = 0
