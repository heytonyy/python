from flask_app import app, bcrypt, render_template, redirect, request, session, flash
from flask_app.models.joke_model import Joke
from flask_app.models.account_model import Account
from pprint import pprint

#dashboard
@app.get('/jokes')
def all_jokes():
    data = { 'id': session['user_id'] }
    user = Account.read_by_id(data)
    all_jokes = Joke.read_all()
    return render_template('all_jokes.html', user=user, all_jokes=all_jokes)

# go to add joke page
@app.get('/jokes/add')
def add_joke():
    return render_template('add_joke.html')

# create joke
@app.post('/jokes/add/<int:id>')
def create_joke(id):
    if not Joke.validate_joke(request.form):
        return redirect('/jokes/add')
    joke_data = {
        'account_id': id,
        'setup': request.form['setup'],
        'punchline': request.form['punchline'],
    }
    Joke.create_joke(joke_data)
    return redirect('/jokes')

#view joke
@app.get('/jokes/view/<int:id>')
def view_joke(id):
    data={'id': id}
    joke_info=Joke.read_one_by_id(data)
    joke_data ={
        'joke_id': id
    }
    joke_author = Joke.author_of_joke(data)
    num_of_groans = Joke.number_of_groans(joke_data)
    return render_template('view_joke.html',joke_info=joke_info, num_of_groans=num_of_groans,joke_author=joke_author)

#edit joke
@app.get('/jokes/edit/<int:id>')
def edit_joke(id):
    data={'id': id}
    joke_info = Joke.read_one_by_id(data)
    return render_template('edit_joke.html', joke_info=joke_info)

#update joke
@app.post('/jokes/edit/<int:id>')
def update_joke(id):
    data={
        'id': id,
        'setup': request.form['setup'],
        'punchline': request.form['punchline']
    }
    Joke.update_joke(data)
    return redirect(f'/jokes/view/{id}')

# delete joke
@app.get('/jokes/delete/<int:id>')
def delete_joke(id):
    data={'id': id}
    Joke.delete_joke(data)
    return redirect('/jokes')

# give groan to jokje
@app.get('/jokes/groans/<int:id>')
def give_groan(id):
    data = {
        'account_id': session['user_id'],
        'joke_id': id
    }
    Account.give_groan(data)
    return redirect('/jokes')