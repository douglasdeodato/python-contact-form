from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    mensagem = request.form['mensagem']

    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{telefone},{mensagem}\n")

    return "Dados enviados com sucesso!"

if __name__ == '__main__':
    app.run()