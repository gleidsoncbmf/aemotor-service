from helpers.database import db

class Cidade():
    
     __tablename__ = 'tb_cidade'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    
    prefeitura_child = db.relationship("Prefeitura", uselist=False)

    def __init__(self, nome):
        self.nome = nome
        

    def __repr__(self):
        return '<Nome: {}>'.format(self.nome)
