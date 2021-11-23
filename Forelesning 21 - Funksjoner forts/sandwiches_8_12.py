def order_sandwich(type_if_bread, *items, cheese):
    print(f"\nA {type_if_bread} sandwich with the following ingredients is being made:")
    for item in items:
        print(f"- {item}")

    if cheese:
        print("Adding lots of cheese...")

    print("The sandwich is done!")


order_sandwich("whole-wheat bread", "chicken", "tomato", "lettuce", cheese=True)
order_sandwich("loaf", "ham", "cheese", 1000, cheese=True)
order_sandwich("kneip","nutella", cheese=False)



