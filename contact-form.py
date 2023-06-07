from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    mensagem = request.form['mensagem']
    
    # Do something with the form data (e.g., send an email, save to a database)
    
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
