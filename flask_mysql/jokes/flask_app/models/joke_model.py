from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import account_model
from pprint import pprint

DATABASE = 'dad_jokes_db'

class Joke:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # foreign key
        self.account_id = data['account_id']
        # attributes
        self.setup = data['setup']
        self.punchline = data['punchline']
        # time stamps
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'<Joke ID: {self.id} , Step: {self.setup}>'
    
    # author of joke method
    @classmethod
    def author_of_joke(cls , data):
        query = "SELECT * FROM accounts LEFT JOIN jokes ON accounts.id = jokes.account_id WHERE jokes.id=%(id)s"
        results = connectToMySQL(DATABASE).query_db( query , data )
        return results[0]

    # count num of groans for joke ID
    @classmethod
    def number_of_groans( cls , data ):
        query = "SELECT * FROM groans WHERE joke_id = %(joke_id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        return len(results)

    # joke validate
    @staticmethod
    def validate_joke(form):
        is_valid = True
        if len(form['setup']) < 3:
            flash('Setup must be at least 3 characters', 'setup')
            is_valid = False
        if len(form['punchline']) < 3:
            flash('Punchline must be at least 3 characters', 'punchline')
            is_valid = False
        return is_valid

    # BASIC CRUD
    #create joke
    @classmethod
    def create_joke(cls, data):
        # save form data to DB, hash pw before using this method
        query = "INSERT INTO jokes ( account_id, setup, punchline, created_at, updated_at ) VALUES ( %(account_id)s, %(setup)s, %(punchline)s, NOW(), NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)

    #read - by ID in DB
    @classmethod
    def read_one_by_id(cls, data):
        query = "SELECT * FROM jokes WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return Joke(results[0])

    # read - all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM jokes;"
        results = connectToMySQL(DATABASE).query_db(query)
        jokes = []
        for dict in results:
            jokes.append( Joke(dict) )
        return jokes
    
    #update
    @classmethod
    def update_joke(cls, data):
        query = "UPDATE jokes SET setup = %(setup)s, punchline = %(punchline)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_joke(cls, data):
        query = "DELETE FROM jokes WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
