from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model

DATABASE = 'books_schema'

class Author:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # attributes
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        # time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        # list of books
        self.list_of_books = []

    def __repr__(self):
        return f'<Author ID: {self.id} , {self.first_name} {self.last_name}>'
        
    # join authors to favorites
    @classmethod
    def join_authors( cls , data ):
        query = "SELECT * FROM users LEFT JOIN favorites ON favorites.user_id = users.id LEFT JOIN books ON favorites.book_id = books.id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        author = cls( results[0] )
        for result in results:
            results_data = {
                "id" : result["books.id"],
                "title": result['title'],
                "num_of_pages": result['num_of_pages'],
                "created_at" : result["books.created_at"],
                "updated_at" : result["books.updated_at"]
            }
            author.list_of_books.append(book_model.Book(results_data))
        return author

    # add favorite
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites ( book_id, user_id ) VALUES ( %(book_id)s, %(user_id)s );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
    
    # remove favorite
    @classmethod
    def remove_favorite_book(cls, data):
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
    def save_author(cls, data):
        query = "INSERT INTO users ( first_name , last_name , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # read - show all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for result in results:
            authors.append( Author(result) )
        return authors

    #read - show one
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #update
    @classmethod
    def update_author(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_author(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
