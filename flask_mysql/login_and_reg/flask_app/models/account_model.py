from curses import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = 'login_reg_db'


class Account:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # add as many attributes
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        # time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<Account ID: {self.id} , Name: {self.first_name} {self.last_name}>'
    
    #read - show one
    @classmethod
    def read_one_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "SELECT * FROM accounts WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_record(cls, data):
        # make form names match columns in db - use request.form as data
        query = "INSERT INTO accounts ( first_name , last_name , email, password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s, %(password)s NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #validate user
    @staticmethod
    def is_valid_account(form):
        is_valid = True
        if not EMAIL_REGEX.match(form['email']):
            flash('INVALID CREDENTIALS')
            is_valid = False
        
        return is_valid