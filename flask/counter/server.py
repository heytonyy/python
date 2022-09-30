from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'FLY YOU FOOLS'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
        session['times_visited'] = 0
        session['rate'] = 1
    session['count'] += session['rate']
    session['times_visited'] += 1
    return render_template('index.html')

@app.get('/destroy_session')
def clear():
    session.clear()
    return render_template('index.html')

@app.get('/double_count')
def double_click():
    session['count'] += session['rate']*2
    session['times_visited'] += 1
    return render_template('index.html')

@app.post('/custom')
def custom():
    session['rate'] = int(request.form['custom'])
    session['times_visited'] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)