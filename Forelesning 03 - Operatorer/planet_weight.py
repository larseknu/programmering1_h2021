print("==== What is your weight on another planet? ====")
planet_name = input("What's the name of the planet? ")
planet_gravity = input("What's the gravity on the planet? ")
planet_gravity = float(planet_gravity)
your_weight = input("What's your weight on earth? ")
your_weight = float(your_weight)

earth_gravity = 9.807

your_mass = your_weight / earth_gravity
weight_on_other_planet = your_mass * planet_gravity
weight_on_other_planet = round(weight_on_other_planet, 2)

print(f"Your weight on {planet_name} is {weight_on_other_planet}kg")
