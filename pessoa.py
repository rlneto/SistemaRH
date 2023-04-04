from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf

    @abstractmethod
    def identificador(self):
        pass