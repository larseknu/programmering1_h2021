# Lager en variabel med string'en "Moon"
moon = "Moon"
# Lager float variabler med tyngdekraften
earth_gravity = 9.807
moon_gravity = 1.622
# Lager int variabel med vekt
my_earth_weight = 85

# Regner ut vekten på månen
my_moon_weight = my_earth_weight / earth_gravity * moon_gravity

# Printer ut vekten på månen
print(f"My weight on the {moon} is {my_moon_weight}")

# Bruker input-funksjonen til å få data om vekt fra brukeren, legger dette i variabelen your_weight
# your_weight vil her bli en string, selv om det skrives inn tall
your_weight = input("Type in your weight: ")
# Regner ut brukeren sin vekt på månen, må her konvertere your_weight til et tall for å kunne regne med det
your_moon_weight = float(your_weight) / earth_gravity * moon_gravity

#print("Your weight on the " + moon + " is " + str(your_moon_weight))
print(f"Your weight on the {moon} is {your_moon_weight}")


