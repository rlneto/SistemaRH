

class Cargo:
    def __init__(self, salario: int, descricao: str):
        self.__salario = salario
        self.__descricao = descricao

    @property
    def descricao(self):
        return self.__descricao

    @property
    def salario(self):
        return self.__salario

