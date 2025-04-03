from typing import Any

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.dependencies import repository
from app.models.books import Book
from app.services.books import BookService

router = APIRouter(prefix="/books", tags=["books"])
_service = BookService(repository())


@router.post("/", status_code=201)
def add_book(book: Book) -> Book:
    if _service.get_book(book.ISBN) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    _service.add_book(book)
    return book


@router.get("/", status_code=200)
def list_books() -> list[Book]:
    return _service.get_book_list()


@router.get("/{ISBN}", status_code=200)
def get_book(ISBN: str) -> Book:
    book = _service.get_book(ISBN)
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return book


@router.put("/{ISBN}", status_code=200, response_model=Book)
def update_book(ISBN: str, book: Book) -> Any:
    if _service.get_book(ISBN) is None:
        _service.add_book(book)
        return JSONResponse(content=book, status_code=status.HTTP_201_CREATED)
    _service.update_book(book)
    return book


@router.delete("/{ISBN}", status_code=204)
def delete_book(ISBN: str) -> None:
    return _service.delete_book(ISBN)
