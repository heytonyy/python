from flask_app import app, render_template, redirect
from flask_app.models.user_model import User
from flask_app.models.friendship_model import Friendship

@app.get('/')
def home():
    friendships = Friendship.read_all()
    users = User.read_all()
    return render_template('index.html', friendships=friendships, users=users)

@app.post('/add_friendship/<int:user_id>/<int:friend_id>')
def add_friendship(user_id,friend_id):
    data = {
        'user_id': int(user_id),
        'friend_id': int(friend_id)
    }
    if Friendship.already_friends(data):
        return redirect('/')
    Friendship.save_friendship(data)
    return redirect('/')