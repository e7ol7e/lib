from library import Library

def main() -> None:
    """
    Основная функция для запуска приложения и управления циклом интерфейса.
    """
    library = Library()

    while True:
        print("\nМеню библиотеки:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            library.remove_book(book_id)

        elif choice == "3":
            search_term = input("Введите название, автора или год издания для поиска: ")
            results = library.search_books(search_term)
            for book in results:
                print(book)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_book_status(book_id, new_status)

        elif choice == "6":
            break

        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
