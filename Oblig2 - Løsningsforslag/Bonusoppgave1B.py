import random

number_of_players = int(input("How many players are going to play? "))
number_of_rounds = int(input("How many rounds are going to be played? "))
number_of_darts = int(input("How many darts are going to be thrown each round? "))

player_round_score = 0
# Creates a list to put the scores for each player in
# We also use the index for player number,
# so we add an "empty player" at the beginning
players_total_score = [0]*(number_of_players+1)

for round_number in range(1, number_of_rounds+1):
    print(f"\n====Round {round_number}====")
    for player_number in range(1, number_of_players+1):
        for throw in range(number_of_darts):
            score = random.randrange(0, 23)
            if 0 < score < 21:  # Hvis score er over 0 og under 20, kan vi ha fått dobbel eller trippel
                multiplier_chance = random.random()
                if multiplier_chance <= 0.3:  # ~30% sjanse for dobbel
                    score *= 2
                elif multiplier_chance <= 0.5:  # ~20% sjanse for trippel
                    score *= 3
            elif score == 21:  # Konverterer 21 til 25p outer bullseye
                score = 25
            elif score == 22:  # Konverterer 21 til 50p  bullseye
                score = 50

            player_round_score += score
        print(f"Player {player_number} - Score: {player_round_score}")
        players_total_score[player_number] += player_round_score
        player_round_score = 0

print("\nEnd scores:")
for player_number, player_score in enumerate(players_total_score[1:], 1):
    print(f"Player {player_number} - Score: {player_score}")
