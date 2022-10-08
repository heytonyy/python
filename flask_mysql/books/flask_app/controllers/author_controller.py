############
#
############
from flask_app import app,render_template, redirect, session
from flask_app.models.book_model import Book

@app.get('/')
def index():
    return render_template('authors.html')