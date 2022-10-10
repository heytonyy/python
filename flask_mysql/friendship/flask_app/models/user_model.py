from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.friendship_model import Friendship

DATABASE = 'name_of_db'

class User:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # user attributes
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        # list of users related to primary key
        self.friends = []

    def __repr__(self):
        return f'<User ID: {self.id} , Name: {self.first_name} {self.last_name}>'
    
    # joining with many side of relationship, list of objects associated w primary key
    @classmethod
    def join(cls, data):
        query = "SELECT * FROM primary LEFT JOIN foreign ON primary.id = foreign_key WHERE primary.id=%(id)s"
        results = connectToMySQL(DATABASE).query_db( query, data )
        user = User(results[0])
        for result in results:
            result_data = {
                'id': result['id'],
                'attribute': result['attribute'],
                'foriegn_key': result['dojo_id'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at']
            }
            user.list.append(Many(result_data))
        return user

    # BASIC CRUD
    # read - show all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for dict in results:
            users.append( User(dict) )
        return users

    # read - show one
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    # create
    @classmethod
    def save_record(cls, data):
        query = "INSERT INTO users ( first_name , last_name , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # update
    @classmethod
    def update_record(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # delete
    @classmethod
    def delete_record(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
