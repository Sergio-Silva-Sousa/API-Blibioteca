from app.routes.livros import livro, ListaLivros
from app import app
from app.extensions import api

def config_tudo():
  config_rotas()


def config_rotas():
  api.add_resource(ListaLivros,"/")
  app.register_blueprint(livro,url_prefix="/livros")
  