from app.repositories.common import BookRepository
from app.repositories.json_mock import JSONMockBookRepository

_repository = None


def repository() -> BookRepository:
    global _repository
    if _repository is None:
        _repository = JSONMockBookRepository()
    return _repository
