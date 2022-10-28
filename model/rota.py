class Rota():

    def __init__(self, cidadeDestino, qtdAlunos, veiculo, passageiro, horaSaida, horaChegada):
        self.cidadeDestino = cidadeDestino
        self.qtdAlunos = qtdAlunos
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada

    def __repr__(self):
        return '<Destino: {}, Quantidade de Alunos: {}, Veículo: {}, Passageiro: {}, Hora de Saída: {}, Hora de Chegada: {}>'.format(self.cidadeDestino, self.qtdAlunos, self.veiculo, self.passageiro, self.horaSaida, self.horaChegada)