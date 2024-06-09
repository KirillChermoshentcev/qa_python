import pytest
from main import BooksCollector

class TestBooksCollector:

    # Проверка, что добавилось именно две книги
    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Проверка добавления одной книги
    def test_add_new_book_one_book(self):

        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert len(collector.get_books_genre()) == 1

    # Проверка, что в словарь нельзя добавить одну и ту же книгу
    def test_add_new_book_cant_add_the_same_books(self):

        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    # Позитивная проверка названия книги из 1,2,39 и 40 символов

    books_correct_name_lenght = ['Я', 'Он', 'Невероятная частная жизнь Максвелла Сима', 'Хитроумный идальго Дон Кихот Ламанчский!']

    @pytest.mark.parametrize('correct_name_lenght', books_correct_name_lenght)
    def test_add_new_book_with_correct_name_lenght(self, correct_name_lenght):

        collector = BooksCollector()
        collector.add_new_book(correct_name_lenght)
        assert correct_name_lenght in collector.get_books_genre()

    # Негативная проверка названия книги из 0 и 41 символа

    books_incorrect_name_lenght = ['', 'Хитроумный идальго Дон Кихот Ламанчский!!']

    @pytest.mark.parametrize('incorrect_lenght', books_incorrect_name_lenght)
    def test_add_new_book_with_incorrect_name_lenght(self,incorrect_lenght):

        collector = BooksCollector()
        collector.add_new_book(incorrect_lenght)
        assert collector.get_book_genre(incorrect_lenght) is None


    # Проверка, что книге устанавливается жанр, если книга есть в books_genre и её жанр в genre
    def test_set_book_genre_book_in_books_genre_and_genre_list(self):

        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    # Проверка, что книге НЕ устанавливается жанр, если её жанр НЕ входит в genre
    def test_set_book_genre_book_is_not_in_genre_list(self):

        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита','Роман')
        assert collector.get_book_genre('Мастер и Маргарита') == ''

    # Проверка, что метод выводит список книг в соответствии с определённым жанром
    def test_get_books_with_specific_genre_get_list(self):

        collector = BooksCollector()
        collector.add_new_book('Сталкер')
        collector.set_book_genre('Сталкер', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Сталкер']

    # Проверка вывода жанра книги по её названию
    def test_get_book_genre_from_list_by_title(self):

        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        assert collector.get_book_genre('Горе от ума') == 'Комедии'

    # Проверка вывода текущего словаря books_genre
    def test_get_books_genre_get_dict_books_genre(self, books_library):
        assert books_library.get_books_genre() == {'Гарри Поттер и философский камень':'Фантастика',
                                                   'Кладбище домашних животных':'Ужасы',
                                                   'Девушка с татуировкой дракона':'Детективы',
                                                   'Простоквашино':'Мультфильмы',
                                                   'Приключения капитана Врунгеля':'Комедии'
                                                   }

    # Проверка вывода книг без возрастного рейтинга
    def test_get_books_for_children_without_age_rating_in_list(self,books_library):
        assert books_library.get_books_for_children() == ['Гарри Поттер и философский камень','Простоквашино','Приключения капитана Врунгеля']

    # Проверка добавления книги в избранное
    def test_add_book_in_favorites_add_book_show_success(self):

        collector = BooksCollector()
        collector.add_new_book('Алиса в стране чудес')
        collector.add_book_in_favorites('Алиса в стране чудес')
        assert 'Алиса в стране чудес' in collector.get_list_of_favorites_books()

    # Проверка, что книга не добавляется в избранное, если её нет в списке books_genre
    def test_add_book_in_favorites_if_books_not_in_books_genre_books_not_add(self):

        collector = BooksCollector()
        collector.add_book_in_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 0

    # Проверка удаления книги из избранного
    def test_delete_from_favorites_book_removed(self):

        collector = BooksCollector()
        collector.add_new_book('Вино из одуванчиков')
        collector.add_book_in_favorites('Вино из одуванчиков')
        collector.delete_book_from_favorites('Вино из одуванчиков')
        assert len(collector.get_list_of_favorites_books()) == 0

    # Проверка вывода книг из списка избранных
    def test_get_list_of_favorites_books_get_list(self):

        collector = BooksCollector()
        collector.add_new_book('V значит Вендетта')
        collector.add_new_book('Хранители')
        collector.add_book_in_favorites('V значит Вендетта')
        collector.add_book_in_favorites('Хранители')
        assert 'V значит Вендетта' in collector.get_list_of_favorites_books() and 'Хранители' in collector.get_list_of_favorites_books()