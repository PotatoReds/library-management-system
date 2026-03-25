class Member:
    def __init__(self, member_id, name, email, borrowed_books):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books = []

    def display_info(self):
        return f"{self.member_id} - {self.name}, Borrowed books: {self.borrowed_books}"
        return f"Contact info: {self.email}"
    
    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)