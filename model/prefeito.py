from model.pessoa import Pessoa
from helpers.database import db


class Prefeito(Pessoa, db.Model):
    
     __tablename__ = "tb_prefeito"
    __mapper_args__ = {'polymorphic_identity': 'prefeito', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    nomePrefeito = db.Column(db.String(80), nullable=False)

    pessoa_parent_ = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_parent = db.Column(db.Integer, db.ForeignKey("tb_prefeitura.id"))

    pessoa = db.relationship("Pessoa",foreign_keys=[pessoa_parent_])

    def __init__(self, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)

    def __repr__(self):
        return '<Nome: {}\n Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
