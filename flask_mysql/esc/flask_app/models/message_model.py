from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'esc_db'

class Message:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # add as many attributes
        self.from_user_id = data['from_user_id']
        self.to_user_id = data['to_user_id']
        self.content = data['content']
        # time stamps
        self.created_at = data['created_at']

    def __repr__(self):
        return f'<Message ID: {self.id} , From User: {self.from_user_id} To User: {self.to_user_id}>'
    
    #create message
    @classmethod
    def create_message(cls, data):
        # save form data to DB, hash pw before using this method
        query = "INSERT INTO messages ( from_user_id, to_user_id, content, created_at ) VALUES ( %(from_user_id)s, %(to_user_id)s, %(content)s, NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #delete message
    @classmethod
    def delete_message(cls, data):
        query = "DELETE FROM messages WHERE id=%(id)s;"
        connectToMySQL(DATABASE).query_db(query, data)
        return True
