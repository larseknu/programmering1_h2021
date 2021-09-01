# Printer en string
print("A string")
# Også en string
print('Still a string')

# String med " som en del av den
print('We can put quotes inside a string: "First, solve the problem. Then, write the code." – John Johnson')
# String med ' som en del av den
print("With apostrophe: It's harder to read code than to write it. - Joel Spolsky")
# String med " og ' som en del av den
print('''Why not both?: "It's harder to read code than to write it." - Joel Spolsky''')

quote = "It's harder to read code than to write it."
author = "Joel Spolsky"
print("author")
print(author)

# Bruker variablene som en del av strengen vi printer
# , gjør at dataen til hver variabel printes "hver for seg"
print('A quote "', quote, '" -', author)
# + gjør at vi kombinerer alle string-verdiene (concatenate) og lager en hel string før den printes
# Dette fungerer bare når vi har string-verdier, ikke med f.eks. int
print('A quote "' + quote, '" -' + author)
# Bruker den innebygde print-format til å lage en streng med verdiene fra variablene
print(f'A quote: "{quote}" - {author}')
