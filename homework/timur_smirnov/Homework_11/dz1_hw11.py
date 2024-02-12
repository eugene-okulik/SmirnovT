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
        return f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, материал: {self.page_material}{reserved_info}"


book1 = Book(title='Идиот', author='Достоевский', num_pages=500, isbn='978-3-16-148410-0')
book2 = Book(title='Война и мир', author='Толстой', num_pages=1300, isbn='978-4-16-148410-1')
book3 = Book(title='Чистый код', author='Роберт Мартин', num_pages=464, isbn='978-5-16-148410-2')
book4 = Book(title='Гарри Поттер', author='Дж. К. Роулинг', num_pages=600, isbn='978-6-16-148410-3')
book5 = Book(title='Преступление и наказание', author='Достоевский', num_pages=672, isbn='978-7-16-148410-4')

# Помечаем одну книгу как зарезервированную
book3.is_reserved = True

# Распечатать детали о каждой книге
books = [book1, book2, book3, book4, book5]
for book in books:
    print(book)
