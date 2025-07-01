"""Métodos de classe recebem a classe (cls), e não a instância (self)
Portando ela pode interagir com a classe em si, sem a alterar as instâncias."""

class Pessoa:

    todas_as_pessoas =[]

    def __init__(self, nome, telefone):
        self.nome = nome #      << O significado de "self" é "Referência à instância".
        self.telefone = telefone

    def __str__(self):
        return f'Nome: {self.nome} | Telefone: {self.telefone}'




    #Os métodos de classe,em POO básica, possui 2 aplicações principais:

    #1 Método de Fábrica, para a criação de instâncias a
    #partir da entrada de dados:


    @classmethod
    def construir_pessoa(cls):    # << O significado de "cls" é
                                  # "Referência à classe"

        p_nome = input("digite o nome: ")
        p_telefone = input('digite o telefone: ')

        nova_pessoa = Pessoa(p_nome,p_telefone)
        cls.todas_as_pessoas.append(nova_pessoa)

        return f'{nova_pessoa}'



    # 2 Manipulação de atributos de Classe compartilhados.

    @classmethod
    def listar_pessoas(cls):
        print('todas as pessoas:\n')

        for pessoa in cls.todas_as_pessoas:
            print(pessoa.nome)



print(Pessoa.construir_pessoa())
print()

Pessoa.listar_pessoas()
