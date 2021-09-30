import random


def print_header():
    print("\n==============================================")
    print("====What is your weight on another planet?====")
    print("==============================================")


def should_user_try_again():
    answer = input("\nDo you want to try again(Y/N)?  ")
    return answer.upper() == 'Y'


def pick_random_element_from_list(collection):
    random_number = random.randrange(0, len(collection))
    chosen_element = collection[random_number]
    return chosen_element


def calculate_weight(your_weight, planet_gravity, original_planet_gravity=9.807):
    calculated_weight = (your_weight / original_planet_gravity) * planet_gravity
    return round(calculated_weight, 2)


planets = [{'name': 'Random'},
           {'name': 'Mercury', 'gravity': 3.7},
           {'name': 'Venus', 'gravity': 8.87},
           {'name': 'Earth', 'gravity': 9.807},
           {'name': 'Mars', 'gravity': 3.721},
           {'name': 'Jupiter', 'gravity': 24.79},
           {'name': 'Saturn', 'gravity': 10.44},
           {'name': 'Uranus', 'gravity': 8.87},
           {'name': 'Neptune', 'gravity': 11.15}]

should_still_run = True

while should_still_run:
    print_header()

    for index, planet in enumerate(planets):
        print(f"{index} - {planet['name']}")

    planet_number = int(input("\nPick a planet by typing a number: "))

    # If input is 0 - pick random planet
    if planet_number == 0:
        chosen_planet = pick_random_element_from_list(planets)
    else:
        chosen_planet = planets[planet_number]

    print(f"\nYou got: {chosen_planet['name']} with a gravity of {chosen_planet['gravity']}")

    user_weight = float(input("\nType in your weight in kg on earth: "))

    your_weight_on_other_planet = calculate_weight(user_weight, chosen_planet['gravity'])

    print(f"\nYou will weigh {your_weight_on_other_planet}kg on the planet {chosen_planet['name']}")

    should_still_run = should_user_try_again()