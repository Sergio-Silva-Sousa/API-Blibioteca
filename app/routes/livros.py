from flask import Blueprint, jsonify, request
from flask_restful import Resource, reqparse, fields, marshal_with
from app.extensions import db, api
from app.database.models.livros import Livro

livro = Blueprint("livros",__name__)
api.init_app(livro)

parser = reqparse.RequestParser()
parser.add_argument("titulo",type=str,required=True,location="json",help="titulo nao pode ser nulo")
parser.add_argument("descricao",type=str,required=True,location="json",help="descricao nao pode ser nulo")

resource_fields = {
  "id": fields.Integer,
  "titulo": fields.String,
  "descricao": fields.String
}

class ListaLivros(Resource):
  @marshal_with(resource_fields) 
  def get(self):
    livros = db.session.execute(db.select(Livro)).scalars()
    return [livro for livro in livros]
  
  def post(self):
    argumentos = parser.parse_args()
    for argumento, valor in argumentos.items():
      if str(valor).strip() == "":
        return {"msg": f"{argumento} nao pode ser nulo"}
    livro = Livro(
      titulo = argumentos["titulo"],
      descricao = argumentos["descricao"]
      )
    db.session.add(livro)
    db.session.commit()
    return argumentos