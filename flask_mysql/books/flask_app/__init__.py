############
# instantiate the Flask module
############
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = 'KEEP IT SECRET - KEEP IT SAFE'