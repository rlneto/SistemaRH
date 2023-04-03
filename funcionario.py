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
            if dependente.cpf == cpf:
                self.__dependentes.discard(dependente)
                break

    @property
    def cargo(self):
        return self.__cargo.descricao

    @property
    def dependentes(self):
        return self.__dependentes
    def __str__(self):
        return 'Salário: {}\nDescrição: {}\nDependentes:{}'.format(self.__cargo.salario, self.__cargo.descricao,
                                                                   self.__dependentes)


