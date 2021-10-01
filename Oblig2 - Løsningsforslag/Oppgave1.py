number = input("Hva er meningen med livet? ")
number = int(number)

if number == 42:
    print("Det stemmer, meningen med liver er 42!")
elif 30 < number < 50:
    print("Nærme, men feil!")
else:
    print("FEIL!")