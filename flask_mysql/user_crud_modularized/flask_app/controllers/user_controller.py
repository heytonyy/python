###########
# these controll the routes of the application
# uses the User class to query DB
#
###########
from flask_app import app, render_template, redirect, request
from flask_app.models.user_model import User

# controllers
# read - main route - all users
@app.get('/users')
def show_all_users():
    users = User.get_all_users()
    return render_template('all_users.html', users = users)

# read - show one user
@app.get('/users/<int:id>')
def show_user(id):
    data = {
        'id': id
    }
    user = User.get_one_user(data)
    return render_template('show_user.html', user = user)

# create user - get
@app.get('/users/new')
def show_new_user_page():
    return render_template('add_user.html')

# create user - post
@app.post('/users/new')
def add_new_user():
    new_user = User.save_user(request.form)
    return redirect(f'/users/{new_user}')

# update user - get
@app.get('/users/<int:id>/edit')
def show_user_to_edit(id):
    data = {
        'id': id
    }
    user = User.get_one_user(data)
    return render_template('edit_user.html', user = user)

# update user - post
@app.post('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return redirect(f'/users/{id}')

# delete user - get
@app.get('/user/<int:id>/delete')
def delete_user(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/users')