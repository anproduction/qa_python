import pytest
from main import BooksCollector

# Тестовые данные
fantasy_book = 'Хроники Нарнии'
horror_book = 'Оно'
detective_book = 'Убийство в Восточном экспрессе'
child_book = 'Малыш и Карлсон'
comedy_book = 'Трое в лодке'
long_name = 'Очень очень очень длинное название книги, которое превышает лимит в сорок символов'

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_with_books(collector):
    books = {
        fantasy_book: 'Фантастика',
        horror_book: 'Ужасы',
        detective_book: 'Детективы',
        child_book: 'Мультфильмы',
        comedy_book: 'Комедии'
    }
    for book, genre in books.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
    return collector