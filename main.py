from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
from textblob import TextBlob
import pickle


# Instanciando Aplicação Flask c/ Autenticação Simples
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'doe'
basic_auth = BasicAuth(app=app)


# Carregando Modelo de RLM Ajustado
with open(file='./model/lr_model.pkl', mode='rb') as fp:
    model, scaler, features = pickle.load(file=fp)


# Endpoint p/ Cotacao do Valor da Casa
@app.route('/cotacao', methods=['POST'])
@basic_auth.required
def cotacao():
    # Recebendo dados json
    data = request.get_json()

    # Parse e Predict do dados recebidos
    X = [data[col] for col in features]
    X = scaler.transform([X])
    price = model.predict(X)[0]
    price = round(price, 2)

    return jsonify(preco=price)


# Endpoint p/ Analise de Sentimento
@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    pol = tb_en.sentiment.polarity

    return jsonify(frase=frase, trad=str(tb_en), polaridade=pol)


# Enpoint Teste
@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True,
    )
