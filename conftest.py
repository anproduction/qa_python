import pytest
from main import BooksCollector
from test_data import books_genres

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def genre_collector():
    def _create_collector(custom_books=None):
        collector = BooksCollector()
        books = custom_books or books_genres

        for book, genre in books.items():
            collector.add_new_book(book)
            if genre:
                collector.set_book_genre(book, genre)
        return collector

    return _create_collector