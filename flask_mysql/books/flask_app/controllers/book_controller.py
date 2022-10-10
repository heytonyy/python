from flask_app import app,render_template, redirect, request
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author

@app.get('/books')
def books():
    books = Book.read_all()
    return render_template('books.html',books=books)

@app.get('/books/<int:id>')
def show_book(id):
    data = { 'id': id }
    book = Book.read_one(data)
    fav_books = Book.join_books(data)
    author_favs = fav_books.list_of_authors
    all_authors = Author.read_all()
    return render_template('book_show.html', book=book, author_favs=author_favs, all_authors=all_authors)

@app.post('/add_book_fav/<int:id>')
def add_book_fav(id):
    data = {
        'book_id': int(id),
        'user_id': request.form['user_id']
    }
    if Book.is_favorited(data):
        return redirect(f'/books/{id}')
    Book.add_favorite(data)
    return redirect (f'/books/{id}')