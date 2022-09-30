# Import Flask to allow us to create our app
from flask import Flask

# Create a new instance of the Flask class called "app"
app = Flask(__name__)

# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/dojo')
def dojo():
    return '<h1>Dojo!</h1>'

@app.route('/say/<person>')
def say(person):
    return f'<h1>Hello {person}!</h1>'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f'<h1>{word*num}</h1>'


# Ensure this file is being run directly and not from a different module
if __name__=="__main__":
    # Run the app in debug mode.
    app.run(debug=True)

