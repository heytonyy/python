from flask_app import app, render_template, redirect, request, session, flash
from flask_app.models.account_model import Account

#main
@app.get('/')
def index():
    return render_template('index.html')

#process acount info route
@app.post('/make_account')
def make_account():
    if not Account.is_valid_account(request.form):
        return redirect('/')
    
    return redirect('/')

#login route
@app.post('/login')
def sign_in():
    #validate log in
    return redirect('/dashboard')

#dashboard
@app.get('/dashboard')
def logged_in():
    #send to dashboard with user_id in session
    return render_template('dashboard.html')