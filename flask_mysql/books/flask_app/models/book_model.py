from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

DATABASE = 'books_schema'

class Book:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # attributes
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        # time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        # list of authors
        self.list_of_authors = []

    def __repr__(self):
        return f'<Book ID: {self.id} , Book: {self.title}>'

    # join Book to bridge
    @classmethod
    def join_books( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN users ON favorites.user_id = users.id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        book = cls( results[0] )
        for result in results:
            results_data = {
                "id" : result["users.id"],
                "first_name": result['first_name'],
                "last_name": result['last_name'],
                "created_at" : result["users.created_at"],
                "updated_at" : result["users.updated_at"]
            }
            book.list_of_authors.append(author_model.Author(results_data))
        return book

    # add favorite
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites ( book_id, user_id ) VALUES ( %(book_id)s, %(user_id)s );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # remove favorite
    @classmethod
    def remove_favorite_author(cls, data):
        query = "DELETE FROM favorites WHERE book_id=%(book_id)s AND user_id=%(user_id)s;"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # check if already favorited
    @staticmethod
    def is_favorited(data):
        query = "SELECT * FROM favorites WHERE user_id=%(user_id)s AND book_id=%(book_id)s;"
        results = connectToMySQL(DATABASE).query_db( query, data )
        return len(results) > 0

    # BASIC CRUD
    # create
    @classmethod
    def save_record(cls, data):
        query = "INSERT INTO table1 ( column1 , column2 , created_at, updated_at ) VALUES ( %(value1)s , %(value2)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # read - show all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for dict in results:
            books.append( Book(dict) )
        return books

    #read - show one
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM books WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #update
    @classmethod
    def update_book(cls, data):
        query = "UPDATE books SET title = %(title)s, num_of_pages = %(num_of_pages)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_book(cls, data):
        query = "DELETE FROM books WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
