from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY', 'portfolio_key')

@app.route('/')
def index():
    return render_template('index.html', 
                         perfil={
                             'nome': 'Victor Martins da Silva',
                             'titulo': 'Analista de Dados',
                             'sobre': 'Engenheiro Agrícola especializado em análise de dados.',
                             'email': 'victoreagri@gmail.com'
                         })

@app.route('/backup')
def backup():
    return render_template('index_backup.html',
                         perfil={
                             'nome': 'Victor Martins da Silva',
                             'titulo': 'Analista de Dados',
                             'sobre': 'Engenheiro Agrícola especializado em análise de dados.',
                             'email': 'victoreagri@gmail.com'
                         })

@app.route('/<path:filename>')
def assets(filename):
    return send_from_directory('..', filename)
