# point of entry to server, starts the server

from flask_app import app

from flask_app.controllers import user_controllers

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)