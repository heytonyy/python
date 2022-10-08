from flask import Flask, render_template, request, redirect
from user_model import User

app = Flask(__name__)

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
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    ## HOW DO I REDIRECT TO THE GIVEN ID NEW_USER_ID???
    new_user_id = User.save_user(data)
    return redirect('/users')

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
    ## HOW DO I REDIRECT TO THE GIVEN ID NEW_USER_ID???
    user = User.update_user(data)
    return redirect('/users')

# delete user - get
@app.get('/user/<int:id>/delete')
def delete_user(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/users')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)