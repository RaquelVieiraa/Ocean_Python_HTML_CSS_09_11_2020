  
from flask import (
    Blueprint, render_template, request
)

from flask import Flask
app = Flask(__name__)

bp = Blueprint('app', __name__)

@bp.route('/', methods=('GET', 'POST'))

def index():
    nome_jogador = None
    premio = None
    premio_imagem = None

    if request.method == 'POST':
        nome_jogador = request.form['nome_jogador']
        escolha = request.form['escolha']

        if escolha == 'futurista':
            premio = 'um sabre de luz'
            premio_imagem = ''
        elif escolha == 'medieval':
           premio = 'uma espada'
           premio_imagem = ''

    return render_template('index.html', nome_jogador=nome_jogador, premio=premio, premio_imagem=premio_imagem)


app.register_blueprint(bp)