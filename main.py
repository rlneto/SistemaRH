from cargo import Cargo
from funcionario import Funcionario

if __name__ == '__main__':
    bancario = Cargo(4000, 'bancário')
    joao = Funcionario(bancario)
    print(joao)
    print('\nAcrescentando dependentes...\n')
    joao.add_dependentes("joaozinho", "0123")
    print(joao)

