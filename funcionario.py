from cargo import Cargo
from dependente import Dependente
from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, cargo: Cargo):
        super().__init__(nome, cpf)
        self.__cargo = cargo
        self.__dependentes = set()

    def add_dependentes(self, nome: str, cpf: str):
        self.__dependentes.add(Dependente(nome, cpf))

    def rem_dependentes(self, cpf):
        for dependente in self.__dependentes:
            if dependente.cpf == cpf:
                print("\nRemovendo {}...\n".format(dependente.nome))
                self.__dependentes.discard(dependente)
                dependente = None
                print(dependente)
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
    def identificador(self):
        return self.cpf


