'''
ONE TO MANY
MANY SIDE - THIS HAS THE FOREIGN KEY OF THE PRIMARY MODEL
CMD+F --> change model to name of choice
change DATABASE to name of schema in mysql
'''
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'name_of_db'

class Model:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # model attributes
        self.attribute = data['attribute']
        # add a foreign key if needed
        self.foriegn_key = data['foriegn_key']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<Model ID: {self.id} , Attribute: {self.attribute}>'
    
    ##BASIC CRUD
    #read - show all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM table1;"
        results = connectToMySQL(DATABASE).query_db(query)
        models = []
        for dict in results:
            models.append( Model(dict) )
        return models

    #read - show one
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM table1 WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_record(cls, data):
        query = "INSERT INTO table1 ( column1 , column2 , foreign_key, created_at, updated_at ) VALUES ( %(value1)s , %(value2)s , %(foreign_key)s, NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #update
    @classmethod
    def update_record(cls, data):
        query = "UPDATE table1 SET column1 = %(value1)s, column2 = %(value2)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        query = "DELETE FROM table1 WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
