from pessoa import Pessoa

class Dependente(Pessoa):
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf)