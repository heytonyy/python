from flask_app import app, render_template, redirect, request
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author

@app.get('/')
def to_start():
    return redirect('/authors')

@app.get('/authors')
def authors():
    authors = Author.read_all()
    return render_template('authors.html', authors=authors)

@app.post('/new_author')
def new_author():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    Author.save_author(data)
    return redirect('/authors')

@app.get('/authors/<int:id>')
def show_author(id):
    data = { 'id': id }
    user = Author.read_one(data)
    author = Author.join_authors(data)
    fav_books = author.list_of_books
    all_books = Book.read_all()
    return render_template('author_show.html', user=user, fav_books=fav_books, all_books=all_books)

@app.post('/add_author_fav/<int:id>')
def add_author_fav(id):
    data = {
        'user_id': int(id),
        'book_id': request.form['book_id']
    }
    if Author.is_favorited(data):
        return redirect(f'/authors/{id}')
    Author.add_favorite(data)
    return redirect (f'/authors/{id}')

@app.post('/remove/<int:id>')
def remove_favorite(id):
    data = {
        'user_id': int(id),
        'book_id': request.form['book_id']
    }
    Author.remove_favorite_book(data)
    return redirect(f'/authors/{id}')