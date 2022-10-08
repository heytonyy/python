###########
# controllers for all routes that use Dojo info
###########
from flask_app import app, render_template, redirect, request
from flask_app.models.dojo_model import Dojo

#redirects to dojo page
@app.get('/')
def index():
    return redirect('/dojos')

# show all dojos page
@app.get('/dojos')
def show_all_dojos():
    dojos = Dojo.read_all_records()
    return render_template('index.html', dojos = dojos)

# add new dojo, redirect to show all dojos
@app.post('/new_dojo')
def add_dojo_to_db():
    Dojo.save_record(request.form)
    return redirect('/dojos')

# delete dojo, redirect to show all dojos
@app.post('/delete_dojo')
def delete_dojo():
    Dojo.delete_record(request.form)
    return redirect('/dojos')

# selects the dojo based on ID, shows all ninjas from that dojo on all ninjas page
@app.get('/dojos/<int:id>')
def show_ninjas_at_dojo(id):
    data = {
        'id': id
    }
    #dojo has the ninjas, so pass dojo to HTML
    dojo = Dojo.ninjas_at_dojo(data)
    return render_template('all_ninjas.html', dojo = dojo)
