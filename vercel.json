from flask import Flask, render_template, send_from_directory, request, flash, redirect, url_for
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY', 'portfolio_victor_2024')

@app.route('/')
def index():
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados.',
        'email': 'victoreagri@gmail.com',
        'github': 'https://github.com/Victormartinsilva',
        'linkedin': 'https://www.linkedin.com/in/victor-martins-da-silva-a111ba190/'
    }
    return render_template('index.html', perfil=perfil)

@app.route('/backup')
def backup():
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados.',
        'email': 'victoreagri@gmail.com',
        'github': 'https://github.com/Victormartinsilva',
        'linkedin': 'https://www.linkedin.com/in/victor-martins-da-silva-a111ba190/'
    }
    return render_template('index_backup.html', perfil=perfil)

if __name__ == "__main__":
    app.run(debug=True)
