from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '2285f79b9701e64cd70a027704e1fd1fb4a3a87137484a0d005274b900aac529'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.post('/process')
def get_info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    if 'services' in request.form:
        session['services'] = 'YES'
    else:
        session['services'] = 'NO'
    pronouns = []
    if 'masc' in request.form:
        pronouns.append('He/Him')
    if 'fem' in request.form:
        pronouns.append('She/Her')
    if 'they' in request.form:
        pronouns.append('They/Them')
    session['pronouns'] = pronouns
    session['comments'] = request.form['comments']
    print(session)
    return redirect('/results')

@app.get('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)