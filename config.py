from app.routes.livros import livro, ListaLivros, IndividualLivro
from app import app
from app.extensions import api

def config_tudo():
  config_rotas()


def config_rotas():
  api.add_resource(ListaLivros,"/")
  api.add_resource(IndividualLivro,"/<livro_id>")
  app.register_blueprint(livro,url_prefix="/livros")
  