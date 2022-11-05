from model.aluno import Aluno
from helpers.database import db

class Passageiro(Aluno, db.Model):
    
     __tablename__ = "tb_passageiro"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidadeOrigem = db.Column(db.String(90), nullable=False)
    cidadeDestino = db.Column(db.String(90), nullable=False)

    aluno_parent = db.Column(db.Integer, db.ForeignKey('tb_aluno.id'))

    def __init__(self, nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula, cidadeOrigem, cidadeDestino):
        super().__init__(nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula)
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return '<Nome: {}, Data de Nascimento: {}, Email: {}, Telefone: {}, Cidade de Origem: {}, Cidade de Destino: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.cidadeOrigem, self.cidadeDestino)
        
