from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'FLY YOU FOOLS'


@app.route('/')
def index():
    if 'winners' not in session:
        session['winners'] = []
    the_number = random.randint(1,100)
    session['answer'] = the_number
    session['attempts'] = 0
    session['guess'] = ''
    session['result'] = ''
    return render_template('index.html')

@app.post('/leaderboard')
def add_to_board():
    # could'nt append to session['winners'], so had to make a var to temp hold
    # the winners list, append to that, them set temp list to session['winners']
    session_winners = session['winners']
    session_winners.append(
        {
            'name' : request.form['new_winner'],
            'attempts' : session['attempts']
        })
    session['winners'] = session_winners
    return redirect('/leaderboard')

@app.get('/leaderboard')
def added_to_board():
    session['show_add_name'] = False
    return render_template('index.html')

@app.post('/guess')
def take_guess():
    session['guess']=int(request.form['guess'])
    print(session)
    if session['guess'] == session['answer']:
        session['result'] = 'correct'
        session['show_add_name'] = True
    elif session['guess'] < session['answer']:
        session['attempts'] += 1
        session['result'] = 'too_low'
    else:
        session['result'] = 'too_high'
        session['attempts'] += 1
    return redirect('/guess')

@app.get('/guess')
def result():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)