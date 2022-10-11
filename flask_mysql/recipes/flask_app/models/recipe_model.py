from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'recipe_db'

class Recipe:
    def __init__(self, data):
        #for reference
        self.id = data['id']
        # foreign_key of creater of recipe
        self.account_id = data['account_id']
        # recipe attributes
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        #time stamps
        self.created_at = data['created_at']
        self.created_at = data['updated_at']

    def __repr__(self):
        return f'<Recipe ID: {self.id} , Name: {self.name}>'
    
    @classmethod
    def all_recipes_with_names(cls):
        query = "SELECT * FROM recipes JOIN accounts ON recipes.account_id = accounts.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results[0])
        recipes = []
        for dict in results:
            recipes.append( Recipe(dict) )
        return recipes

    # BASIC CRUD
    # read - show all
    @classmethod
    def all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for dict in results:
            recipes.append( Recipe(dict) )
        return recipes

    # read - show one
    @classmethod
    def recipe_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id=%(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return (results[0])

    # create
    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes ( account_id , name , description, instructions, date_made, under_30, created_at, updated_at ) VALUES ( %(account_id)s , %(name)s , %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, NOW() , NOW() );"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # update
    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True

    # delete
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s"
        connectToMySQL(DATABASE).query_db( query, data )
        return True
