from src.library import Library
from src.book import Book
from src.member import Member

library = Library()
library.load_books()
library.load_members()

# CLI menu for library management system, allows user to interact with the library by choosing options from the menu
while True:
    print ("\n -- Library Menu --")
    print("1. Display Books")
    print("2. Display Members")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. Search Members")
    print("7. Add Book")
    print("8. Add Member")
    print("9. Remove Book")
    print("10. Remove Member")
    print("11. Update Book")
    print("12. Update Member")
    print("13. Show Member History")
    print("14. Exit")
    
    choice = input("Enter your choice (1-14): ")

# choice 1, display books
    if choice == "1":
        print("\nBooks in Library:")
        for book in library.display_books():
            print(book)

# choice 2, display members
    elif choice == "2":
        print("\nLibrary Members:")
        for member in library.display_members():
            print(member)
            
# choice 7, add books to library
    elif choice == "7":
        book_id = input("Enter book ID:")
        title = input("Enter book title:")
        author =input("Enter author name:")

        year_input = input("Enter publication year:")
        if not year_input.isdigit():
            print("Invalid year. Please enter a valid number.")
            continue
        year = int(year_input)
        
        copies_input = input("Enter number of copies available:")
        if not copies_input.isdigit():
            print("Invalid number of copies. Please enter a valid number.")
            continue
        copies = int(copies_input)

        book = Book(book_id, title, author, year, copies)
        library.add_book(book)
        library.save_books()

        print("Book added successfully.")

# choice 8, add member to library
    elif choice == "8":
        member_id = input("Enter member ID:")
        name = input("Enter member name:")
        email = input("Enter member email:")

        member = Member(member_id, name, email)
        library.add_member(member)
        library.save_members()

        print("Member added successfully.")

# choice 14, exit the program
    elif choice == "14":
        print("Exiting the library management system. Goodbye!")
        library.save_books()
        library.save_members()
        break