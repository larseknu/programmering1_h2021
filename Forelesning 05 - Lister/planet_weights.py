print("================================================")
print("==== What is your weight on another planet? ====")
print("================================================")

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

print("=====Planets======")
print(f"1 - {planets[0]}")
print(f"2 - {planets[1]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")

planet_number = input("\nPick a planet by typing in a number: ")
planet_number = int(planet_number)-1
if 0 > planet_number > len(planets):
    print(f"The number you entered is outside the required range")
    exit()

print(f"\nYou picked {planets[planet_number]}")

your_weight = input("\nType in your weight in kg: ")
your_weight = int(your_weight)

your_mass = your_weight / planets_gravity[2]
your_weight = your_mass * planets_gravity[planet_number]

print(f"You will weigh {round(your_weight, 2)}kg on the planet {planets[planet_number]} with a gravity of {planets_gravity[planet_number]}m/s\u00b2")
