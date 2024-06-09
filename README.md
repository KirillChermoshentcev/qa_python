# qa_python
1. Проврка добавления 2 книг -- (**def test_add_new_book_add_two_books**)
2. Проверка добавления 1 книги -- (**def test_add_new_book_one_book**)
3. Проверка, что в словарь нельзя добавить одну и ту же книгу -- (**def test_add_new_book_cant_add_the_same_books**)
4. Позитивная проверка, что книга, название которой состоит из 1-40 символов, можно добавить в словарь -- (**def test_add_new_book_with_correct_name_lenght**)
5. Негативная проверка, что книгу, название которой состоит из 0 и 41 символа и больше, нельзя добавить в словарь -- (**def test_add_new_book_with_incorrect_name_lenght**)
6. Проверка, что книге устанавливается жанр, если книга есть в books_genre и её жанр в genre -- (**def test_set_book_genre_book_in_books_genre_and_genre_list**)
7. Проверка, что книге НЕ устанавливается жанр, если её жанр НЕ входит в genre -- (**def test_set_book_genre_book_is_not_in_genre_list**)
8. Проверка, что метод выводит список книг в соответствии с определённым жанром -- (**def test_get_books_with_specific_genre_get_list**)
9. Проверка вывода жанра книги по её названию -- (**def test_get_book_genre_from_list_by_title**)
10. Проверка вывода текущего словаря books_genre -- (**def test_get_books_genre_get_dict_books_genre**)
11. Проверка вывода книг без возрастного рейтинга -- (**def test_get_books_for_children_without_age_rating_in_list**)
12. Проверка добавления книги в избранное -- (**def test_add_book_in_favorites_add_book_show_success**)
13. Проверка, что книга не добавляется в избранное, если её нет в списке books_genre -- (**def test_add_book_in_favorites_if_books_not_in_books_genre_books_not_add**)
14. Проверка удаления книги из избранного -- (**def test_delete_from_favorites_book_removed**)
15. Проверка вывода книг из списка избранных -- (**def test_get_list_of_favorites_books_get_list**)

Файл **conftest.py** содержит фикстуру для проверки метода **def test_get_books_genre_get_dict_books_genre** и **def test_get_books_for_children_without_age_rating_in_list**