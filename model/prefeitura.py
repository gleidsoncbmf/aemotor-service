from helpers.database import db

class Prefeitura(db.Model):
    
     __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    secretarios=db.Column(db.String(120), nullable=False)
    telefone=db.Column(db.String(120), nullable=False)
    rota_id = db.Column(db.Integer, db.ForeignKey("tb_Rota.id"))
    
    cidade_parent = db.Column(db.Integer, db.ForeignKey("tb_cidade.id"))
    rota_parent = db.Column(db.Integer, db.ForeignKey("tb_Rota.id"))
    gestores = db.relationship('GestorApp_db', backref='GestorApp_db', lazy=True)
    funcionarios = db.relationship('Funcionario_db', backref='Funcionario_db', lazy=True)

    def __init__(self, secretarios, email, telefone):
        self.secretarios = secretarios
        self.email = email
        self.telefone = telefone
        

    def __repr__(self):
        return '<Secretários: {}, Email: {}, Telefone: {}>'.format(self.secretarios, self.email, self.telefone)
