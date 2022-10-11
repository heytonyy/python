from flask_app import app, bcrypt, render_template, redirect, request, session, flash
from flask_app.models.recipe_model import Recipe
from flask_app.models.account_model import Account

# dashboard
@app.get('/recipes')
def logged_in():
    data = { 'id': session['user_id'] }
    user = Account.read_by_id(data)
    # all_recipes = Recipe.all_recipes()
    all_recipes = Recipe.all_recipes_with_names()
    return render_template('all_recipes.html', user=user, all_recipes=all_recipes)

#add recipe
@app.get('/recipes/new')
def new_recipe():
    data={'id': session['user_id']}
    user = Account.read_by_id(data)
    action = 'new'
    return render_template('new_recipe.html', user=user, action = action)

# post new recipe to DB
@app.post('/recipes/new/<int:id>')
def create_recipe(id):
    data = {
        'account_id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30'],
    }
    Recipe.save_recipe(data)
    return redirect('/recipes/new')

# view recipe
@app.get('/recipes/view/<int:id>')
def view_recipe(id):
    user_data = { 'id': session['user_id'] }
    user = Account.read_by_id(user_data)
    recipe_id = { 'id': id}
    recipe_info = Recipe.recipe_by_id(recipe_id)
    return render_template('view_recipe.html', recipe_info=recipe_info, user=user)

# edit recipe
@app.get('/recipes/edit/<int:id>/<int:account_id>')
def edit_recipe(id, account_id):
    user_data = { 'id': account_id }
    user = Account.read_by_id(user_data)
    recipe_id = { 'id': id}
    recipe_info = Recipe.recipe_by_id(recipe_id)
    action = 'edit'
    return render_template('new_recipe.html', recipe_info=recipe_info, user=user, action = action)

# update recipe
@app.post('/recipes/edit/<int:id>')
def update_recipe(id):
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_30': request.form['under_30']
    }
    Recipe.update_recipe(data)
    return redirect(f'/recipes/view/{id}')