class Restaurant:
	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.name} serves food of the cuisine {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.name} is noe open! Welcome!")


genericfishrestaurant = Restaurant("the generic fish restaurant", "fish")
print(genericfishrestaurant.name)
print(genericfishrestaurant.cuisine_type)

genericfishrestaurant.describe_restaurant()
genericfishrestaurant.open_restaurant()

