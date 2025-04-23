# Тестирование класса BooksCollector

Проект содержит автотесты для проверки работы класса `BooksCollector`, который управляет коллекцией книг.


## Структура проекта

1. **`main.py`**  
   Класс `BooksCollector`

2. **`conftest.py`**  
   Фикстуры с тестовыми данными

3. **`tests.py`**  
   Автотесты

4. **`README.md`**  
   Описание проекта


## Список тестов

### 1. Метод `add_new_book()`
- **Тест**: `test_add_new_book_add_two_books`  
  **Проверяет**: Корректность добавления двух книг в коллекцию

- **Тест**: `test_add_new_book_with_long_name`  
  **Проверяет**: Обработку названий длиннее 40 символов

- **Тест**: `test_add_new_book_add_similar_books`  
  **Проверяет**: Защиту от дублирования книг

### 2. Метод `set_book_genre()`
- **Тест**: `test_set_book_genre_get_genre_successfully`  
  **Проверяет**: Установку и получение жанра для книги

### 3. Метод `get_books_with_specific_genre()`
- **Тест**: `test_get_books_with_specific_genre_one_book_get_list_genre`  
  **Проверяет**: Фильтрацию книг по конкретному жанру

### 4. Метод `get_books_for_children()`
- **Тест**: `test_get_books_for_children_three_books_get_list_book`  
  **Проверяет**: Исключение книг с возрастными ограничениями

- **Тест**: `test_get_books_for_children_adult_books_not_included_the_list`  
  **Проверяет**: Критерии отбора детских книг через параметризацию

### 5. Метод `add_book_in_favorites()`
- **Тест**: `test_add_book_in_favorites_add_one_books_successfully`  
  **Проверяет**: Добавление одной книги в избранное

- **Тест**: `test_add_book_in_favorites_same_books`  
  **Проверяет**: Защиту от дублирования в избранном

### 6. Метод `delete_book_from_favorites()`
- **Тест**: `test_delete_book_from_favorites_removes_book_successfully`  
  **Проверяет**: Корректность удаления книги из избранного

### 7. Метод `get_list_of_favorites_books()`
- **Тест**: `test_add_to_favorites_unlisted_books`  
  **Проверяет**: Невозможность добавления несуществующих книг


## Запуск тестов
```bash
pytest -v tests.py