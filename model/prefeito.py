from model.pessoa import Pessoa

class Prefeito(Pessoa):

    def __init__(self, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)

    def __repr__(self):
        return '<Nome: {}\n Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)