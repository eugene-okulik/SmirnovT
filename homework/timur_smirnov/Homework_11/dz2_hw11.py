class Book:

    page_material = 'бумага'
    has_text = True

    def __init__(self, title, author, num_pages, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def __str__(self):
        reserved_info = ', зарезервирована' if self.is_reserved else ''
        return (f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.num_pages}, материал: {self.page_material}{reserved_info}")


class Textbook(Book):
    def __init__(self, title, author, num_pages, isbn, subject, grade, has_tasks, is_reserved=False):
        super().__init__(title, author, num_pages, isbn, is_reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = has_tasks

    def __str__(self):
        reserved_info = ', зарезервирована' if self.is_reserved else ''
        has_tasks_info = ', с заданиями' if self.has_tasks else ', без заданий'
        return f"{super().__str__()}, предмет: {self.subject}, класс: {self.grade}{has_tasks_info}{reserved_info}"


# Создаем экземпляры учебников
textbook1 = Textbook('Алгебра', 'Иванов', 200, '123-456-789', 'Математика', 9, True)
textbook2 = Textbook('История', 'Петров', 250, '987-654-321', 'История', 10, False)
textbook3 = Textbook('Биология', 'Сидоров', 300, '567-890-123', 'Биология', 8, True)

# Помечаем один учебник как зарезервированный
textbook3.is_reserved = True

# Распечатываем детали о каждом учебнике
textbooks = [textbook1, textbook2, textbook3]
for textbook in textbooks:
    print(textbook)
