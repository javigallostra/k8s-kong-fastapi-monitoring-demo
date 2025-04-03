from app.main import app
from app.repositories.empty import EmptyBookRepository
from app.routers.books import _service
from fastapi.testclient import TestClient

_client = TestClient(app)

_test_book_json = {
    "title": "The Five Love Languages",
    "author": "Gary Chapman",
    "ISBN": "978-8-17-992826-4",
    "published": "2008-01-01T00:00:00",
}


def test_post_repost_delete_repost() -> None:
    _service._repository = EmptyBookRepository()
    post_response = _client.post("/books/", json=_test_book_json)
    assert post_response.status_code == 201
    second_post_response = _client.post("/books/", json=_test_book_json)
    assert second_post_response.status_code == 409


def test_get_post_get_delete_get() -> None:
    _service._repository = EmptyBookRepository()
    get_response = _client.get(f"/books/{_test_book_json["ISBN"]}")
    assert get_response.status_code == 404
    post_response = _client.post("/books/", json=_test_book_json)
    assert post_response.status_code == 201
    second_get_response = _client.get(f"/books/{_test_book_json["ISBN"]}")
    assert second_get_response.status_code == 200
    assert second_get_response.json() == _test_book_json
    delete_response = _client.delete(f"/books/{_test_book_json["ISBN"]}")
    assert delete_response.status_code == 204
    third_get_response = _client.get(f"/books/{_test_book_json["ISBN"]}")
    assert third_get_response.status_code == 404
