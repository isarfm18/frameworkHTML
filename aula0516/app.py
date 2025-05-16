from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    nome = "Usuário"
    return render_template('index.html', nome=nome)  # Passando a variável 'nome'


@app.route('/saudacao/<nome_usuario>')
def saudacao(nome_usuario):
    return render_template('index.html', nome=nome_usuario)  # Passando outra variável


@app.route('/produtos')
def produtos():
    lista_produtos = [
        {'nome': 'Notebook', 'preco': 3500.00},
        {'nome': 'Mouse', 'preco': 80.00},
        {'nome': 'Teclado', 'preco': 150.00}, ]
    return render_template('produtos.html', produtos=lista_produtos)
    # obtida da URL


@app.route('/home')
def home():
    return render_template('home.html')  # Renderiza o template filho home.html


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')  # Renderiza o template filho sobre.html


if __name__ == '__main__':
    app.run(debug=True)
