from flask_app import app
from flask_app.controllers import friendship_controller
from flask_app.controllers import user_controller

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)