from restaurant_9_6 import Restaurant, IceCreamStand

olivegarden = Restaurant("olive garden", "italian")
olivegarden.describe_restaurant()

cherry_on_top = IceCreamStand("cherry on top")
cherry_on_top.flavours = ["chocolate", "vanilla", "pistachio", "lollipop"]
cherry_on_top.display_flavours()
cherry_on_top.describe_restaurant()