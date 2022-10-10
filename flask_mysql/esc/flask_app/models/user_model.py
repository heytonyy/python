from flask_app import flash, session
from flask_app.models.message_model import Message
from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
DATABASE = 'esc_db'


class User:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # add as many attributes
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.msg_sent = data['msg_sent']
        # time stamps
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #list of messages
        self.msgs = []

    def __repr__(self):
        return f'<User ID: {self.id} , Name: {self.first_name} {self.last_name}>'
    
    #reads all user messages
    @classmethod
    def get_all_msgs(cls, data):
        query = "SELECT * FROM messages INNER JOIN users from_user ON messages.from_user_id = from_user.id INNER JOIN users to_user ON messages.to_user_id = to_user.id WHERE to_user.id = %(id)s;"
        #query = "SELECT messages.id, from_user.first_name AS from_user_name, to_user.first_name AS to_user_name, messages.content, messages.created_at FROM messages INNER JOIN users from_user ON messages.from_user_id = from_user.id INNER JOIN users to_user ON messages.to_user_id = to_user.id WHERE to_user.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        data = {
            'id': results[0]['to_user.id'],
            'first_name': results[0]['to_user.first_name'],
            'last_name': results[0]['to_user.last_name'],
            'email': results[0]['to_user.email'],
            'password': results[0]['to_user.password'],
            'msg_sent': results[0]['to_user.msg_sent'],
            'created_at': results[0]['to_user.created_at'],
            'updated_at': results[0]['to_user.updated_at']
        }
        user = User(data)
        for msg in results:
            msg_data ={
                'id': msg['id'],
                'from_user_id': msg['first_name'],
                'to_user_id': msg['to_user.first_name'],
                'content': msg['content'],
                'created_at': msg['created_at']
            }
            user.msgs.append(Message(msg_data))
        return user

    #increase sent message #
    @classmethod
    def send_message(cls, data):
        query = "UPDATE users SET msg_sent = msg_sent + 1 WHERE id=%(id)s;"
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # get all
    @classmethod
    def get_all_friends(cls, data):
        query = "SELECT id, first_name, last_name FROM users WHERE id!=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    #read - by ID in DB
    @classmethod
    def read_by_id(cls, data):
        # is there a way to only return first_name, last_name, email?
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return User(results[0])

    # read - by email in DB
    @classmethod
    def read_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return User(result[0])
    
    @classmethod
    def is_email_taken(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        return len(result) > 0

    #create user
    @classmethod
    def create_user(cls, data):
        # save form data to DB, hash pw before using this method
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)

    #validate user for registration
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
        if User.is_email_taken(data={'email':form['email']}):
            flash('Email has been already taken.', 'email_taken')
            is_valid = False
        if not PW_REGEX.match(form['password']):
            flash('Password must have a minimum of 8 characters, which includes at least 1 uppercase, 1 number, and 1 special character.', 'password')
            is_valid = False
        if form['password'] != form['password_confirm']:
            flash('Password and Confirm Password must match.', 'password_match')
            is_valid = False
        return is_valid