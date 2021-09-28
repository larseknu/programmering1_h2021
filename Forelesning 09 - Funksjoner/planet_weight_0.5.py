import random


def print_header():
    print("\n==============================================")
    print("====What is your weight on another planet?====")
    print("==============================================")


def print_list_of_planets(planets_to_print):
    print("0 - Random Planet")
    for index, planet in enumerate(planets_to_print):
        print(f"{index+1} - {planet}")


def user_input_to_index(input_message_to_user):
    number = input(input_message_to_user)
    index = int(number) - 1  # Get the correct index
    return index


def pick_random_element_from_list(collection):
    index = random.randrange(0, len(collection))
    chosen_element = collection[index]
    return chosen_element


def calculate_weight(your_weight, planets_gravity, original_planet_gravity=9.807):
    calculated_weight = (your_weight / original_planet_gravity) * planets_gravity
    return round(calculated_weight, 2)


def should_user_try_again():
    answer = input("\nDo you want to try again(Y/N)?  ")
    return answer.upper() != 'Y'


planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
planets_gravity = 3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15

close = False

while not close:
    print_header()

    print_list_of_planets(planets)

    planet_number = user_input_to_index("\nPick a planet by typing a number: ")

    #If input is 0 - pick random planet
    if planet_number == -1:
        chosen_planet = pick_random_element_from_list(planets)
        print(f"\nYou got: {chosen_planet}")
    else:
        chosen_planet = planets[planet_number]
        print(f"\nYou picked: {chosen_planet}")

    user_weight = float(input("\nType in your weight in kg on earth: "))

    your_weight_on_other_planet = calculate_weight(user_weight, planets_gravity[planet_number])

    print(f"\nYou will weigh {your_weight_on_other_planet}kg on the planet {chosen_planet}")

    close = should_user_try_again()
