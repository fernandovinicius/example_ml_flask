from flask import Flask


app = Flask('my_app')


@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
