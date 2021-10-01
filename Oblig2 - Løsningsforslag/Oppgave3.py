tolkien_books = ['The Hobbit', 'Farmer Giles of Ham ', 'The Fellowship of the Ring','The Two Towers',
                 'The Return of the King', 'The Adventures of Tom Bombadil', 'Tree and Leaf',]

print("Two first Tolkien books:")
print(tolkien_books[0])
print(tolkien_books[1])

print("\nTwo last Tolkien books:")
print(tolkien_books[-1])
print(tolkien_books[-2])

# Adding two books
tolkien_books.append("The Silmarillion")
tolkien_books.append("Unfinished Tales")

# Changing the 3 LOTR books to include "Lord of the Rings
lotr = "Lord of the Rings: "
for index in range(2, 5):
    tolkien_books[index] = lotr + tolkien_books[index]

tolkien_books.sort()

print("\nTolkien books:")
print(tolkien_books)