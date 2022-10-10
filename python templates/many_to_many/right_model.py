'''
MANY TO MANY MODEL
Reference: L <- bridge -> R
This is the Right SIDE (first)
CMD+F --> change model to name of choice
change DATABASE to name of schema in mysql
'''
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import left_model

DATABASE = 'name_of_db'

class RModel:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # model attributes
        self.attribute = data['attribute']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        # list RModels
        self.list_of_lmodels = []

    def __repr__(self):
        return f'<Model ID: {self.id} , Attribute: {self.attribute}>'
    
    # join RModel to bridge
    @classmethod
    def join_RModel( cls , data ):
        query = "SELECT * FROM rmodels LEFT JOIN bridge ON bridge.rmodel_id = rmodel.id LEFT JOIN lmodel ON bridge.lmodel_id = lmodel.id WHERE rmodel.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        rmodel = cls( results[0] )
        for result in results:
            results_data = {
                "id" : result["LModel.id"],
                "attribute": result['attribute'],
                "created_at" : result["RModel.created_at"],
                "updated_at" : result["RModel.updated_at"]
            }
            rmodel.list_of_lmodels.append(left_model.LModel(results_data))
        return rmodel

    # BASIC CRUD
    # create
    @classmethod
    def save_record(cls, data):
        query = "INSERT INTO table1 ( column1 , column2 , created_at, updated_at ) VALUES ( %(value1)s , %(value2)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # read - show all
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


    #update
    @classmethod
    def update_rmodel(cls, data):
        query = "UPDATE table1 SET column1 = %(value1)s, column2 = %(value2)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_rmodel(cls, data):
        query = "DELETE FROM table1 WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
