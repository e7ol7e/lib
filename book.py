import uuid

class Fuck:
    pass

class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        id (str): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (str): Год издания книги.
        status (str): Статус книги (в наличии или выдана).
    """

    def __init__(self, title: str, author: str, year: str, id: str = None, status: str = "в наличии") -> None:
        """
        Инициализирует новый экземпляр класса Book.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (str): Год издания книги.
            id (str, optional): Уникальный идентификатор книги. Если не указан, генерируется автоматически.
            status (str, optional): Статус книги. По умолчанию - "в наличии".
        """
        self.id = id if id else str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        Возвращает:
            str: Строковое представление книги.
        """
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"
