class Restaurant:
	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.name} serves food of the cuisine {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.name} is noe open! Welcome!")


genericfishrestaurant = Restaurant("the generic fish restaurant", "fish")
genericfishrestaurant.describe_restaurant()

thairestaurant = Restaurant("the thai palace", "thai")
olivegarden = Restaurant("the olive garden", "italian")
olivegardennewyork = Restaurant("the olive garden", "italian")

thairestaurant.describe_restaurant()
olivegarden.describe_restaurant()
olivegardennewyork.name = "The Olive Garden NY"
olivegardennewyork.describe_restaurant()




