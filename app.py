from books import list_books
from repository import Repository
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    books = list_books(Repository('books.csv'))
    return render_template('hello.html', books=books)


if __name__ == '__main__':
    app.run('0.0.0.0')
