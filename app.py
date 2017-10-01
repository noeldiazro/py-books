from books import Book, list_books, add_book
from repository import Repository
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)


@app.route('/')
def home():
    books = list_books(Repository('books.csv'))
    return render_template('books.html', books=books, title='Books')


@app.route('/book', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        add_book(Book(request.form['isbn_13'], request.form['title']),
                 Repository('books.csv'))
        return redirect(url_for('home'))
    else:
        return render_template('book.html', title='Add a new book')


if __name__ == '__main__':
    app.run('0.0.0.0')
