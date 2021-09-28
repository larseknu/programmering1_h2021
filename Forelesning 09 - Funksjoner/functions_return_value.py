from math import log


def including_tax(price, tax=0.25):
    price_with_tax = price + (price * tax)
    #print(f"The total price including tax will be {price_with_tax} NOK")
    return price_with_tax


price_excluding_tax = 100
price_including_tax = including_tax(price_excluding_tax)
print(f"The total price including tax will be {price_including_tax} NOK")



def dog_to_human_years(dog_age):
    """
    Dog to human years converter.
    The result is rounded to a full year.

    :param dog_age:
    :return: The dog's age in human years (rounded)
    """
    human_equivalent_age = 16 * log(dog_age) + 31
    return int(human_equivalent_age)


print(dog_to_human_years(20))
print(dog_to_human_years.__doc__)