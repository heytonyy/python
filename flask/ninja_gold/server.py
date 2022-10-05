from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'AND MY AXE'

@app.route('/')
def index():
    # session.clear()
    if 'gold' not in session:
        session['gold'] = 0
        session['log'] = []
        session['turns'] = 0
        session['play_status'] = 'playing'
    return render_template('index.html')

@app.post('/process_money')
def get_gold():
    # VARS FOR LOG STRING
    msg = ''
    status = ''
    now = datetime.now()
    # UPDATE GOLD
    if request.form['building'] == 'farm':
        gold = random.randint(10,20)
        msg = 'Earned '+str(gold)+' gold from the farm! ['+str(now)+']'
        status = 'success'
    elif request.form['building'] == 'cave':
        gold = random.randint(5,10)
        msg = 'Earned '+str(gold)+' gold from the cave! ['+str(now)+']'
        status = 'success'
    elif request.form['building'] == 'house':
        gold = random.randint(2,5)
        msg = 'Earned '+str(gold)+' gold from the house! ['+str(now)+']'
        status = 'success'
    else:
        operation = random.randint(0,1)
        if operation == 0:
            gold = -random.randint(0,50)
            msg = 'Entered a casino and lost '+str(gold)+' gold... Yikes! ['+str(now)+']'
            status = 'danger'
        else:
            gold = random.randint(0,50)
            msg = 'Entered a casino and won '+str(gold)+' gold! Ayoo! ['+str(now)+']'
            status = 'success'
    # UPDATE LOG
    temp_log = session['log']
    temp_log.append({
        'message': msg,
        'status': status
    })
    session['log']=temp_log
    session['gold'] += gold
    session['turns'] += 1
    # LOSE CONDITION
    if session['gold'] < 0:
        session['gold'] = 0
        session['play_status'] = 'lose'
        session['log'] = [{
            'message': 'Oh no! You ran out of gold. You lose. :(',
            'status': 'danger'
        }]
    if session['turns'] > 14:
        session['turns'] = 15
        session['play_status'] = 'lose'
        session['log'] = [{
            'message': 'Oh no! You ran out of turns. You lose. :(',
            'status': 'danger'
        }]
    # WIN CONDITION
    if session['gold'] > 500:
        session['gold'] = 500
        session['play_status'] = 'win'
        session['log'] = [{
            'message': 'CONGRATZ! You collected 500 gold! You win!',
            'status': 'success'
        }]
    return redirect('/')

@app.post('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)