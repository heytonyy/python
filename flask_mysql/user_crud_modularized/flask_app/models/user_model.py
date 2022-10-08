###########
# creates how the data is organized and retrieved from the DB
# need to use MYSQL connection here so import the connection.
# 
###########
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<User: {self.first_name} {self.last_name}>'
    
    #read - show all
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_cr_db').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    #read - show one
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL('user_cr_db').query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        results = connectToMySQL('user_cr_db').query_db( query, data )
        return results

    #update
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id=%(id)s"
        results = connectToMySQL('user_cr_db').query_db( query, data )
        return results

    #delete
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        results = connectToMySQL('user_cr_db').query_db( query, data )
        return results
