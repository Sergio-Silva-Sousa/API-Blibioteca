from app.routes.livros import livro
from app import app

def config_tudo():
  config_rotas()


def config_rotas():
  app.register_blueprint(livro,url_prefix="/livros")