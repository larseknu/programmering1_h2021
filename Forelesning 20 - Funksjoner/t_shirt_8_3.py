def make_shirt(size="large", message="I love Python!"):
    print(f'Done printing a {size} shirt with the message: "{message}"')


make_shirt("medium", "The meaning of life is 42!")
make_shirt(size="large", message="I love code!")
make_shirt("extra message", message="I also love code!")

make_shirt()
make_shirt(size="medium")
make_shirt(size="any size", message="A very long message about nothing!")

