from book import Book
from storage import Storage

class Library:
    """
    Класс для управления библиотекой книг.

    Атрибуты:
        storage (Storage): Объект для управления хранением данных.
        books (list[Book]): Список книг в библиотеке.
    """

    def __init__(self) -> None:
        """
        Инициализирует новый экземпляр класса Library.
        """
        self.storage = Storage()
        self.books = self.storage.load_books()

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Добавляет новую книгу в библиотеку и сохраняет её в файл.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год издания книги.
        """
        book = Book(title, author, year)
        self.books.append(book)
        self.storage.save_books(self.books)
        print(f"Книга '{title}' добавлена с ID {book.id}.")

    def remove_book(self, book_id: str) -> None:
        """
        Удаляет книгу из библиотеки и обновляет файл.

        Аргументы:
            book_id (str): Уникальный идентификатор книги для удаления.
        """
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            self.books.remove(book)
            self.storage.save_books(self.books)
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, search_term: str) -> list[Book]:
        """
        Ищет книги по названию, автору или году издания.

        Аргументы:
            search_term (str): Термин для поиска (название, автор или год издания).

        Возвращает:
            list[Book]: Список книг, соответствующих поисковому запросу.
        """
        results = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower() or search_term == book.year]
        return results

    def display_books(self) -> None:
        """
        Выводит все книги в библиотеке.
        """
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("В библиотеке нет книг.")

    def change_book_status(self, book_id: str, new_status: str) -> None:
        """
        Изменяет статус книги и обновляет файл.

        Аргументы:
            book_id (str): Уникальный идентификатор книги для изменения статуса.
            new_status (str): Новый статус книги ("в наличии" или "выдана").
        """
        book = next((book for book in self.books if book.id == book_id), None)
        if book:
            if new_status in ["в наличии", "выдана"]:
                book.status = new_status
                self.storage.save_books(self.books)
                print(f"Статус книги с ID {book_id} изменен на {new_status}.")
            else:
                print("Некорректный статус. Статус должен быть 'в наличии' или 'выдана'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
