from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = "cb3cbd158f116b06c613c210f6061da876c8c6aef1bb14aba8027570ed86ab70"