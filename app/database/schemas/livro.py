from app.extensions import ma
from app.database.models.livros import Livro

class LivroSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Livro
    load_instance = True
    