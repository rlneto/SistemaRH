from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, codigo: int):
        super().__init__(nome, cpf)
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo