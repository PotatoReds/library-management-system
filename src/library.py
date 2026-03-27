import json

from src.book import Book
from src.member import Member

# library class // manages books and members, allows adding, removing, updating books and members, issuing and returning books, and displaying information about books and members
# {} = stores values // [] = list of values
class Library: 
    def __init__(self):
        self.books = {}
        self.members = {}
        self.history = []

# method to add book to the library, takes a book object as parameter and adds it to the books dictionary with book_id
    def add_book(self, book):
        self.books[book.book_id] = book

# method to remove book from the library, takes book_id as parameter and removes the book from the books dictionary if it exists
    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

# method to update book informations // takes book_id and parameters for title, author, year and copies,
# checks if book_id exists in books dictionary, if it does, updates the attributes of the book object
    def update_book(self, book_id, title=None, author=None, year=None, copies=None):
        if book_id in self.books:
            book = self.books[book_id]
            if title:
                book.title = title
            if author:
                book.author = author
            if year is not None:
                book.year = year
            if copies is not None:
                book.copies = copies

# method to add members to the library, takes a member object as parameter and adds it to the members dictionary with member_id
    def add_member(self, member):
        self.members[member.member_id] = member

# method to remove members from the library
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
    
# method to update member information, takes member_id and parameters for name and email, checks if member_id exists in members dictionary, if it does, updates the attributes of the member object
    def update_member(self, member_id, name=None, email=None):
        if member_id in self.members:
            member = self.members[member_id]
            if name:
                member.name = name
            if email:
                member.email = email

# method to issueing a book to a member, takes book_id and member_id as parameters, checks if both book_id and member_id exist in their respective dictionaries,
#  if they do, checks if the book has available copies, if it does, decreases the number of copies by 1 and adds the book_id to the member's borrowed_books list
    def issue_book(self, book_id, member_id):
        if book_id not in self.books:
            print("Book not found in library.")
            return
        
        if member_id not in self.members:
            print ("Member not found in library.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book.copies <= 0:
            print("No copies available for this book.")
            return
        
        book.copies -= 1
        member.borrow_book(book_id)

# method for returning a book, takes book_id and member_id as parameters, checks if both book_id and member_id exist in their respective dictionaries,
# if they do, increases the number of copies of the book by 1 and removes the book_id from the member's borrowed_books list
    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            print("Book not found in library.")
            return
        
        if member_id not in self.members:
            print ("Member not found in library.")
            return
        
        book = self.books[book_id]
        member = self.members[member_id]

        if book_id not in member.borrowed_books:
            print("This member did not borrow this book.")
            return
                
        book.copies += 1
        member.return_book(book_id)


# method to display all books in the library, returns a list of book information by calling the display_info method of each book object in the books dictionary
    def display_books(self):
        return [book.display_info() for book in self.books.values()]
    
# method to display all members in the library, returns a list of member information by calling the display_info method of each member object in the members dictionary
    def display_members(self):
        return [member.display_info() for member in self.members.values()]
    
# method to search for books by title or author, takes a keyword as parameter, 
# checks if the keyword is present in the title or author of each book in the books dictionary
# if a match is found, adds the book information to the results list and returns it
    def search_books(self, keyword):
        results = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book.display_info())
        return results

# method to save books to a json file, creates a dictionary of book_id and book attributes using __dict__ and saves it to "books.json"
    def save_books(self):
        with open("books.json", "w") as f:
            json.dump({book_id: book.__dict__ for book_id, book in self.books.items()}, f)

#method to load books from a json file, reads the "books.json" file and creates book objects from the data, adding them to the books dictionary
    def load_books(self):
        try:
            with open("books.json", "r") as f:
                books_data = json.load(f)
                for book_id, book_info in books_data.items():
                    self.books[book_id] = Book(**book_info)
        except FileNotFoundError:
            print("No saved books found.")

# method to save members to a json file, creates a dictionary of member_id and member attributes using __dict__ and saves it to "members.json"
    def save_members(self):
        with open("members.json", "w") as f:
            json.dump({member_id: member.__dict__ for member_id, member in self.members.items()}, f)

# method to load members from a json file, reads the "members.json" file and creates member objects from the data, adding them to the members dictionary
    def load_members(self):
        try:
            with open("members.json", "r") as f:
                members_data = json.load(f)
                for member_id, member_info in members_data.items():
                    member = Member(member_info["member_id"], member_info["name"], member_info["email"])

                    member.borrowed_books = member_info.get("borrowed_books", [])
                    member.history = member_info.get("history", [])
                    self.members[member_id] = member

        except FileNotFoundError:
            print("No saved members found.")
            pass
                        
    def load_members(self):
        try:
            with open("members.json", "r") as f:
                members_data = json.load(f)
                for member_id, member_info in members_data.items():
                    self.members[member_id] = Member(**member_info)
        except FileNotFoundError:
            print("No saved members found.")
            pass