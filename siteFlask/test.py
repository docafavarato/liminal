from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    response = requests.get(f'https://cep.awesomeapi.com.br/:format/:{processed_text}')
    data = response.json()
    return render_template('index.html', cep=data['cep'], address=data['address'], state=data['state'], district=data['district'])


app.run()