import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request

app = Flask(__name__)

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    mensagem = request.form['mensagem']

    # Create the email message
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = EMAIL_ADDRESS
    message['Subject'] = 'Form Submission'

    # Add the form data to the email body
    body = f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}"
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)

    return "Dados enviados com sucesso!"

if __name__ == '__main__':
    app.run()
