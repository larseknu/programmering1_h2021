board_games = ['Ubongo', 'Pandemic', 'Ticket To Ride', 'Monopoly', 'Mysterium',
               'Pandemic Legacy: Season 0', 'Pandemic Legacy: Season 1', 'Pandemic Legacy: Season 2']

# Får slice av lista på plass fra og med 4 og til 7
# Skriver ut denne
print(board_games[4:7])

# Oppretter en slice av lista på plass fra og med -3 og siste element
# Itererer gjennom denne direkte
for board_game in board_games[-3:]:
    print(board_game)

#Sorterer lista alfabetisk
board_games.sort()

# Lager en ny liste som referer til en slice av lista med de 3 første elementene
first_board_games = board_games[:3]
print(f"{first_board_games}")

# Henter ut annenhvert spill fra hele lista
print(board_games[::2])

print(board_games)

# Henter det 3. siste elementet i lista, som er "Pandemic Legacy: Season 2"
pandemic_legacy_s2 = board_games[-3]
# Vil gi oss tegnene fra plass 9-14 "Legacy"
print(f"\n{pandemic_legacy_s2[9:15]}")
# Henter ut det siste tegnet i strengen
print(f"\n{pandemic_legacy_s2[-1]}")
# Vil gi oss tegnene fra plass -8 til slutten av lista "Season 2"
print(f"\n{pandemic_legacy_s2[-8:]}")




