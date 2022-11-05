from model.pessoa import Pessoa
from helpers.database import d

class Aluno(Pessoa):
    
    __tablename__ = "tb_aluno"
    __mapper_args__ = {'polymorphic_identity': 'aluno', 'concrete': True}
    
    id = db.Column(db.Integer, primary_key=True)
    instituicaoDeEnsino = db.Column(db.String(80), nullable=False)
    curso = db.Column(db.String(50), nullable=False)
    matricula = db.Column(db.String(20), nullable=False)

    pessoa_parent = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    instituicaoDeEnsino_child = db.relationship("InstituicaoDeEnsino", uselist=False)
    rota = db.relationship('Rota', backref='Rota', lazy=True)
    passageiro_child = db.relationship('Passageiro',uselist=False)
    

    def __init__(self, nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome, nascimento, email, telefone)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula

    def __repr__(self):
        return '<Nome: {}, Nascimento: {} , Email: {}, Telefone: {} , Instituição de Ensino: {}, Curso: {}, Matricula: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.instituicaoDeEnsino, self.curso, self.matricula)
