# Import Flask to allow us to create our app
from flask import Flask

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following
@app.route('/')

# Return the string 'Hello World!' as a response
def hello_world():
    return 'Hello World!'

# Ensure this file is being run directly and not from a different module
if __name__=="__main__":
    # Run the app in debug mode.
    app.run(debug=True)

