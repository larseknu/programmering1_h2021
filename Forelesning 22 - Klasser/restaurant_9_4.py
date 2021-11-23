class Restaurant:
	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"{self.name} serves food of the cuisine {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.name} is noe open! Welcome!")

	def set_number_served(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, people_served):
		self.number_served += people_served


olivegarden = Restaurant("the olive garden", "italian")
print(f"The restaurant has served: {olivegarden.number_served} customers.")
olivegarden.set_number_served(50)
print(f"The restaurant has served: {olivegarden.number_served} customers.")
olivegarden.increment_number_served(200)  # Day 2
olivegarden.increment_number_served(400)  # Day 3
print(f"The restaurant has served: {olivegarden.number_served} customers.")


