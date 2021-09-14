board_games = ['Ubongo', 'Pandemic', 'Ticket To Ride', 'Monopoly', 'Mysterium']

for board_game in board_games:
    print(f"{board_game} is a good game!")
    print("You should try it!\n")

# Printing the characters in the string one by one with a for-loop
for character in 'Risk':
    print(character)

pandemic_legacy_season = 'Pandemic Legacy: Season'

for number_in_series in range(3):
    pandemic_legacy = f"{pandemic_legacy_season} {number_in_series}"
    if pandemic_legacy not in board_games:
        print(f"{pandemic_legacy} is not in the collection. That's a shame, let's add it!")
        board_games.append(pandemic_legacy)

print("\nBoardgames in our collection: ")
for board_game in board_games:
    print(board_game)


print("\nLet's clean up our collection, we are tired of the Pandemic games:")
purged_list = []
for board_game in board_games:
    # Checkin if 'Pandemic' is part of the name of the board game
    if 'Pandemic' in board_game:
        print(f"We don't want {board_game}...")
        # We can't remove items from a list safely while we iterate to it
        # board_games.remove(board_game)
    else:
        purged_list.append(board_game)

board_games = purged_list

print("\nUpdated list without Pandemic games: ")
for board_game in board_games:
    print(board_game)


board_games.append('Monopoly')
board_games.append('Monopoly')
board_games.append('Monopoly')

print("\nWe don't really want any Monolopy games either...")
board_games.remove('Monopoly')
while 'Monopoly' in board_games:
    board_games.remove('Monopoly')
    print("Removing Monopoly...")

print("\nOur final collection: ")
for board_game in board_games:
    print(board_game)

print("\nLet's sell them all: ")
# Will continue as long as the list is not empty
while board_games:
    print(f"{board_games.pop()} - sold")



