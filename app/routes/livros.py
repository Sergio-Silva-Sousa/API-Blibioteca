from flask import Blueprint, jsonify
livro = Blueprint("livros",__name__)

@livro.route("/")
def tudo():
  dados = {"Status": "ok"}
  return  jsonify(dados)