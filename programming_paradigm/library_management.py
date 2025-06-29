class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


# Main execution
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)

    # After Initial Setup
    print("Available books after setup:")
    library.list_available_books()

    # After Checking Out '1984'
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # After Returning '1984'
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
