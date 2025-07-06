from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/cadastro", methods=["POST"])
def salvar():
    nome = request.form["nome"]
    email = request.form["email"]
    with open("dados.txt", "a") as f:
        f.write(f"{nome},{email}\n")
    return f"Olá, {nome}! Cadastro salvo com sucesso."

app.run(debug=True)
