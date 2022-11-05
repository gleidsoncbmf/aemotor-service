from model.pessoa import Pessoa
from helpers.database import db

class GestorApp(Pessoa, db_Model):
    
    __tablename__ = "tb_gestorApp"
    __mapper_args__ = {'polymorphic_identity': 'gestor', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    gestorApp = db.Column(db.String(80), nullable=False)

    pessoa_parent = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_parent = db.Column(db.Integer, db.ForeignKey('tb_prefeitura.id'), nullable=False)

    def __init__(self, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)

    def __repr__(self):
        return '<Nome: {}, Data de Nascimento: {}, Email: {}, Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
