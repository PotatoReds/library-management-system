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

# choice 3, issue book to member
    elif choice == "3":
        book_id = input("Enter book ID to issue:")
        member_id = input("Enter member ID to issue to:")

        message = library.issue_book(book_id, member_id)
        library.save_books()
        library.save_members()

        print(message)

# choice 4, return book from member
    elif choice == "4":
        book_id = input("Enter book ID to return:")
        member_id = input("Enter member ID returning the book:")

        message = library.return_book(book_id, member_id)
        library.save_books()
        library.save_members()

        print(message)

# choice 5, search for books by title, author or year
    elif choice == "5":
        keyword = input("Enter keyword to search for books (title, author, or year): ")
        results = library.search_books(keyword)

        if results:
            print("\nSearch Results:")
            for book in results:
                print(book)
        
        else:
            print("No books found matching the keyword.")

# choice 6, search for members by name or email
    elif choice == "6":
        keyword = input("Enter keyword to search for members (name or email):")
        results = library.search_members(keyword)

        if results:
            print("\nSearch Results:")
            for member in results:
                print(member)

        else:
            print("No members found matching the keyword.")

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

# choice 9, remove book from library
    elif choice == "9":
        book_id = input("Enter book ID to remove:")
        library.remove_book(book_id)
        library.save_books()

        print("Book removed successfully.")

# choice 10, remove member from library
    elif choice == "10":
        member_id = input("Enter member ID to remove:")
        library.remove_member(member_id)
        library.save_members()

        print("Member removed successfully.")

# choice 11, update book information
    elif choice == "11":
        book_id = input("Enter book ID to update:")
        title = input("Enter new title (leave blank to keep current):")
        author = input("Enter new author (leave blank to keep current):")
        year_input = input("Enter new publication year (leave blank to keep current):")
        copies_input = input("Enter new number of copies (leave blank to keep current):")

        year = int(year_input) if year_input.isdigit() else None
        copies = int(copies_input) if copies_input.isdigit() else None

        library.update_book(book_id, title=title if title else None, author=author if author else None, year=year, copies=copies)

        library.save_books()
        print("Book information updated successfully.")

# choice 12, update member information
    elif choice == "12":
        member_id = input("Enter member ID to update:")
        name = input("Enter new name (leave blank to keep current):")
        email = input("Enter new email (leave blank to keep current):")

        library.update_member(member_id, name=name if name else None, email=email if email else None)

        library.save_members()
        print("Member information updated successfully.")

# choice 13, show member history
    elif choice == "13":
        member_id = input("Enter member ID to view history:")
        
        if member_id in library.members:
            history = library.members[member_id].display_history()

            if history:
                print("\nMember History:")
                for entry in history:
                    print(entry)

            else:
                print("No history available for this member.")
        else:
            print("Member not found in library.")

# choice 14, exit the program
    elif choice == "14":
        print("Exiting the library management system. Goodbye!")
        library.save_books()
        library.save_members()
        break