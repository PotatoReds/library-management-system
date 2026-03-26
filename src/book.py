# book class // Self = it self, a reference to the current instance of class, used to access attributes (variables) that belongs to the class
class Book:
    def __init__(self, book_id, title, author, year, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

# method (function within a class) to display book information
    def display_info(self):
        return f"{self.book_id} - {self.title} by {self.author}, year: {self.year}, copies available: {self.copies}" 