from flask import Blueprint, jsonify, request, abort
from flask_restful import Resource, reqparse
from app.extensions import db, api, ma
from app.database.models.livros import Livro
from app.database.schemas.livro import LivroSchema

livro = Blueprint("livros",__name__)
api.init_app(livro)
ma.init_app(livro)

parser = reqparse.RequestParser()
parser.add_argument("titulo",type=str,required=True,location="json",help="titulo nao pode ser nulo")
parser.add_argument("descricao",type=str,required=True,location="json",help="descricao nao pode ser nulo")


livroSchema = LivroSchema()
livrosSchema = LivroSchema(many=True)

LIVRO_NAO_ENCONTRADO = 'Livro nao encontrado'

class ListaLivros(Resource):
  def get(self):
    livros = Livro.pegue_todos()
    return livrosSchema.dump(livros)
  
  def post(self):
    argumentos = parser.parse_args()
    for argumento, valor in argumentos.items():
      if str(valor).strip() == "":
        return {"msg": f"{argumento} nao pode ser nulo"}
    livro = Livro(
      titulo = argumentos["titulo"],
      descricao = argumentos["descricao"]
      )
    livro.adicionar_db()
    return {"msg": "Livro adicionado com sucesso"}
    
class IndividualLivro(Resource):
  def get(self, livro_id):
    livro = Livro.ache_pelo_id(livro_id)
    if livro:
      return livroSchema.dump(livro)
    return {"msg":LIVRO_NAO_ENCONTRADO}, 404
  
  def put(self,livro_id):
    args = parser.parse_args()
    livro = Livro.ache_pelo_id(livro_id)
    if livro:
      livro.editar(args)
      return {"msg": "livro editado com sucesso"}, 200
    return {"msg": LIVRO_NAO_ENCONTRADO}, 404
   
  def delete(self, livro_id):
    livro = Livro.ache_pelo_id(livro_id)
    if livro:
      livro.remover_db()
      return {"msg":"livro deletado com sucesso"}, 200
    
    return {"msg": LIVRO_NAO_ENCONTRADO}, 404