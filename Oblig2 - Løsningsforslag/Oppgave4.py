tolkien_books = ['Farmer Giles of Ham ', 'Lord of the Rings: The Fellowship of the Ring',
                 'Lord of the Rings: The Return of the King', 'Lord of the Rings: The Two Towers',
                 'The Adventures of Tom Bombadil', 'The Hobbit', 'The Silmarillion', 'Tree and Leaf',
                 'Unfinished Tales']

lotr_books = []

for book in tolkien_books:
    if "Lord of the Rings" in book:
        lotr_books.append(book)

print("Print with for-each:")
for book in lotr_books:
    print(book)

print("\nPrint with range:")
for index in range(0, len(lotr_books)):
    print(lotr_books[index])