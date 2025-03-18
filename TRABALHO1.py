import sys
class SistemadDeCadastros:
    def __init__(self):
        self.livros = {"codigo":{"a":'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g'}}

    def info(self):
        for i, a in self.livros.items():
            print(f"{i} - {a}")

    def MenuInterativo(self, cadastro, listagem, busca_nome, busca_categoria, busca_valor, valor_estoque, encerrar):
        print()
        print(10 * "-=")
        print("--MENU PRINCIPAL--")
        print()
        print("DIGITE A AÇÃO DESEJADA (Ex.: 1)")
        print()
        print("> 1. CADASTRAR UM NOVO LIVRO")
        print("> 1. CADASTRAR UM NOVO LIVRO")
        print("> 1. CADASTRAR UM NOVO LIVRO")
        print("> 6. BUSCAR LIVRO POR CATEGORIA")
        print("> 7. BUSCA LIVRO POR PREÇO DE LIVRO")
        print("> 8. BUSCA POR QUANTIDADE EM ESTOQUE")
        print("> 9. VALOR TOTAL EM ESTOQUE")
        print("> 0. ENCERRAR ATIVIDADES")

    def CadastrarNovoLivro(self):
        print()
        print(10 * "-=")
        print("--CADASTRO DE LIVROS--")
        print()

        while True:
            novo_livro = {}

            codigo = input("> DIGITE O CÓDIGO DO LIVRO: ")

            titulo = input("> DIGITE O TÍTULO DO LIVRO: ")
            novo_livro["Título"] = titulo

            editora = input("> DIGITE A EDITORA DO LIVRO: ")
            novo_livro["Editora"] = editora

            categoria = input("> DIGITE A CATEGORIA DO LIVRO: ")
            novo_livro['Categoria'] = categoria

            ano = input('> DIGITE O ANO DO LIVRO: ')
            novo_livro['Ano'] = ano

            valor = input('> DIGITE O VALOR DO LIVRO: ')
            novo_livro['Valor'] = valor

            quantidade_em_estoque = input('DIGITE A QUANTIDADE EM ESTOQUE DO LIVRO: ')
            novo_livro['Quantidade em Estoque'] = quantidade_em_estoque

            self.livros[codigo] = novo_livro

            for i, a in self.livros.items():
                print(f'>>>>CÓDIGO: {i}')
                for b,c in a.items():
                    print(f'{b}: {c}')
                print()


            # while True:
            #     print(f"Código: {self.livros[codigo]}\nTítulo: {self.livros['titulo']}\n"
            #           f"Editora: {self.livros['editora']}\nCategoria: {self.livros['categoria']}\n"
            #           f"Ano: {self.livros['ano']}\nValor: {self.livros[valor]}\n"
            #           f"Quantidade Em Estoque: {self.livros['quantidade_em_estoque']}")


    # def ListarLivros(self):
    #     pass
    #
    # def BuscaPorNome(self):
    #     pass
    #
    # def BuscaPorCategoria(self):
    #     pass
    #
    # def BuscaPorPreco(self):
    #     pass
    #
    # def ValorTotalEmEstoque(self):
    #     pass
    #
    # def EncerrarAtividades(self):
    #     pass

sistema = SistemadDeCadastros()

sistema.CadastrarNovoLivro()
