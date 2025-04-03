from app.models.books import Book


class EmptyBookRepository:

    def __init__(self) -> None:
        self._data: list[Book] = []

    def list_books(self) -> list[Book]:
        return self._data

    def get_book(self, ISBN: str) -> Book | None:
        for book in self._data:
            if book.ISBN == ISBN:
                return book
        return None

    def add_book(self, book: Book) -> None:
        self._data.append(book)
        return None

    def delete_book(self, ISBN: str) -> None:
        for index, book in enumerate(self._data):
            if book.ISBN == ISBN:
                del self._data[index]
                break
        return None
