###########
# this is the file that is executed
# 
###########
from flask_app import app

#import controllers
from flask_app.controllers import dojo_controller
from flask_app.controllers import ninja_controller

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)