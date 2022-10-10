from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'friendship_schema'

class Friendship:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # foreign keys
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<Friendship ID: {self.id} , User/Friend Pairs: {self.user_id} {self.friend_id}>'
    
    ##BASIC CRUD
    #create
    @classmethod
    def save_friendship(cls, data):
        query = "INSERT INTO friendships ( user_id , friend_id ,  created_at, updated_at ) VALUES ( %(user_id)s , %(friend_id)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    @staticmethod
    def already_friends(data):
        query = "SELECT * FROM friendships WHERE user_id=%(user_id)s AND friend_id=%(friend_id)s;"
        results = connectToMySQL(DATABASE).query_db( query, data )
        return len(results) > 0

    #read - show all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM friendships INNER JOIN users user_id ON friendships.user_id = user_id.id INNER JOIN users friend_id ON friendships.friend_id = friend_id.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        friendships = []
        for result in results:
            dict = {
                'id': result['id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'ffirst_name': result['friend_id.first_name'],
                'flast_name': result['friend_id.last_name'],
            }
            friendships.append( dict )
        return friendships

    #read - show one
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM friendships WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])


    #update
    @classmethod
    def update_friendship(cls, data):
        query = "UPDATE friendships SET user_id = %(user_id)s, friend_id = %(friend_id)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        query = "DELETE FROM friendships WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
