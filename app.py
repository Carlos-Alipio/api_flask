# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"mensagem": "API rodando na Hostinger!"})

if __name__ == '__main__':
    app.run()