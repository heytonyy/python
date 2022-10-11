from flask_app import app, bcrypt, render_template, redirect, request, session, flash
from flask_app.models.account_model import Account

#main
@app.get('/')
def login():
    return render_template('login.html')

#process acount info route
@app.post('/make_account')
def make_account():
    if not Account.validate_reg(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = Account.create_account(data)
    session['user_id'] = user_id
    return redirect('/')

#login route
@app.post('/login')
def sign_in():
    data = { 'email': request.form['email'] }
    user_in_db = Account.read_by_email(data)
    if not user_in_db:
        flash('Invalid Credentials', 'invalid')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Credentials', 'invalid')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/jokes')

#logout route
@app.get('/logout')
def logout():
    session.clear()
    return redirect('/')