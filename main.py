from cargo import Cargo
from funcionario import Funcionario


def tracejado():
    print("-" * 79)
def relatorio_pessoas(pessoas):
    print("Pessoas da empresa:\n")
    for pessoa in pessoas:
        print(pessoa.nome, pessoa.cpf)
    tracejado()

def relatorio_dependentes(funcionario):
    print("\nDependentes de", funcionario.nome)
    for dep in funcionario.dependentes:
        print(dep.nome)
    tracejado()

if __name__ == '__main__':
    bancario = Cargo(4000, 'bancário')
    joao = Funcionario("João", "1234", bancario)
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
    joao.identificador()

    # cargo2 = Cargo(int(input("Informe o salário:")), str(input("Informe a descrição")))
    #
    # print(cargo2.salario, cargo2.descricao)

