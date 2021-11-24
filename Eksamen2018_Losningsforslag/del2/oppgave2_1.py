def print_number_once(numbers):
	printed_before = []
	for number in numbers:
		if number not in printed_before:
			print(number)
			printed_before.append(number)


tall = [2, 4, 2, 4, 1, 2, 5, 6, 5]

print_number_once(tall)