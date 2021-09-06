# if <betingelse>:
    # Kjør koden her hvis betingelsen er oppfyllt
# elif <betingelse>:
    # Kjør koden her hvis betingelsen er oppfyllt (og IKKE den i den første if'en er oppfylt)
# else:
    # Kjør denne koden hvis betingelsen ikke er oppfyllt


number = 3
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")

print(f"End of program?")


dolphins_sleep_with_one_eye_open = True

if dolphins_sleep_with_one_eye_open:
    print("\nIt is true, dolphins DO sleep with one eye open.")
else:
    print("\nIt was a lie, dolphins don't sleep at all!")


x = 50
y = 10
is_x_bigger_than_y = y < x
if is_x_bigger_than_y:
    print(f"\nx ({x}) is bigger than y ({y}), let's fix that! Over 9000!")
    y += 9001
else:
    print(f"\nx ({x}) is smaller than y ({y}), everything is OK!")


first_name = "Lars Emil"
another_first_name = "lars emil"

if first_name.lower() == another_first_name.lower():
    print(f"\nThe names {first_name} and {another_first_name} are equal\n")
else:
    print(f"\nThe names {first_name} and {another_first_name} are NOT equal\n")


number = "ten"
if number == "ten":
    number = 10
print(number)


print(number < 9000 and number != 42)

number = 42
print(number < 9000 and number != 42)

print("Over 9000" if number > 9000 else "Under 9000")

a, b = 5, 10

smallest = a if a < b else b
print(smallest)