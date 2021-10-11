try:
    number1 = int(input("Type in a whole number: "))
    number2 = int(input("Type in another whole number: "))
    answer = number1 / number2
except ValueError:
    print("You have to enter a valid number")
except ZeroDivisionError:
    print("You can't enter zero")
else:
    print(f"The numbers {number1} / {number2} = {answer}")

