###########
# Data model for Ninja, with CRUD
# Many Ninjas in a dojo
###########
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojo_ninja_db'

class Ninja:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # ninja attributes
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        # add a foreign key if needed
        self.dojo_id = data['dojo_id']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<ninja ID: {self.id} , Attribute: {self.attribute}>'
    
    #read - show all
    @classmethod
    def read_all_records(cls):
        query = "SELECT * FROM table1;"
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for dict in results:
            ninjas.append( Ninja(dict) )
        return ninjas

    #read - show one
    @classmethod
    def read_one_record(cls, data):
        # make data a dict with key 'id'
        query = "SELECT * FROM table1 WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    #create
    @classmethod
    def save_record(cls, data):
        # make data a dict with keys from form name
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , %(dojo_id)s , NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #update
    @classmethod
    def update_record(cls, data):
        # make data a dict with keys from the form name
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    #delete
    @classmethod
    def delete_record(cls, data):
        # make data a dict with key 'id'
        query = "DELETE FROM ninjas WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
