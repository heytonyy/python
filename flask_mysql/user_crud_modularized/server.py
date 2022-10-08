###########
# this is the file that is executed
# this runs the apps
###########
from flask_app import app

#import controllers
from flask_app.controllers import user_controller

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)