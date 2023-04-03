from cargo import Cargo
from funcionario import Funcionario

if __name__ == '__main__':
    bancario = Cargo(4000, 'bancário')
    joao = Funcionario(bancario)
    print(joao)
    print('\nAcrescentando dependentes...\n')
    joao.add_dependentes("joaozinho", "0123")
    print(joao)
    for dependente in joao.dependentes:
        print(dependente)
    print('\nRemovendo dependentes...\n')
    joao.rem_dependentes("0123")
    for dependente in joao.dependentes:
        print(dependente)


    # cargo2 = Cargo(int(input("Informe o salário:")), str(input("Informe a descrição")))
    #
    # print(cargo2.salario, cargo2.descricao)

