videogames = ['Legend of Zelda', 'Tetris', 'Mario Bros.', 'Apex Legends']
print(videogames)

random_list = ["Lars Emil", 42, 3.14, False, 1000]
print(random_list)

print(videogames[0])
print(videogames[2])
print(videogames[-1])

videogames[2] = 'Super Mario Bros.'
print(videogames)

videogames.append("Fortnite")
print(videogames)

videogames.insert(1, "Dark Souls")
print(videogames)

videogames.pop()  # Tar bort siste element i lista
print(videogames)

print(videogames.pop(2))  # Tar bort element nummer 2 i lista
print(videogames)

videogames.remove("Dark Souls")  # Tar bort element med samme verdi
print(videogames)

print(f"The length of the list is {len(videogames)}")

videogames.reverse()
print(videogames)

videogames_sorted = sorted(videogames)
print(f"Sorted list: {videogames_sorted}")
print(f"Original list: {videogames}")

videogames.sort()
print(videogames)
