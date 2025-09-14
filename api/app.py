from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY', 'default_key')

@app.route('/')
def index():
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados.',
        'email': 'victoreagri@gmail.com'
    }
    return render_template('index.html', perfil=perfil)

@app.route('/backup')
def backup():
    perfil = {
        'nome': 'Victor Martins da Silva',
        'titulo': 'Analista de Dados',
        'sobre': 'Engenheiro Agrícola especializado em análise de dados.',
        'email': 'victoreagri@gmail.com'
    }
    return render_template('index_backup.html', perfil=perfil)

# REMOVER estas linhas se existirem:
# if __name__ == "__main__":
#     app.run()
