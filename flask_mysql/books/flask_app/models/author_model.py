###########
# 
###########
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'authors_schema'

class Author:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # add as many attributes
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<Author ID: {self.id} , {self.first_name} {self.last_name}>'
    
    #read - show all
    @classmethod
    def read_all_records(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        authors = []
        for dict in results:
            authors.append( Author(dict) )
        return authors

    #read - show one
    @classmethod
    def read_one_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_record(cls, data):
        # make form names match columns in db - use request.form as data
        query = "INSERT INTO users ( first_name , last_name , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #update
    @classmethod
    def update_record(cls, data):
        ## make form names match columns in db - use request.form as data
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "DELETE FROM users WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
