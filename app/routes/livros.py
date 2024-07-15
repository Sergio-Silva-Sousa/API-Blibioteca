from flask import Blueprint, jsonify, request
livro = Blueprint("livros",__name__)


@livro.route("/add", methods=["POST"])
def aidicionar():
  dados = {"Status": "ok"}
  return  jsonify(dados)