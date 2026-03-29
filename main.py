# This is the main entry point for the library management system. It provides a command-line interface (CLI) for users to interact with the library.
# // Final Version
from src.library import Library
from src.book import Book
from src.member import Member

# create library instance and load books and members from files
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
# displays the list of books in the library by calling the display_books method of the library object and printing each book's information to the console
    if choice == "1":
        print("\nBooks in Library:")
        for book in library.display_books():
            print(book)

# choice 2, display members
# displays the list of members in the library by calling the display_members method of the library object and printing each member's information to the console
    elif choice == "2":
        print("\nLibrary Members:")
        for member in library.display_members():
            print(member)

# choice 3, issue book to member
# prompts user to enter book ID and member ID, processes the issuing of the book to the member, updates the library's records accordingly, saves the updated information to the files and informs the user of the result of the issuing operation
    elif choice == "3":
        book_id = input("Enter book ID to issue:")
        member_id = input("Enter member ID to issue to:")

        message = library.issue_book(book_id, member_id)
        library.save_books()
        library.save_members()

        print(message)

# choice 4, return book from member
# prompts user to enter book ID and member ID, processes the return of the book from the member, updates the library's records accordingly, saves the updated information to the files and informs the user of the result of the return operation
    elif choice == "4":
        book_id = input("Enter book ID to return:")
        member_id = input("Enter member ID returning the book:")

        message = library.return_book(book_id, member_id)
        library.save_books()
        library.save_members()

        print(message)

# choice 5, search for books by title, author or year
# prompts user to enter a keyword, searches for books in the library whose title, author or publication year contains the keyword, and displays the search results. If no books are found matching the keyword, informs the user.
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
# prompts user to enter a keyword, searches for members in the library whose name or email contains the keyword, and displays the search results. If no members are found matching the keyword, informs the user.
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
# prompts user to enter book ID, title, author, publication year and number of copies, creates a new book object with the provided information, adds the book to the library's books dictionary, saves the updated book information to the file and informs the user that the addition was successful
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
# prompts user to enter member ID, name and email, creates a new member object with the provided information, adds the member to the library's members dictionary, saves the updated member information to the file and informs the user that the addition was successful
    elif choice == "8":
        member_id = input("Enter member ID:")
        name = input("Enter member name:")
        email = input("Enter member email:")

        member = Member(member_id, name, email)
        library.add_member(member)
        library.save_members()

        print("Member added successfully.")

# choice 9, remove book from library
# prompts user to enter book ID, checks if book exists in library, if it does, removes the book from the library's books dictionary, saves the updated book information to the file and informs the user that the removal was successful
    elif choice == "9":
        book_id = input("Enter book ID to remove:")
        library.remove_book(book_id)
        library.save_books()

        print("Book removed successfully.")

# choice 10, remove member from library
# prompts user to enter member ID, checks if member exists in library, if it does, removes the member from the library's members dictionary, saves the updated member information to the file and informs the user that the removal was successful
    elif choice == "10":
        member_id = input("Enter member ID to remove:")
        library.remove_member(member_id)
        library.save_members()

        print("Member removed successfully.")

# choice 11, update book information
# prompts user to enter book ID, new title, new author, new publication year and new number of copies, checks if book exists in library, if it does, updates the book's information with the new values provided by the user (if they are not left blank), saves the updated book information to the file and informs the user that the update was successful
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
# prompts user to enter member ID, new name and new email, checks if member exists in library, if it does, updates the member's name and email with the new values provided by the user (if they are not left blank), saves the updated member information to the file and informs the user that the update was successful
    elif choice == "12":
        member_id = input("Enter member ID to update:")
        name = input("Enter new name (leave blank to keep current):")
        email = input("Enter new email (leave blank to keep current):")

        library.update_member(member_id, name=name if name else None, email=email if email else None)

        library.save_members()
        print("Member information updated successfully.")

# choice 13, show member history
# prompts user to enter member ID, checks if member exists in library, if it does, retrieves and displays the borrowing and returning history of the member, if no history is available, informs the user
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
# saves the current state of books and members to their respective files before exiting the program, ensuring that any changes made during the session are preserved for future use
    elif choice == "14":
        print("Exiting the library management system. Goodbye!")
        library.save_books()
        library.save_members()
        break