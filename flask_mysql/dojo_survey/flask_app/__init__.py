# instantiates the Flask app

from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)

app.secret_key = '2285f79b9701e64cd70a027704e1fd1fb4a3a87137484a0d005274b900aac529'