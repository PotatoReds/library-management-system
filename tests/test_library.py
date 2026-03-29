# This file contains test cases for the Library class, using the unittest framework. // Final Version
# It tests adding books and members, issuing and returning books, searching for books and members, updating book and member information, removing books and members, and checking member history.
import unittest
from src.book import Book
from src.member import Member
from src.library import Library

# Test cases for the Library class, using unittest framework
class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("A00001", "The Fellowship of the Ring", "J.R.R. Tolkien", 1954, 5)
        self.member = Member("X00001", "Jonathan S. Jacobsen", "joj009@edu.zealand.dk")

        self.library.add_book(self.book)
        self.library.add_member(self.member)
# test cases for adding a book, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_add_book(self):
        self.assertIn("A00001", self.library.books)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_issue_book(self):
        message = self.library.issue_book("A00001", "X00001")
        self.assertEqual(message, "Book issued successfully.")
        self.assertEqual(self.book.copies, 4)
        self.assertIn("A00001", self.member.borrowed_books)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_return_book(self):
        self.library.issue_book("A00001", "X00001")
        message = self.library.return_book("A00001", "X00001")
        self.assertEqual(message, "Book returned successfully.")
        self.assertEqual(self.book.copies, 5)
        self.assertNotIn("A00001", self.member.borrowed_books)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_issue_unavailable_book(self):
        self.book.copies = 0
        message = self.library.issue_book("A00001", "X00001")
        self.assertEqual(message, "No copies available for this book.")
        self.assertEqual(self.book.copies, 0)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_book_not_found(self):
        message = self.library.issue_book("Z9999", "X00001")
        self.assertEqual(message, "Book not found in library.")
        self.assertEqual(self.book.copies, 5)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_member_not_found(self):
        message = self.library.issue_book("A00001", "Z9999")
        self.assertEqual(message, "Member not found in library.")
        self.assertEqual(self.book.copies, 5)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_return_not_borrowed(self):
        message = self.library.return_book("A00001", "X00001")
        self.assertEqual(message, "This member did not borrow this book.")
        self.assertEqual(self.book.copies, 5)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_search_books(self):
        results = self.library.search_books("Tolkien")
        self.assertEqual(len(results), 1)
        self.assertIn("The Fellowship of the Ring", results[0])

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_search_members(self):
        results = self.library.search_members("Jonathan")
        self.assertEqual(len(results), 1)
        self.assertIn("Jonathan S. Jacobsen", results[0])

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_update_book(self):
        self.library.update_book("A00001", title="LOTR", copies=3)
        self.assertEqual(self.book.title, "LOTR")
        self.assertEqual(self.book.copies, 3)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_update_member(self):
        self.library.update_member("X00001", name="Jon", email="jon@email.com")
        self.assertEqual(self.member.name, "Jon")
        self.assertEqual(self.member.email, "jon@email.com")

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_remove_book(self):
        self.library.remove_book("A00001")
        self.assertNotIn("A00001", self.library.books)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history
    def test_remove_member(self):
        self.library.remove_member("X00001")
        self.assertNotIn("X00001", self.library.members)

# test cases for adding a member, issuing a book, returning a book, searching for books and members, updating book and member information, removing books and members, and checking member history

    def test_member_history(self):
        self.library.issue_book("A00001", "X00001")
        self.library.return_book("A00001", "X00001")
        self.assertIn("Borrowed: A00001", self.member.history)
        self.assertIn("Returned: A00001", self.member.history)

# if this file is run directly, run the test cases
if __name__ == "__main__":
    unittest.main()