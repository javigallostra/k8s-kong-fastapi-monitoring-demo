from typing import Protocol

from app.models.books import Book


class BookRepository(Protocol):

    def list_books(self) -> list[Book]: ...

    def get_book(self, ISBN: str) -> Book | None: ...

    def add_book(self, book: Book) -> None: ...

    def delete_book(self, ISBN: str) -> None: ...
