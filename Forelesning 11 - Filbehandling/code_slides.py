try:
    number = int("42")  # int("a_string")
except ValueError:
    print(f"That is not a valid integer!")
else:
    print(f"{number*2} is a nice number")

