from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

# Instanciamos o caixa globalmente para guardar os dados enquanto o servidor roda
meu_caixa = Caixa("Policarpo", 0)

@app.route('/inicio')
def home():
    return render_template('index.html')

@app.route('/adicionar', methods=['POST'])
def adicionar():
    # Passo 1: Pegar os dados que vieram do formulário HTML
    valor = float(request.form['valor'])
    descricao = request.form['descricao']
    categoria = request.form['categoria']
    tipo = request.form['tipo']
    data = request.form['data']
    
    nova_mov = Movimentacao(valor, descricao, categoria, tipo, data)
    
    # Passo 2: Usar o conhecimento de POO (criando o objeto Movimentacao)
    
    # Passo 3: Adicionar a movimentação dentro do nosso objeto Caixa
    meu_caixa.adc_movimentacao(nova_mov)
    
    
    # Passo 4: Redirecionar o usuário de volta para a tela inicial
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)