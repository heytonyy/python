from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'FLY YOU FOOLS'


@app.route('/')
def index():
    session.clear()
    the_number = random.randint(1,100)
    session['answer'] = the_number
    return render_template('index.html')

@app.post('/guess')
def take_guess():
    session['guess']=int(request.form['guess'])
    print(session)
    if session['guess'] == session['answer']:
        session['result'] = 'correct'
    elif session['guess'] < session['answer']:
        session['result'] = 'too_low'
    else:
        session['result'] = 'too_high'
    return redirect('/guess')

@app.get('/guess')
def result():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)