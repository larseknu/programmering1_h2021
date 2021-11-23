favorite_numbers = {
    "john": 12,
    "klara": 9,
    "nils": 69,
    "camilla": 7,
    "emil": 1337,
}

print(favorite_numbers)

favorite_numbers["viktoria"] = 420

print(favorite_numbers)

print(f"John's favourite number is: {favorite_numbers['john']}")
print(f"Viktoria's favourite number is: {favorite_numbers['viktoria']}")

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favourite number is: {number}")
