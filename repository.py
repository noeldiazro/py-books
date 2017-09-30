from books import Book


class Parser:
    @classmethod
    def parse(cls, record):
        [isbn_13, title] = record.rstrip('\n').split(',')
        return Book(isbn_13, title)


class Repository:
    def __init__(self, filename):
        self._filename = filename

    def list_books(self):
        with open(self._filename, 'r') as db:
            return [Parser.parse(record) for record in db]
