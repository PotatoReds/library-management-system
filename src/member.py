# member class // self = itself, a reference to current instance of class // self.borrowed_books = [] = creates an empty list for borrowed_books attribute when a member is created
class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
        self.history = []

    # method to display member information in a structured return format
    def display_info(self):
        return f"{self.member_id} - {self.name}, Borrowed books: {self.borrowed_books}, Contact info: {self.email}"
    
    # method for borrowing a book, adds the book_id to member borrowed_books list // append = add to the list
    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)
        self.history.append(f"Borrowed: {book_id}")

    # method for returning a book, removes book_id from member borrowed_books list
    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            self.history.append(f"Returned: {book_id}")

    # method to display the borrowing and returning history of the member
    def display_history(self):
        return self.history