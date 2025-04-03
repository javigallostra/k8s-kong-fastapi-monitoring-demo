from app.models.books import Book
from app.repositories.common import BookRepository


class BookService:

    def __init__(self, repository: BookRepository) -> None:
        self._repository = repository

    def get_book_list(self) -> list[Book]:
        return self._repository.list_books()

    def get_book(self, ISBN: str) -> Book | None:
        return self._repository.get_book(ISBN)

    def add_book(self, book: Book) -> None:
        """Raise ValueError if the book already exists."""
        if self._repository.get_book(book.ISBN) is not None:
            raise ValueError("Book with this ISBN already exists")
        return self._repository.add_book(book)

    def update_book(self, book: Book) -> None:
        """Raise ValueError if the book does not exist."""
        if self._repository.get_book(book.ISBN) is None:
            raise ValueError("Book with this ISBN does not exist")
        self._repository.delete_book(book.ISBN)
        self._repository.add_book(book)
        return None

    def delete_book(self, ISBN: str) -> None:
        return self._repository.delete_book(ISBN)
