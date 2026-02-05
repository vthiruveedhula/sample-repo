class Book:
    favs = []

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title}, {self.pages} pages long.!!!!!!!"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

    __hash__ = None

    def is_short(self):
        return self.pages < 60


book = Book("Goodnight Moon", 30)
print(book)
print(book.is_short())
Book.favs.append(book)

book2 = Book("Are You my Mother?", 72)
print(book2)
print(book2.is_short())
Book.favs.append(book2)

print(Book.favs)