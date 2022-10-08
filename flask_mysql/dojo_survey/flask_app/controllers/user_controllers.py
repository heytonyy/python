from flask_app import app, render_template, redirect, session, request
from flask_app.models.user_model import User
from pprint import pprint

# main route
@app.route('/')
def index():
    return render_template('new_survey.html')

@app.post('/process')
def process_info():
    if not User.validate_user(request.form):
        return redirect('/')
    pronouns_list = []
    if 'masc' in request.form:
         pronouns_list.append('He/Him')
    if 'fem' in request.form:
         pronouns_list.append('She/Her')
    if 'they' in request.form:
        pronouns_list.append('They/Them')
    pronouns = ', '.join(pronouns_list)
    if 'services' in request.form:
         services = 'YES'
    else:
         services = 'NO'
    data = {
        'name': request.form['name'],
        'dojo': request.form['dojo'],
        'language': request.form['language'],
        'pronouns': pronouns,
        'services': services,
        'comments': request.form['comments']
    }
    new_user_id = User.save_record(data)
    return redirect(f'/results/{new_user_id}')

@app.get('/results/<int:id>')
def results(id):
    data = {
        'id': id
    }
    user_data = User.read_one_record(data)
    pprint(user_data)
    return render_template('results.html', user = user_data)