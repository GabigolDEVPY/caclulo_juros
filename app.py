from flask import Flask, blueprints, Blueprint, render_template, make_response, jsonify, request


def calcular_juros(inicial, meses, aportes, juros):

    total = inicial
    total_investido = inicial + (aportes * meses)
    juros = juros / 12

    for mes in range(meses):
        total = total + aportes + (total) / 100 * juros
    valor_juros = total - total_investido

    return {
        "total": round(total, 2),
        "total_investido": round(total_investido, 2),
        "valor_juros": round(valor_juros, 2)
    }    



app = Flask(__name__)

@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.form.to_dict()
    result = calcular_juros(float(dados['inicial']), int(dados['meses']), float(dados['aportes']), float(dados['juros']))
    return render_template("users.html", result=result)

@app.route("/users", methods=["GET"])
def return_users():
    return render_template("users.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3000)