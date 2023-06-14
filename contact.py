import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    mensagem = request.form['mensagem']

    # Email configuration
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

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
