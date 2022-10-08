###########
# creates the flask instance here called 'app'
# this need to be imported to ever file that has app
#       from flask_app import app
# Q: Why do I need to have render_template, redirect, request, flash here?
#   for the controllers that the app uses??
#
###########
from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)

app.secret_key = "1cb1381ed3795166946eb621940ead03cf261f29e214b0e125d73fdab47a05e3"