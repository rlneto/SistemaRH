from pessoa import Pessoa

class Dependente(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)

    def __str__(self):
        return '\nNome: {}\nCPF:{}'.format(self.nome, self.cpf)

    def identificador(self):
        return self.cpf
