def print_game_character(character, game="Super Mario Bros."):
    """Prints the character and the game given as arguments"""
    print(f"{character} is a character in the game {game}")


# print_game_character()  # Er ikke lov, vi må gi en verdi for "character"
print_game_character("Mario")
print_game_character("Peach")
print_game_character("Link", "The Legend of Zelda")
print_game_character("Apex Legends", "Pathfinder")  # Blir feil
print_game_character(game="Apex Legends",character="Pathfinder")