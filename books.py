class Book:
    def __init__(self, isbn_13, title):
        self.isbn_13 = isbn_13
        self.title = title


def list_books(repository):
    return repository.list_books()
