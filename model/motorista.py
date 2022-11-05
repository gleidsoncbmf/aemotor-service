from model.funcionario import Funcionario
from helpers.database import db


class Motorista(Funcionario, db.Model):
    
    __tablename__ = "tb_motorista"
    __mapper_args__ = {'polymorphic_identity': 'motorista', 'concrete': True}

    id = db.Column(db.Integer, primary_key=True)
    rotas = db.Column(db.String(80), nullable=False)
    
    funcionario_parent = db.Column(db.Integer, db.ForeignKey("tb_funcionario.id"))
    veiculo_child = db.relationship('Veiculo',uselist=False)

    def __init__(self, nome, nascimento, email, telefone, prefeitura, cargo, rotas):
        super().__init__(nome, nascimento, email, telefone, prefeitura, cargo)
        self.rotas = rotas

    def __repr__(self):
        return 'Nome: {}, Data de Nascimento: {}, Email: {}, Telefone: {}, Prefeitura: {}, Cargo: {}, Rotas: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.prefeitura, self.cargo, self.rotas)
