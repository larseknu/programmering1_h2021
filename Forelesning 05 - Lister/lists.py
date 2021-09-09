# Creates a list containing some of the planets in our solar system
planets = ['Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturne', 'Uranus']

# Printing the list directly
print(planets)

# Printing the first planet (index starts at 0)
print(planets[0])

# Printing the first planet in capital letters
print(planets[0].upper())

# Changing the planet on index 4, and correcting the spelling mistake
planets[4] = 'Saturn'
print(f"\nAfter correction: {planets}")

# Appending planets to the end of the list
planets.append('Neptune')
planets.append('Pluto')
planets.append('Eris')
planets.append('Makemake')
print(f"\nAfter append: {planets}")

# Inserting planet at a specific index
planets.insert(3, 'Mars')
planets.insert(3, 'Mars')
planets.insert(3, 'Tellus')
print(f"\nAfter insert: {planets}")

# Popping planets from the end of the list(removing them from the list)
planets.pop()
print(f"\nAfter pop: {planets}")
print(planets.pop())  # Will print the value since pop-returns the element
print(f"After pop: {planets}")

# Popping planets from a specific index (removing them from the list)
planets.pop(3)
print(f"After pop: {planets}")

# Removing planets, when we know the name (first occurrence will be removed)
planets.remove('Mars')
print(f"\nAfter remove: {planets}")
print(planets.remove('Pluto'))  # Will print 'None' since remove doesn't return a value
print(f"After remove: {planets}")


