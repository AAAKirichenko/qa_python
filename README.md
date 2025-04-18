# qa_python

Написано 14 автотестов:

1) test_add_new_book_add_two_books_succes - успешное добавление двух книг;
2) test_add_new_book_empty_book_name_not_succes - попытка добавления книги с пустым названием;
3) test_add_new_book_add_identical_books_not_succes - попытка добавления одной и той же книгуи дважды;
4) test_set_book_genre_three_books_success - установление жанра книги, если книга есть в books_genre и её жанр входит в список genre;
5) test_set_book_genre_not_genre_in_list_not_success - попытка установления жанра книги, если жанр книги не входит в список genre;
6) test_get_book_genre_existing_book_receive_genre - получение жанра книги по ее имени;
7) test_get_books_with_specific_genre_receive_list_books - вывод списка книг с определенным жанром;
8) test_get_books_with_specific_genre_not_genre_receive_empty_list - вывод списка книг с отсутствующим жанром;
9) test_get_books_genre_succes - вывод текущего словаря;
10) test_get_books_for_children_receive_list_books - возвращение книг, которые подходят детям;
11) test_add_book_in_favorites_one_book_success - добавление книги в избранное;
12) test_add_book_in_favorites_identical_book_not_success - попытка повторного добавления книги в избранное;
13) test_delete_book_from_favorites_one_book_success - удаление книги из избранного;
14) test_get_list_of_favorites_books_two_books_receive_list - получение списка избранных книг.