import random


def pick_random_boardgame(boardgames):
    boardgame_index = random.randrange(len(boardgames))
    return boardgames.pop(boardgame_index)


def print_list(list_to_print):
    for element in list_to_print:
        print(element)


board_games = ['Ubongo', 'Pandemic', 'Ticket To Ride', 'Monopoly', 'Mysterium']

#picked_boardgame = pick_random_boardgame(board_games)
picked_boardgame = pick_random_boardgame(board_games)  # Hvis vi ikke vil at lista skal endres sender vi med en kopi [:]

print(f"You picked {picked_boardgame}. Have fun playing! :)")

print("\nThe games you have left:")
print_list(board_games)

