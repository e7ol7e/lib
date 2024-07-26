import json
from book import Book

class Storage:
    """
    Класс для управления хранением данных книг в файле JSON.

    Атрибуты:
        filename (str): Имя файла для хранения данных.
    """

    def __init__(self, filename: str = "library.json") -> None:
        """
        Инициализирует новый экземпляр класса Storage.

        Аргументы:
            filename (str, optional): Имя файла для хранения данных. По умолчанию "library.json".
        """
        self.filename = filename

    def load_books(self) -> list[Book]:
        """
        Загружает книги из файла JSON.

        Возвращает:
            list[Book]: Список объектов Book, загруженных из файла.
        """
        books = []
        try:
            with open(self.filename, 'r') as file:
                books_data = json.load(file)
                for book_data in books_data:
                    book = Book(**book_data)
                    books.append(book)
        except FileNotFoundError:
            pass
        return books

    def save_books(self, books: list[Book]) -> None:
        """
        Сохраняет все книги в файл JSON, перезаписывая его.

        Аргументы:
            books (list[Book]): Список объектов Book для сохранения.
        """
        with open(self.filename, 'w') as file:
            json.dump([book.__dict__ for book in books], file, indent=4)
