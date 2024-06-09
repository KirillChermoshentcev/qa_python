import pytest

from main import BooksCollector

@pytest.fixture
def books_library():
    books_library = BooksCollector()

    books_library.add_new_book('Гарри Поттер и философский камень')
    books_library.add_new_book('Кладбище домашних животных')
    books_library.add_new_book('Девушка с татуировкой дракона')
    books_library.add_new_book('Простоквашино')
    books_library.add_new_book('Приключения капитана Врунгеля')
    books_library.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
    books_library.set_book_genre('Кладбище домашних животных', 'Ужасы')
    books_library.set_book_genre('Девушка с татуировкой дракона', 'Детективы')
    books_library.set_book_genre('Простоквашино', 'Мультфильмы')
    books_library.set_book_genre('Приключения капитана Врунгеля', 'Комедии')

    return books_library
