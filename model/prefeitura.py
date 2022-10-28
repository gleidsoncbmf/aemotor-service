class Prefeitura():

    def __init__(self, secretarios, email, telefone):
        self.secretarios = secretarios
        self.email = email
        self.telefone = telefone
        

    def __repr__(self):
        return '<Secretários: {}, Email: {}, Telefone: {}>'.format(self.secretarios, self.email, self.telefone)