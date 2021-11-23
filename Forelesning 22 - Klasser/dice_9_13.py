from random import randint


class Die:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		return randint(1, self.sides)

	def roll_dice(self, number_of_times):
		print(f"Rolling d{self.sides} 10 times: ")
		for i in range(number_of_times):
			print(self.roll_die())


def roll_dice(die, number_of_times):
	print(f"Rolling d{die.sides} 10 times: ")
	for i in range(number_of_times):
		print(die.roll_die())

d6 = Die()
d6.roll_dice(10)

d10 = Die(10)
roll_dice(d10, 10)

d20 = Die(20)
roll_dice(d20, 100)