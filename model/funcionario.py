from model.pessoa import Pessoa
from helpers.database import db

class Funcionario(Pessoa, db.Model):
    
    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario', 'concrete': True}
    
    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String(90), nullable=False)
    cargo = db.Column(db.String(30), nullable=False)

    
    pessoa_parent = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_id = db.Column(db.Integer, db.ForeignKey('tb_prefeitura.id'), nullable=False)
    motorista_child = db.relationship("Motorista", uselist=False)

    pessoa = db.relationship("Pessoa",foreign_keys=[pessoa_parent])

    def __init__(self,nome, nascimento, email, telefone, prefeitura, cargo):
        super().__init__(nome, nascimento, email, telefone)
        self.prefeitura = prefeitura
        self.cargo = cargo
        
    def __repr__(self):
        return 'Nome: {}, Data de Nascimento: {}, Email: {}, Telefone: {}, Prefeitura: {}, Cargo: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.prefeitura, self.cargo)
