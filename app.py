from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, soy Miguel Sosa y este contenedor se construyó con CI/CD y Docker (v1.0.0)."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
