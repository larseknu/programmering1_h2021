#if
number = 5
if number == 5:
    print("The number is 5.")
    
number = 89
if number == 5:
    print("The number is 5.")
    

#else
number = 89
if number == 5:
    print("The number is 5.")
else:
    print("The number is not 5.")
    
    
#elif (else if)
number = 89
if number == 5:
    print("The number is 5.")
elif number == 89:
    print("The number is 89.")
else:
    print("The number is not 5 or 89.")

#if, elif og else henger sammen
number = 89
if number == 5:
    print("The number is 5.")
elif number == 89:
    print("The number is 89.")
elif number == 89:
    print("The number is 89.")
else:
    print("The number is not 5 or 89.")
    
number = 1
if number == 1:
    print("The number is 1.")
if number == 1:
    print("The number is 1 again.")
    
number = 89
if number == 5:
    print("The number is 5.")
elif number == 89:
    print("The number is 89.")
print("something...")
else:
    print("The number is not 5 or 89.")
    
#Innholdet i en if-test kan være hva som helst
number = 10
if number == 10:
    number_plus_five = number + 5
    print("10 plus 5 is", number_plus_five)
    
number = "ten"
if number == "ten":
    number = 10
print(number)