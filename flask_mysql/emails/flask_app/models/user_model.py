###########
#
###########
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'name_of_db'

class Model:
    def __init__(self, data):
        # for reference
        self.id = data['id']
        # add as many attributes
        self.attribute = data['attribute']
        # add a foreign key if needed
        # time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<Model ID: {self.id} , Attribute: {self.attribute}>'
    
    #read - show all
    @classmethod
    def read_all_records(cls):
        query = "SELECT * FROM table1;"
        results = connectToMySQL(DATABASE).query_db(query)
        models = []
        for dict in results:
            models.append( Model(dict) )
        return models

    #read - show one
    @classmethod
    def read_one_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "SELECT * FROM table1 WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_record(cls, data):
        # make form names match columns in db - use request.form as data
        query = "INSERT INTO table1 ( collumn1 , collumn2 , created_at, updated_at ) VALUES ( %(name1)s , %(name2)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #update
    @classmethod
    def update_record(cls, data):
        # make form names match columns in db - use request.form as data
        query = "UPDATE table1 SET collumn1 = %(name1)s, collumn2 = %(name2)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        # use hidden input form with id - use request.form as data
        query = "DELETE FROM table1 WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
