class Endereco():

    def __init__(self, cep, numero, complemento, referencia, logradouro):
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia
        self.logradouro= logradouro

    def __repr__(self):
        return '<CEP: {}, Número: {}, Complemento: {}, Referência: {}, Logradouro: {}>'.format(self.cep, self.numero, self.complemento, self.referencia, self.logradouro)