from model.pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self,nome, nascimento, email, telefone, prefeitura, cargo):
        super().__init__(nome, nascimento, email, telefone)
        self.prefeitura = prefeitura
        self.cargo = cargo
        
    def __repr__(self):
        return 'Nome: {}, Data de Nascimento: {}, Email: {}, Telefone: {}, Prefeitura: {}, Cargo: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.prefeitura, self.cargo)