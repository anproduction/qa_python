import pytest
from main import BooksCollector
from test_data import books_genres

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def genre_collector(collector):
    def _add_books(custom_books=None):
        books_to_add = custom_books or books_genres
        for book, genre in books_to_add.items():
            collector.add_new_book(book)
            if genre:
                collector.set_book_genre(book, genre)
        return collector
    return _add_books