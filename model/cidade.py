class Cidade():

    def __init__(self, nome):
        self.nome = nome
        

    def __repr__(self):
        return '<Nome: {}>'.format(self.nome)