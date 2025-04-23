# Тестирование класса BooksCollector

Проект содержит набор автотестов для проверки функциональности класса `BooksCollector`, который управляет коллекцией книг.

## Реализованные тесты

### 1. Тесты добавления книг

- `test_add_new_book_add_two_books` - проверяет добавление двух книг в коллекцию
- `test_add_one_book_successfully` - проверяет добавление одной книги
- `test_add_book_with_invalid_name` - проверяет обработку невалидных названий:
  - Пустая строка
  - Название длиннее 40 символов
- `test_add_duplicate_book` - проверяет, что нельзя добавить книгу дважды

### 2. Тесты работы с жанрами

- `test_set_book_genre_valid` - проверяет установку валидного жанра
- `test_set_book_genre_invalid` - проверяет попытку установки несуществующего жанра
- `test_get_book_genre` - проверяет получение жанра книги
- `test_get_books_with_specific_genre` - проверяет фильтрацию по жанру

### 3. Тесты для детских книг

- `test_get_books_for_children` - проверяет, что возвращаются только книги без возрастных ограничений
- Параметризованный тест `test_children_books_filter` проверяет для каждого жанра:
  ```python
  @pytest.mark.parametrize('book, expected', [
      (fantasy_book, True),
      (horror_book, False),
      # ... другие книги
  ])