from flask import Flask, render_template, redirect, flash, session, request
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = 'bfcf78c885191484d2c5d714f523f4cce0306481acb5b4559030b0ea61a1365b'
