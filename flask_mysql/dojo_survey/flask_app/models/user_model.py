###########
#
###########
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from pprint import pprint

DATABASE = 'dojo_survey_db'

class User:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # add as many attributes
        self.name = data['name']
        self.dojo = data['dojo']
        self.language = data['language']
        self.pronouns = data['pronouns']
        self.services = data['services']
        self.comments = data['comments']
        # time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<User ID: {self.id} , Name: {self.name}>'
    
    #read - show all
    @classmethod
    def read_all_records(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for dict in results:
            users.append( User(dict) )
        return users

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
        query = "INSERT INTO users ( name , dojo , language , pronouns , services , comments, created_at, updated_at ) VALUES ( %(name)s , %(dojo)s , %(language)s, %(pronouns)s, %(services)s, %(comments)s, NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    #update
    @classmethod
    def update_record(cls, data):
        # make form names match columns in db - use request.form as data
        query = "UPDATE users SET name = %(name)s, dojo = %(dojo)s, language = %(language)s, pronouns = %(pronouns)s, services = %(services)s, WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "DELETE FROM users WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #validation
    @staticmethod
    def validate_user(form):
        pprint(form)
        if len(form['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if form['dojo'] == 'Not Selected':
            flash("Please select a dojo")
            is_valid = False
        if form['language'] == 'Not Selected':
            flash("Please select a language")
            is_valid = False

        if ('masc' or 'fem' or 'they') not in form:
            flash("Please select the pronouns you use")
            is_valid = False

        if len(form['comments']) == 0:
            flash("Please write a comment")
            is_valid = False
        return is_valid