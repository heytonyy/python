'''
ONE TO MANY
ONE SIDE - LIST ATTRIBUTE ASSOCIATED WITH PRIMARY KEY
CMD+F --> change model to name of choice
change DATABASE to name of schema in mysql
'''
from flask_app.config.mysqlconnection import connectToMySQL
#make sure to import many model
from flask_app.models.many_model import Many

DATABASE = 'name_of_db'

class Model:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # model attributes
        self.attribute = data['attribute']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        # list of models related to primary key
        self.list = []

    def __repr__(self):
        return f'<Model ID: {self.id} , Attribute: {self.attribute}>'
    
    # joining with many side of relationship, list of objects associated w primary key
    @classmethod
    def join(cls, data):
        query = "SELECT * FROM primary LEFT JOIN foreign ON primary.id = foreign_key WHERE primary.id=%(id)s"
        results = connectToMySQL(DATABASE).query_db( query, data )
        model = Model(results[0])
        for result in results:
            result_data = {
                'id': result['id'],
                'attribute': result['attribute'],
                'foriegn_key': result['dojo_id'],
                'created_at': result['created_at'],
                'updated_at': result['updated_at']
            }
            model.list.append(Many(result_data))
        return model

    # BASIC CRUD
    # read - show all
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM table1;"
        results = connectToMySQL(DATABASE).query_db(query)
        models = []
        for dict in results:
            models.append( Model(dict) )
        return models

    # read - show one
    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM table1 WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    # create
    @classmethod
    def save_record(cls, data):
        query = "INSERT INTO table1 ( column1 , column2 , created_at, updated_at ) VALUES ( %(value1)s , %(value2)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # update
    @classmethod
    def update_record(cls, data):
        query = "UPDATE table1 SET column1 = %(value1)s, column2 = %(value2)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # delete
    @classmethod
    def delete_record(cls, data):
        query = "DELETE FROM table1 WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
