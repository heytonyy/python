###########
# Data model for Dojo, with CRUD
# Need to import Ninja bc a Dojo has many Ninjas (list)
###########
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja
from pprint import pprint

DATABASE = 'dojo_ninja_db'

class Dojo:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # add as many attributes
        self.name = data['name']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']
        # add all ninjas here
        self.ninjas = []

    def __repr__(self):
        return f'<Dojo ID: {self.id} , Dojo Name: {self.name}>'
    
    #read - show all
    @classmethod
    def read_all_records(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dict in results:
            dojos.append( Dojo(dict) )
        return dojos

    #read - show one
    @classmethod
    def read_one_record(cls, data):
        # make data a dict with key 'id'
        query = "SELECT * FROM dojos WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_record(cls, data):
        # make data a dict with keys from form name
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #update
    @classmethod
    def update_record(cls, data):
        # make data a dict with keys from the form name
        query = "UPDATE dojos SET name = %(name)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        # make data a dict with key 'id'
        query = "DELETE FROM dojos WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #joins ninjas to specific dojo
    @classmethod
    def ninjas_at_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id=%(id)s"
        results = connectToMySQL(DATABASE).query_db( query, data )
        pprint(results)
        # ONLY NEED FIRST RESULT TO GET dojo_id
        dojo = Dojo(results[0])
        # CHECKS IF DOJO HAS ANY NINJAS
        if results[0]['dojo_id']:
            for result in results:
                ninja_data = {
                    'id': result['id'],
                    'first_name': result['first_name'],
                    'last_name': result['last_name'],
                    'age': result['age'],
                    'dojo_id': result['dojo_id'],
                    'created_at': result['created_at'],
                    'updated_at': result['updated_at']
                }
                dojo.ninjas.append(Ninja(ninja_data))
        return dojo