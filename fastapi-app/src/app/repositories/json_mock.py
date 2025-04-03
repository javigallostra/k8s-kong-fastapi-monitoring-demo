import json
import os

from pydantic import TypeAdapter

from app.models.books import Book

_DEFAULT_JSON_SOURCE_FILE = os.path.join(
    os.path.dirname(__file__), "..", "static", "mock_data.json"
)


def _load_data_from_file(source_file: str) -> list[Book]:
    with open(source_file, "r") as fo:
        data = json.load(fo)
    return TypeAdapter(list[Book]).validate_python(data)


class JSONMockBookRepository:

    def __init__(self, source_file: str | None = None) -> None:
        if source_file is None or source_file.strip() == "":
            source_file = _DEFAULT_JSON_SOURCE_FILE
        self._data = _load_data_from_file(source_file)

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
