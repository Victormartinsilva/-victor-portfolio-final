from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return "Victor Martins Portfolio - Working!"

@app.route('/test')
def test():
    return "Flask is working on Vercel!"
