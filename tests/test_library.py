# import of unittest framework and necessary classes from src folder for testing
import unittest
from src.book import Book
from src.member import Member
from src.library import Library

# Test class for Library, using unittest framework
class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("A00001", "The Fellowship of the Ring", "J.R.R. Tolkien", 1954, 5)
        self.member = Member("X00001", "Jonathan S. Jacobsen", "joj009@edu.zealand.dk")

        self.library.add_book(self.book)
        self.library.add_member(self.member)

# test method to check if a book is added to the liberary
    def test_add_book(self):
        self.assertIn("A00001", self.library.books)
        
# test method to check if a member is added to the library
    def test_issue_book(self):
        self.library.issue_book("A00001", "X00001")
        self.assertEqual(self.book.copies, 4)
        self.assertIn("A00001", self.member.borrowed_books)

# test method to check if a book is returned to the library
    def test_return_book(self):
        self.library.issue_book("A00001", "X00001")
        self.library.return_book("A00001", "X00001")
        self.assertEqual(self.book.copies, 5)
        self.assertNotIn("A00001", self.member.borrowed_books)

# test method to check if a book cannot be issued when there are no copies available
    def test_issue_unavailable_book(self):
        self.book.copies = 0
        self.library.issue_book("A00001", "X00001")
        self.library.issue_book("A00001", "X00001")
        self.assertEqual(self.book.copies, 0)

# test method to check if a book cannot be issued when the book_id is not found in the library
    def test_book_not_found(self):
        self.library.issue_book("Z9999", "X00001")
        self.assertEqual(self.book.copies, 5)

# test method to check if a book cannot be issued when the member_id is not found in the library
    def test_member_not_found(self):
        self.library.issue_book("A00001", "Z9999")
        self.assertEqual(self.book.copies, 5)

# test method to check if a book cannot be returned when the book_id is not found in the library
    def test_return_not_borrowed(self):
        self.library.return_book("A00001", "X00001")
        self.assertEqual(self.book.copies, 5)

if __name__ == '__main__':
    unittest.main()