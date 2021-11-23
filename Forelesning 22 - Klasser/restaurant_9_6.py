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


class IceCreamStand(Restaurant):
	def __init__(self, name, cuisine_type="ice cream"):
		super().__init__(name, cuisine_type)
		self.flavours = []

	def display_flavours(self):
		print(f"{self.name} has the flavours:")
		for flavour in self.flavours:
			print(f"- {flavour}")


if __name__ == '__main__':
	cherry_on_top = IceCreamStand("cherry on top")
	cherry_on_top.flavours = ["chocolate", "vanilla", "pistachio", "lollipop"]
	cherry_on_top.display_flavours()
	cherry_on_top.describe_restaurant()
