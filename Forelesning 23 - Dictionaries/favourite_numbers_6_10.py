favorite_numbers = {
    "john": [12, 4],
    "klara": [9, 10],
    "nils": [69, 420],
    "camilla": [7],
    "emil": [1337, 9001, 42, 7, 13, 3, 0],
    "viktoria": [420, 240]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers is:")
    for number in numbers:
        print(f"\t\t- {number}")
