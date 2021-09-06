print("==== What is your weight on another planet? ====")
your_weight = input("What's your weight on earth (in whole kg)? ")
if your_weight.isnumeric():
    your_weight = int(your_weight)
else:
    print(f'"{your_weight}" is not a valid weight.')
    exit()

if your_weight <= 0:
    print(f"Your weight of {your_weight}kg is not positive, please enter a positive number.")
    exit()
elif your_weight > 700:
    print(f"{your_weight}kg is either a world record, or you're lying.")
    exit()

planet_name = input("What's the name of the planet? ")
if planet_name == "Pluto":
    print("Pluto is not really a planet, but OK.")

planet_gravity = input("What's the gravity on the planet? ")
planet_gravity = float(planet_gravity)
if planet_gravity <= 0:
    print(f"The gravity of {planet_gravity} can't be a negative number.")
    exit()

earth_gravity = 9.807

if planet_gravity < earth_gravity:
    print(f"{planet_name} has a low gravity")
elif planet_gravity == earth_gravity:
    print(f"{planet_name} has the same gravity as Earth. Are you in a parallel universe?")
elif planet_gravity < earth_gravity * 5:
    print(f"{planet_name} has a heavy gravity")
else:
    print(f"{planet_name} has an insane gravity. Are you sure you're not on a star?")




your_mass = your_weight / earth_gravity
weight_on_other_planet = your_mass * planet_gravity
weight_on_other_planet = round(weight_on_other_planet, 2)

print(f"\n\n\t\tYour weight on {planet_name} with a gravity of {planet_gravity}m/s is {weight_on_other_planet}kg")