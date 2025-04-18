import pytest

class TestBooksCollector:

    # Тестируем добавление двух книг
    def test_add_new_book_add_two_books_succes(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тестируем попытку добавить книгу с пустым названием
    def test_add_new_book_empty_book_name_not_succes(self, collector):
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # Тестируем попытку добавить одну и ту же книгу дважды
    def test_add_new_book_add_identical_books_not_succes(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Гордость и предубеждение и зомби', 'Фантастика'],
            ['Что делать, если ваш кот хочет вас убить', 'Ужасы'],
            ['Шрек', 'Мультфильмы']
        ]
    )
    #  Тестируем установление жанра книги, если книга есть в books_genre и её жанр входит в список genre
    def test_set_book_genre_three_books_success(self, collector, book_name, book_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.books_genre[book_name] == book_genre

    # Тестируем попытку установления жанра книги, если жанр книги не входит в список genre
    def test_set_book_genre_not_genre_in_list_not_success(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Триллер')
        assert  collector.books_genre['Гордость и предубеждение и зомби'] == ''

    # Тестируем получение жанра книги по ее имени
    def test_get_book_genre_existing_book_receive_genre(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.books_genre[book_name] = book_genre
        assert collector.get_book_genre(book_name) == book_genre


    # Тестируем вывод списка книг с определенным жанром
    def test_get_books_with_specific_genre_receive_list_books(self, collector):
        collector.add_new_book('Ледниковый период')
        collector.books_genre['Ледниковый период'] = 'Мультфильмы'
        collector.add_new_book('Шрек')
        collector.books_genre['Шрек'] = 'Мультфильмы'
        result = collector.get_books_with_specific_genre('Мультфильмы')
        expected = ['Ледниковый период','Шрек']
        assert result == expected

    # Тестируем вывод списка книг с отсутствующим жанром
    def test_get_books_with_specific_genre_not_genre_receive_empty_list(self, collector):
        collector.add_new_book('Ледниковый период')
        collector.set_book_genre('Ледниковый период', 'Мультфильмы')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        result = collector.get_books_with_specific_genre('Ужасы')
        expected = []
        assert result == expected

    # Тестируем вывод текущего словаря
    def test_get_books_genre_succes(self,collector):
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        result = collector.get_books_genre()
        expected = {'Звонок' : 'Ужасы', 'Шрек' : 'Мультфильмы'}
        assert result == expected

    #Тестируем возвращение книг, которые подходят детям
    def test_get_books_for_children_receive_list_books(self, collector):
        collector.add_new_book('Звонок')
        collector.books_genre['Звонок']= 'Ужасы'
        collector.add_new_book('Шрек')
        collector.books_genre['Шрек'] = 'Мультфильмы'
        assert collector.get_books_for_children() == ['Шрек']

    # Тестируем добавление книги в избранное
    def test_add_book_in_favorites_one_book_success(self, collector):
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Шрек')
        assert 'Шрек' in collector.favorites

    # Тестируем попытку повторного добавления книги в избранное
    def test_add_book_in_favorites_identical_book_not_success(self, collector):
        collector.add_new_book('Золушка')
        collector.add_book_in_favorites('Золушка')
        collector.add_book_in_favorites('Золушка')
        assert len(collector.favorites) == 1

    # Тестируем удаление книги из избранного
    def test_delete_book_from_favorites_one_book_success(self, collector):
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Шрек')
        collector.delete_book_from_favorites('Шрек')
        assert len(collector.favorites) == 0

    # Тестируем получение списка избранных книг
    def test_get_list_of_favorites_books_two_books_receive_list(self, collector):
        collector.add_new_book('Золушка')
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Золушка')
        collector.add_book_in_favorites('Шрек')
        collector.get_list_of_favorites_books()
        assert collector.favorites == ['Золушка','Шрек']
