import pytest
from main import BooksCollector
from conftest import fantasy_book, horror_book, detective_book, child_book, comedy_book, long_name
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тесты добавления книг
    def test_add_one_book_successfully(self, collector):
        collector.add_new_book(fantasy_book)
        assert len(collector.get_books_genre()) == 1

    def test_add_duplicate_books(self, collector):
        collector.add_new_book(fantasy_book)
        collector.add_new_book(fantasy_book)
        assert len(collector.get_books_genre()) == 1

    def test_add_book_with_long_name(self, collector):
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_book_with_empty_name(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_new_book_has_empty_genre(self, collector):
        collector.add_new_book(fantasy_book)
        assert collector.get_book_genre(fantasy_book) == ''

    # Тесты работы с жанрами
    def test_set_valid_genre(self, collector_with_books):
        assert collector_with_books.get_book_genre(fantasy_book) == 'Фантастика'

    def test_set_invalid_genre(self, collector):
        collector.add_new_book(fantasy_book)
        collector.set_book_genre(fantasy_book, 'Роман')
        assert collector.get_book_genre(fantasy_book) == ''

    def test_get_books_by_genre(self, collector_with_books):
        assert collector_with_books.get_books_with_specific_genre('Ужасы') == [horror_book]

    # Тесты детских книг
    def test_get_children_books(self, collector_with_books):
        children_books = collector_with_books.get_books_for_children()
        assert child_book in children_books
        assert horror_book not in children_books

    @pytest.mark.parametrize('book, expected', [
        (fantasy_book, True),
        (horror_book, False),
        (detective_book, False),
        (child_book, True),
        (comedy_book, True)
    ])
    def test_children_books_filter(self, collector_with_books, book, expected):
        assert (book in collector_with_books.get_books_for_children()) == expected

    # Тесты избранного
    def test_add_to_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites(fantasy_book)
        assert fantasy_book in collector_with_books.get_list_of_favorites_books()

    def test_add_duplicate_to_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites(fantasy_book)
        collector_with_books.add_book_in_favorites(fantasy_book)
        assert len(collector_with_books.get_list_of_favorites_books()) == 1

    def test_add_unlisted_to_favorites(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_remove_from_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites(fantasy_book)
        collector_with_books.delete_book_from_favorites(fantasy_book)
        assert fantasy_book not in collector_with_books.get_list_of_favorites_books()