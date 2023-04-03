from cargo import Cargo
from dependente import Dependente

class Funcionario:
    def __init__(self, cargo: Cargo):
        self.__cargo = cargo
        self.__dependentes = set()

    def add_dependentes(self, nome: str, cpf: str):
        self.__dependentes.add(Dependente(nome, cpf))

    def rem_dependentes(self, cpf):
        for dependente in self.__dependentes:
            if dependente.__cpf == cpf:
                self.__dependentes.discard(dependente)
                break


