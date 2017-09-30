from books import Book


class Parser:
    @classmethod
    def parse_record_to_book(cls, record):
        [isbn_13, title] = record.rstrip('\n').split(',')
        return Book(isbn_13, title)

    @classmethod
    def parse_book_to_record(cls, book):
        return '{0},{1}\n'.format(book.isbn_13, book.title)


class Repository:
    def __init__(self, filename):
        self._filename = filename

    def list_books(self):
        with open(self._filename, 'r') as db:
            return [Parser.parse_record_to_book(record) for record in db]

    def add_book(self, book):
        with open(self._filename, 'a') as db:
            db.write(Parser.parse_book_to_record(book))
