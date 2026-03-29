# This is a playground file for testing the functionality of the library management system.
# // Final Version
from src.book import Book
from src.member import Member
from src.library import Library

# create library instance
library = Library()

# create book instances (books with book_id, title, author, year and copies // book_id is given a letter to differentiate categories for future categorization possibilities)
book1 = Book("A00001", "The Fellowship of the Ring", "J.R.R. Tolkien", 1954, 5)
book2 = Book("A00002", "The Two Towers", "J.R.R. Tolkien", 1954, 6)
book3 = Book("A00003", "The Return of the King", "J.R.R. Tolkien", 1955, 4)
book4 = Book("B00001", " Computer Networking: A Top-Down Approach", "James F. Kurose and Keith W. Ross", 2017, 3)
book5 = Book("B00002", "C how to program", "Paul Deitel and Harvey Deitel", 2022, 2)
book6 = Book("B00003", "Projektledelse", "Niels Vestergaard, Susanne Muusmann Lassen", 2019, 4)
book7 = Book("B00004", "Arduino Cookbook", "Michael Margolis", 2020, 5)

# create member instances (members with member_id, name and email)
member1 = Member("X00001", "Jonathan S. Jacobsen", "joj009@edu.zealand.dk")

#add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)

# add members to library
library.add_member(member1)

# issue a book to a member
library.issue_book("Z9999", "X00001")

# display library books and members
print()
print("Awesome Library has the following books available:")
print(library.display_books())
print()
print("Library members:")
for member in library.display_members():
    print(member)

# return a book from a member
library.return_book("A00002", "X00001")

print()
print("After returning:")
for book in library.display_books():
    print(book)

# display member information and history
print()
for member in library.display_members():
    print(member)

# search for books by title, author or year
print()
print("Search results for 'Tolkien':")
for result in library.search_books("Tolkien"):
    print(result)

# issue and return a book to demonstrate history tracking
library.issue_book("A00001", "X00001")
library.return_book("A00001", "X00001")

# search for members by name or email
print()
print("Member history:")
for entry in member1.display_history():
    print(entry)

