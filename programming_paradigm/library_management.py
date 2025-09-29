# library_management.py

class Book:
    """
    Represents a book with a title and author.
    Public attributes:
      - title
      - author
    Private attribute:
      - _is_checked_out : bool
    """

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """
        Mark the book as checked out.
        Returns True if checkout succeeded (book was available), False if already checked out.
        """
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """
        Mark the book as returned (available).
        Returns True if return succeeded (book was checked out), False if it was already available.
        """
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """
    Manages a collection of Book instances.
    Private attribute:
      - _books : list[Book]
    """

    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        """Add a Book instance to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("add_book expects a Book instance")

    def check_out_book(self, title: str) -> bool:
        """
        Attempt to check out a book by title.
        Returns True if checkout succeeded, False if book not found or already checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title: str) -> bool:
        """
        Attempt to return a book by title.
        Returns True if return succeeded, False if book not found or wasn't checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self) -> None:
        """
        Print all available books, each on its own line in the format:
          Title by Author
        If no books are available, nothing is printed.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
