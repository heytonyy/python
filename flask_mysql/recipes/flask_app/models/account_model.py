from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.recipe_model import Recipe
import re
from pprint import pprint

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
DATABASE = 'recipe_db'

class Account:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # account info
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        # time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        # list of recipes
        self.recipe_list = []

    def __repr__(self):
        return f'<Account ID: {self.id} , Name: {self.first_name} {self.last_name}>'
    
    # joining with recipes, list of objects associated w account id
    @classmethod
    def join_recipes(cls, data):
        query = "SELECT * FROM accounts LEFT JOIN recipes ON accounts.id = recipes.account_id WHERE accounts.id=%(id)s"
        results = connectToMySQL(DATABASE).query_db( query, data )
        pprint(results[0])
        user = Account(results[0])
        for result in results:
            result_data = {
                'id': result['id'],
                'account_id': result['account_id'],
                'name': result['name'],
                'description': result['description'],
                'instructions': result['instructions'],
                'date_made': result['date_made'],
                'under_30': result['under_30'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at']
            }
            user.recipe_list.append(Recipe(result_data))
        return user

    # BASIC CRUD
    # create account
    @classmethod
    def create_account(cls, data):
        query = "INSERT INTO accounts ( first_name, last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def email_is_taken(cls, data):
        query = "SELECT * FROM accounts WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        return len(result) > 0
    
    #read - by ID
    @classmethod
    def read_by_id(cls, data):
        query = "SELECT * FROM accounts WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return Account(results[0])

    # read - by email
    @classmethod
    def read_by_email(cls, data):
        query = "SELECT * FROM accounts WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return Account(result[0])
    
    #validate account for registration
    @staticmethod
    def validate_reg(form):
        is_valid = True
        if len(form['first_name']) < 2:
            flash('First name must be at least 2 characters.', 'first_name')
            is_valid = False
        if len(form['last_name']) < 2:
            flash('Last name must be at least 2 characters.', 'last_name')
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash('Not a valid email.', 'email')
            is_valid = False
        if Account.email_is_taken(data={'email':form['email']}):
            flash('Email has been already taken.', 'email_taken')
            is_valid = False
        if not PW_REGEX.match(form['password']):
            flash('Password must have a minimum of 8 characters, which includes at least 1 uppercase, 1 number, and 1 special character.', 'password')
            is_valid = False
        if form['password'] != form['password_confirm']:
            flash('Password and Confirm Password must match.', 'password_match')
            is_valid = False
        return is_valid