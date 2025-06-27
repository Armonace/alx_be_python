class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: Human-readable format."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Used for debugging or recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
