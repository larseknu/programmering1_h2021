board_game = {
    'title': 'Dixit',
    'playtime': 30,
    'age': 8,
    'description': "Give the perfect clue so most (not all) players guess the right surreal image card."
}

print(f"\nLoop that iterates the keys for {board_game['title']} (use the keys to get the values as well):")
for key in board_game:  # Kan også bruke board_game.keys()
    print(f"{key.title()} - {board_game[key]}")

print(f"\nJust values for {board_game['title']}:")
for value in board_game.values():
    print(value)

print(f"\nValues and keys in the same for-loop")
for key, value in board_game.items():
    print(f"{key.title()} - {value}")