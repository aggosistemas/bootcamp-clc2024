from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<br>New message 12622024</br>"