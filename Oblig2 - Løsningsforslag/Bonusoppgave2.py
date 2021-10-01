import random

number_of_players = int(input("How many players are going to play? "))

count_down_from = 301
# Creates lists to put the scores and throws for each player in
# We also use the index for player number,
# so we add an "empty player" at the beginning
players_total_throws = [0]*(number_of_players+1)
players_current_score = [301]*(number_of_players+1)

was_double = False

for player_number in range(1, number_of_players+1):
    while players_current_score[player_number] != 0:
        score = random.randrange(0, 23)
        if 0 < score < 21:  # Hvis score er over 0 og under 20, kan vi ha fått dobbel eller trippel
            multiplier_chance = random.random()
            if multiplier_chance <= 0.3:  # ~30% sjanse for dobbel
                score *= 2
                was_double = True
            elif multiplier_chance <= 0.5:  # ~20% sjanse for trippel
                score *= 3
        elif score == 21:  # Konverterer 21 til 25p outer bullseye
            score = 25
        elif score == 22:  # Konverterer 21 til 50p  bullseye
            score = 50

        players_total_throws[player_number] += 1

        if players_current_score[player_number] == 301 and was_double:  # Start condition
            players_current_score[player_number] -= score
            print(f"\nPlayer {player_number} got started after {players_total_throws[player_number]} of throws")
        elif players_current_score[player_number] - score <= 1:
            if players_current_score[player_number] - score == 0 and was_double:  # Winning condition
                players_current_score[player_number] -= score
                print(f"Player {player_number} finished after {players_total_throws[player_number]} of throws")
        elif players_current_score[player_number] != 301:
            players_current_score[player_number] -= score
            print(f"Player {player_number} got a score of {score} on throw {players_total_throws[player_number]} "
                  f"and has {players_current_score[player_number]} left")

        was_double = False


print("\nEnd scores:")
for player_number, player_score in enumerate(players_total_throws[1:], 1):
    print(f"Player {player_number} - Number of throws: {player_score}")
