###########
# 
###########
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'books_schema'

class Book:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # add as many attributes
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<Book ID: {self.id} , Book: {self.title}>'
    
    #read - show all
    @classmethod
    def read_all_records(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for dict in results:
            books.append( Book(dict) )
        return books

    #read - show one
    @classmethod
    def read_one_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "SELECT * FROM books WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_record(cls, data):
        # make form names match columns in db - use request.form as data
        query = "INSERT INTO books ( title , num_of_pages , created_at, updated_at ) VALUES ( %(title)s , %(num_of_pages)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #update
    @classmethod
    def update_record(cls, data):
        ## make form names match columns in db - use request.form as data
        query = "UPDATE books SET collumn1 = %(title)s, collumn2 = %(num_of_pages)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "DELETE FROM books WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
