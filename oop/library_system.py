# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def get_details(self):
        return f"{self.title} by {self.author} [E-Book, {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"{self.title} by {self.author} [Print Book, {self.page_count} pages]"


class Library:
    def __init__(self):
        self.books = []  # composition: contains Book, EBook, PrintBook instances

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        for book in self.books:
            print(book.get_details())
