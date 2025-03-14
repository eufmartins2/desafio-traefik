from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá! Este é um app Flask rodando com Traefik!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
