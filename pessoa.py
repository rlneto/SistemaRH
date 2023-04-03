class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        retur