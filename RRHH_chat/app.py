from flask import Flask, render_template, request, jsonify

from chatbot.chat import preguntar

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/preguntar", methods=["POST"])
def consulta():

    pregunta = request.json["pregunta"]

    respuesta = preguntar(pregunta)

    return jsonify({

        "respuesta":respuesta

    })


app.run(debug=True)