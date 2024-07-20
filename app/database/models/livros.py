from app.extensions import db

class Livro(db.Model):
  __tablename__ = "livros"
  
  id = db.Column(db.Integer, primary_key=True,autoincrement=True)
  #capa = db.Column(db.String,nullable=False)
  titulo = db.Column(db.String(220),nullable=False)
  #autor = db.Column(db.String(40),nullable=False)
  descricao = db.Column(db.String(),nullable=False)
  #genero = db.Column(db.String(30),nullable=False)
  #paginas = db.Column(db.Integer,nullable=False)
  #editora = db.Column(db.String(220),nullable=False)
  #idioma = db.Column(db.String(30),nullable=False)
  #isbn_13 = db.Column(db.String(13),nullable=False)
  #idade_minima = db.Column(db.Integer,nullable=False)
  #quantidade = db.Column(db.Integer,nullable=False)
  
  @classmethod
  def ache_pelo_id(cls,id):
    return cls.query.filter_by(id=id).first()
    
  @classmethod
  def pegue_todos(cls):
    return cls.query.all()
    
  def adicionar_db(self):
    db.session.add(self)
    db.session.commit()
    
  def remover_db(self):
    db.session.delete(self)
    db.session.commit()
    
  def editar(self,args):
    for chave, item in args.items():
      setattr(self,chave,item)
    db.session.commit()
  