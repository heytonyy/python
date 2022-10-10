from flask_app import app, render_template, redirect, request, session
from flask_app.models.message_model import Message
from flask_app.models.user_model import User

#send message
@app.post('/send_message/<int:id>')
def send_message(id):
    to_user_id = id
    data = { 
        'from_user_id': session['user_id'],
        'to_user_id': to_user_id,
        'content': request.form['content']
    }
    Message.create_message(data)
    User.send_message(data={'id':session['user_id']})
    return redirect('/dashboard')

#delete message
@app.post('/delete_msg')
def delete_msg():
    data = { 'id': request.form['id'] }
    Message.delete_message(data)
    return redirect('/dashboard')