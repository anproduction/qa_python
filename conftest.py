import pytest
from main import BooksCollector
from test_data import books_genres

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_with_books(collector):
    for book, genre in books_genres.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
    return collector