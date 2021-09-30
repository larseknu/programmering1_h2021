board_games = [
    {'title': 'Dixit', 'playtime': 30, 'age': 8, 'year': 2008},
    {'title': 'Pandemic', 'playtime': 45, 'age': 8, 'year': 2008},
    {'title': 'Wingspan', 'playtime': 40, 'age': 10, 'year': 2019},
]

print("\nBoard games loop from list:")
for board_game in board_games:
    print(f"{board_game['title']} are for players {board_game['age']} and above")

board_games.append({'title': 'Mysterium', 'playtime': 42, 'age': 10, 'year': 2015})

wingspan = board_games[2]
print(f"{wingspan['title']} is  a good game!")


board_games = {
    'dixit2008': {'title': 'Dixit', 'playtime': 30, 'age': 8, 'year': 2008},
    'pandemic2008': {'title': 'Pandemic', 'playtime': 45, 'age': 8, 'year': 2008},
    'wingspan2019': {'title': 'Wingspan', 'playtime': (40, 70), 'age': 10, 'year': 2019},
}

print("\nBoard games in loop from dictionary:")
for key, board_game in board_games.items():
    print(f"{key} - {board_game['title']} was released in {board_game['year']}")
