from flask import Flask, render_template, redirect, session, request, flash

app = Flask(__name__)

app.secret_key = "CHANGE THIS LATER"