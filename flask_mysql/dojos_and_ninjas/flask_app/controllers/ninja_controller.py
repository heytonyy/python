###########
# these control the routes of the application
#
###########
from flask_app import app, render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.get('/ninjas')
def show_new_ninja_page():
    dojos = Dojo.read_all_records()
    return render_template('new_ninja.html', dojos = dojos)

@app.post('/new_ninja')
def save_new_ninja():
    Ninja.save_record(request.form)
    return redirect('/')