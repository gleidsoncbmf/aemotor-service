class Veiculo ():

    def __init__(self, cidade, qtdPassageiros, tipoVeiculo, placa):
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa

    def __repr__(self):
        return '<Cidade: {}, Quantidade de Passageiros: {}, Veículo: {}, Placa: {}>'.format(self.cidade, self.qtdPassageiros, self.tipoVeiculo, self.placa)