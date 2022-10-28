from model.aluno import Aluno

class Passageiro(Aluno):

    def __init__(self, nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula, cidadeOrigem, cidadeDestino):
        super().__init__(nome, nascimento, email, telefone, instituicaoDeEnsino, curso, matricula)
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return '<Nome: {}, Data de Nascimento: {}, Email: {}, Telefone: {}, Cidade de Origem: {}, Cidade de Destino: {}>'.format(self.nome, self.nascimento, self.email, self.telefone, self.cidadeOrigem, self.cidadeDestino)
        