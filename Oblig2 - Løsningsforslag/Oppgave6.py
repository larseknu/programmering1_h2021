print("===============================")
print("=====Create package list=======")
print("===============================")

package_list = ["Towel", "Wallet", "A worn out shoesole"]

should_still_pack = True

while should_still_pack:
    print("\nCommands:")
    print("A - Add to the list")
    print("D - Delete from the list")
    print("P - Print the current list")
    print("Q - Quit the program")

    command = input("Pick a command: ")

    if command == 'A':
        item_to_add = input("What to add: ")
        package_list.append(item_to_add)
        print(f"{item_to_add} added to the list")
    elif command == 'D':
        delete_item = input("What to delete: ")
        if delete_item in package_list:
            package_list.remove(delete_item)
            print(f"{delete_item} removed from the list")
        else:
            print(f"{delete_item} does not exist in the list\n")
    elif command == 'P':
        print("\nItems in the package list:")
        for item in package_list:
            print(item)
    elif command == 'Q':
        should_still_pack = False
    else:
        print("\nYou typed in an invalid command, pleas try again!")
