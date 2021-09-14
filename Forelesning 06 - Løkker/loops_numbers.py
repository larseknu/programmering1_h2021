print("\nPrinting numbers from 0 to 10:")
for number in range(11):
    print(number)

print("\nPrinting numbers from 1 to 9:")
for number in range(1, 10):
    print(number)

print("\nPrinting numbers from 1000 to 9001:")
for number in range(1000, 9002):
    print(number)


print("\nPrinting numbers from 1000 to 9000, with interval of 1000:")
numbers = []
for number in range(1000, 9002, 1000):
    print(number)
    numbers.append(number)

print(f"\nMinimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

numbers = list(range(1, 101, 2))
print(f"\nMinimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")

print("Counting down with a while loop")
counter = 5
while counter > 0:
    print(counter)
    counter -= 1

while counter <= 5:
    print(counter)
    counter += 1
