import sys


class SistemaDeCadastros:
    def __init__(self):
        self.livros = [
            ["001", "O Grande Gatsby", "F. Scott Fitzgerald", "Romance", 1925, 45.0, 80],
            ["002", "1984", "George Orwell", "Distopia", 1949, 55.5, 100],
            ["003", "Sapiens", "Yuval Noah Harari", "História", 2011, 60.0, 120],
            ["004", "A Guerra dos Tronos", "George R. R. Martin", "Fantasia", 1996, 90.0, 70],
            ["005", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 1943, 40.0, 150],
            ["006", "A Origem das Espécies", "Charles Darwin", "Ciência", 1859, 85.0, 200],
            ["007", "A Arte da Guerra", "Sun Tzu", "Estratégia", -500, 50.0, 90],
            ["008", "O Diário de Anne Frank", "Anne Frank", "Biografia", 1947, 35.0, 110],
            ["009", "O Alquimista", "Paulo Coelho", "Ficção", 1988, 45.0, 140],
            ["010", "O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia", 1954, 80.0, 130],
            ["011", "O Caçador de Pipas", "Khaled Hosseini", "Drama", 2003, 60.0, 100],
            ["012", "O Nome da Rosa", "Umberto Eco", "Mistério", 1980, 70.0, 150],
            ["013", "Crime e Castigo", "Fiódor Dostoiévski", "Filosofia", 1866, 95.0, 90],
            ["014", "O Mundo de Sofia", "Jostein Gaarder", "Filosofia", 1991, 65.0, 110],
            ["015", "A Menina que Roubava Livros", "Markus Zusak", "Drama", 2005, 75.0, 130],
            ["016", "O Senhor dos Anéis: As Duas Torres", "J.R.R. Tolkien", "Fantasia", 1954, 85.0, 150],
            ["017", "O Guia do Mochileiro das Galáxias", "Douglas Adams", "Ficção", 1979, 72.5, 180],
            ["018", "A Revolução dos Bichos", "George Orwell", "Distopia", 1945, 40.0, 200],
            ["019", "O Hobbit", "J.R.R. Tolkien", "Ficção", 1937, 50.0, 90],
            ["020", "O Sol é para Todos", "Harper Lee", "Drama", 1960, 60.0, 100]
        ]  # 0              1              2             3      4     5     6

    def info(self):  # OPÇÃO 2 - MENU INTERATIVO

        for informacoes_livros in range(len(self.livros)):
            print()
            print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                  f"Título/Editora: {self.livros[informacoes_livros][1]}/{self.livros[informacoes_livros][2]}\n"
                  f"Categoria: {self.livros[informacoes_livros][3]}\n"
                  f"Ano: {self.livros[informacoes_livros][4]}\n"
                  f"Valor: R$ {self.livros[informacoes_livros][5]}\n"
                  f"Estoque: {self.livros[informacoes_livros][6]} unidades\n"
                  f"Valor em Estoque: R$ {self.livros[informacoes_livros][6] * self.livros[informacoes_livros][5]}")

        print()
        print(5 * "-=")
        print("RESPONDA COM S / N:")
        pergunta_info = input('DESEJA CADASTRAR MAIS LIVROS? ')

        opcao_escolhida_info = self

        if pergunta_info.lower() == "s":
            opcao_escolhida_info.CadastrarNovoLivro()
        else:
            opcao_escolhida_info.MenuInterativo()

    def MenuInterativo(self):
        print(18 * "-=")
        print(18 * "-=")
        print("        --MENU PRINCIPAL--")
        print()
        print("> 1. CADASTRAR NOVO LIVRO")
        print("> 2. LISTAR LIVROS")
        print("> 3. BUSCAR LIVROS POR NOME")
        print("> 4. BUSCAR LIVROS POR CATEGORIA")
        print("> 5. BUSCAR LIVROS POR PREÇO")
        print("> 6. BUSCA POR QUANTIDADE EM ESTOQUE")
        print("> 7. VALOR TOTAL NO ESTOQUE")
        print("> 0. ENCERRAR ATIVIDADES")
        print()
        print(18 * "-=")

        pergunta_menu_interativo = int(input("Digite a opção desejada >>> "))

        opcao_escolhida_menu_interativo = self

        if pergunta_menu_interativo == 1:
            opcao_escolhida_menu_interativo.CadastrarNovoLivro()  # CONDICIONA O USUÁRIO AO MENU DE CADASTRO

        elif pergunta_menu_interativo == 2:
            opcao_escolhida_menu_interativo.info()

        elif pergunta_menu_interativo == 3:
            opcao_escolhida_menu_interativo.BuscaPorNome()

        elif pergunta_menu_interativo == 4:
            opcao_escolhida_menu_interativo.BuscaPorCategoria()

        elif pergunta_menu_interativo == 5:
            opcao_escolhida_menu_interativo.BuscaPorPreco()

        elif pergunta_menu_interativo == 6:
            opcao_escolhida_menu_interativo.BuscaPorQuantidadeEmEstoque()

        elif pergunta_menu_interativo == 7:
            opcao_escolhida_menu_interativo.BuscaPorValorDeEstoque()

        else:
            if pergunta_menu_interativo == 0:
                print()
                print(18 * "-=")
                print()
                print('             OBRIGADO')
                sys.exit()

    def CadastrarNovoLivro(self):  # OPÇÃO 1
        print()
        print(18 * "-=")
        print("     >> CADASTRO DE LIVROS <<")

        while True:
            novo_livro = []

            print()
            codigo = input(">> Código do livro: ")
            novo_livro.append(codigo)

            titulo = input(">> Título do livro: ")
            novo_livro.append(titulo)

            editora = input(">> Editora do livro: ")
            novo_livro.append(editora)

            categoria = input(">> Categoria do livro: ")
            novo_livro.append(categoria)

            ano = int(input('>> Ano do livro: '))
            novo_livro.append(ano)

            valor = int(input('>> Valor do livro: '))
            novo_livro.append(valor)

            quantidade_em_estoque = int(input('>> Digite a quantidade em estoque do livro: '))
            novo_livro.append(quantidade_em_estoque)

            self.livros.append(novo_livro)

            # INTERAÇÃO-#INTERAÇÃO-#INTERAÇÃO-#INTERAÇÃO

            print()
            print(18 * "-=")
            print()
            print('    LIVRO CADASTRADO COM SUCESSO!')
            print()
            print('> OPÇÕES:')
            print("> 1. CADASTRAR NOVO LIVRO")
            print("> 2. VOLTAR AO MENU PRINCIPAL")
            print()

            pergunta_cadastro_novo_livro = int(input("Digite a opção desejada >>  "))

            opcao_escolhida_cadastrar_novo_livro = self

            if pergunta_cadastro_novo_livro == 2:
                opcao_escolhida_cadastrar_novo_livro.MenuInterativo()
                break

    def BuscaPorNome(self):  # OPÇÃO 3 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("     --BUSCAR LIVRO POR NOME--")

        while True:
            print()
            pergunta_1_busca_por_nome = input("Digite o nome do livro (ou 0 para sair): ")

            opcao_escolhida_busca_por_nome = self

            if pergunta_1_busca_por_nome.lower() != "0":  # Se o usuário digitou algum nome

                controle_de_iteracoes_busca_nome = 0
                for informacoes_livros in range(
                        len(self.livros)):  # Busca por nome - itera sobre as informações de cada livro
                    if pergunta_1_busca_por_nome.lower() == self.livros[informacoes_livros][1].lower():
                        print()
                        print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                              f"Título/Editora: {self.livros[informacoes_livros][1]}/{self.livros[informacoes_livros][2]}\n"
                              f"Categoria: {self.livros[informacoes_livros][3]}\n"
                              f"Ano: {self.livros[informacoes_livros][4]}\n"
                              f"Valor: R$ {self.livros[informacoes_livros][5]}\n"
                              f"Estoque: {self.livros[informacoes_livros][6]} unidades\n"
                              f"Valor em Estoque: R$ {self.livros[informacoes_livros][6] * self.livros[informacoes_livros][5]}")
                    else:
                        controle_de_iteracoes_busca_nome += 1

                if controle_de_iteracoes_busca_nome == len(self.livros):
                    print()
                    print("LIVRO NÃO ENCONTRADO!")
                    print()
                    print("> 1. Buscar novo livro")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_nome = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_nome != 1:
                        opcao_escolhida_busca_por_nome.MenuInterativo()


                else:
                    print(18 * "-=")
                    print(f"Nome informado: {pergunta_1_busca_por_nome}")
                    print(f"Quantidade de livros encontrados: {len(self.livros) - controle_de_iteracoes_busca_nome}")
                    print()
                    pergunta_3_busca_por_nome = input("Gostaria de consultar outro livro (s/ n)? ")

                    if pergunta_3_busca_por_nome.lower() == "n":
                        opcao_escolhida_busca_por_nome.MenuInterativo()

            else:
                if pergunta_1_busca_por_nome == "0":
                    opcao_escolhida_busca_por_nome.MenuInterativo()

    def BuscaPorCategoria(self):  # OPÇÃO 4 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("   --BUSCAR LIVRO POR CATEGORIA--")
        print()

        while True:
            pergunta_1_busca_por_categoria = input("Digite o nome da categoria (ou 0 para sair): ")

            opcao_escolhida_busca_por_categoria = self

            if pergunta_1_busca_por_categoria.lower() != "0":

                controle_de_iteracoes_busca_categoria = 0
                for informacoes_livros in range(len(self.livros)):
                    if pergunta_1_busca_por_categoria.lower() == self.livros[informacoes_livros][3].lower():
                        print()
                        print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                              f"Título/Editora: {self.livros[informacoes_livros][1]}/{self.livros[informacoes_livros][2]}\n"
                              f"Categoria: {self.livros[informacoes_livros][3]}\n"
                              f"Ano: {self.livros[informacoes_livros][4]}\n"
                              f"Valor: R$ {self.livros[informacoes_livros][5]}\n"
                              f"Estoque: {self.livros[informacoes_livros][6]} unidades\n"
                              f"Valor em Estoque: R$ {self.livros[informacoes_livros][6] * self.livros[informacoes_livros][5]}")


                    else:
                        controle_de_iteracoes_busca_categoria += 1

                if controle_de_iteracoes_busca_categoria == len(self.livros):
                    print()
                    print("CATEGORIA NÃO ENCONTRADA!")
                    print()
                    print("> 1. Buscar nova categoria")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_categoria = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_categoria != 1:
                        opcao_escolhida_busca_por_categoria.MenuInterativo()


                else:
                    print(18 * "-=")
                    print(f"Categoria informada: {pergunta_1_busca_por_categoria}")
                    print(f"Total de livros: {len(self.livros) - controle_de_iteracoes_busca_categoria}")
                    print()
                    pergunta_3_busca_por_categoria = input("Gostaria de consultar outra categoria (s/n)? ")

                    if pergunta_3_busca_por_categoria.lower() == "n":
                        opcao_escolhida_busca_por_categoria.MenuInterativo()

            else:
                if pergunta_1_busca_por_nome == "0":
                    opcao_escolhida_busca_por_nome.MenuInterativo()

    def BuscaPorPreco(self):  # OPÇÃO 5 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("   --BUSCAR LIVROS POR PREÇO--")
        print()

        while True:
            print()
            pergunta_1_busca_por_preco = int(input("Digite seu valor máximo (ou 0 para sair): "))

            opcao_escolhida_busca_por_preco = self

            if pergunta_1_busca_por_preco != 0:

                controle_de_iteracoes_busca_preco = 0

                for informacoes_livros in range(len(self.livros)):
                    if self.livros[informacoes_livros][5] <= pergunta_1_busca_por_preco:

                        print()
                        print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                              f"Título/Editora: {self.livros[informacoes_livros][1]}/{self.livros[informacoes_livros][2]}\n"
                              f"Categoria: {self.livros[informacoes_livros][3]}\n"
                              f"Ano: {self.livros[informacoes_livros][4]}\n"
                              f"Valor: R$ {self.livros[informacoes_livros][5]}\n"
                              f"Estoque: {self.livros[informacoes_livros][6]} unidades\n"
                              f"Valor em Estoque: R$ {self.livros[informacoes_livros][6] * self.livros[informacoes_livros][5]}")
                    else:
                        controle_de_iteracoes_busca_preco += 1

                if controle_de_iteracoes_busca_preco == len(self.livros):
                    print()
                    print("PREÇO ESTIMADO INEXISTENTE!")
                    print()
                    print("> 1. Solicitar nova busca")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_preco = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_preco != 1:
                        opcao_escolhida_busca_por_preco.MenuInterativo()


                else:
                    print(18 * "-=")
                    print(f"Preço informado: {pergunta_1_busca_por_preco}")
                    print(f"Total de livros com preço estimado: {len(self.livros) - controle_de_iteracoes_busca_preco}")
                    print()
                    pergunta_3_busca_por_preco = input("Gostaria de colicitar uma nova busca (s/n)? ")

                    if pergunta_3_busca_por_preco.lower() == "n":
                        opcao_escolhida_busca_por_preco.MenuInterativo()

            else:
                if pergunta_1_busca_por_preco == 0:
                    opcao_escolhida_busca_por_preco.MenuInterativo()

    def BuscaPorQuantidadeEmEstoque(self):  # OPÇÃO 6 DO MENU INTERATIVO
        print()
        print(10 * "-=")
        print("--BUSCAR LIVRO POR QUANTIDADE EM ESTOQUE--")
        print()

        while True:
            print()
            pergunta_1_busca_por_estoque = int(input("Digite a quantidade desejada (ou 0 para sair): "))

            opcao_escolhida_busca_por_estoque = self

            if pergunta_1_busca_por_estoque != 0:

                controle_de_iteracoes_busca_por_estoque = 0

                for informacoes_livros in range(len(self.livros)):
                    if self.livros[informacoes_livros][6] <= pergunta_1_busca_por_estoque:
                        print()
                        print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                              f"Título: {self.livros[informacoes_livros][1]}\n"
                              f"Quantidade Em Estoque: {self.livros[informacoes_livros][6]} unidades")
                    else:
                        controle_de_iteracoes_busca_por_estoque += 1

                if controle_de_iteracoes_busca_por_estoque == len(self.livros):
                    print()
                    print("QUANTIDADE ESTIMADA INEXISTENTE!")
                    print()
                    print("> 1. Solicitar nova busca")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_por_estoque = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_por_estoque != 1:
                        opcao_escolhida_busca_por_estoque.MenuInterativo()


                else:
                    print()
                    print(18 * "-=")
                    print(f"Quantidade informada: {pergunta_1_busca_por_estoque}")
                    print(
                        f"Total de livros com quantidade em estoque estimada: {len(self.livros) - controle_de_iteracoes_busca_por_estoque}")
                    print()
                    pergunta_3_busca_por_estoque = input("Gostaria de solicitar uma nova busca (s/n)? ")

                    if pergunta_3_busca_por_estoque.lower() == "n":
                        opcao_escolhida_busca_por_estoque.MenuInterativo()

            else:
                if pergunta_1_busca_por_estoque == 0:
                    opcao_escolhida_busca_por_estoque.MenuInterativo()

    def BuscaPorValorDeEstoque(self):  # OPÇÃO 7
        print()
        print(10 * "-=")
        print("--BUSCA DE PRODUTO POR VALOR EM ESTOQUE--")
        print()

        while True:
            print()
            pergunta_1_busca_por_valor_de_estoque = int(input("Digite o valor mínimo da busca: (0 - SAIR): "))

            opcao_escolhida_busca_por_valor_de_estoque = self

            if pergunta_1_busca_por_valor_de_estoque != 0:

                controle_de_iteracoes_busca_por_valor_de_estoque = 0

                for informacoes_livros in range(len(self.livros)):
                    controle_de_valor_total_de_estoque = self.livros[informacoes_livros][6] * \
                                                         self.livros[informacoes_livros][5]
                    if pergunta_1_busca_por_valor_de_estoque < controle_de_valor_total_de_estoque:
                        print()
                        print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                              f"Título: {self.livros[informacoes_livros][1]}\n"
                              f"VALOR TOTAL EM ESTOQUE: {self.livros[informacoes_livros][6] *
                                                         self.livros[informacoes_livros][5]}\n"
                              f"Quantidade em Estoque: {self.livros[informacoes_livros][6]} unidades")
                    else:
                        controle_de_iteracoes_busca_por_valor_de_estoque += 1

                if controle_de_iteracoes_busca_por_valor_de_estoque == len(self.livros):
                    print()
                    print("VALOR ESTIMADO INEXISTENTE!")
                    print()
                    print("> 1. Solicitar nova busca")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_por_valor_de_estoque = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_por_valor_de_estoque != 1:
                        opcao_escolhida_busca_por_valor_de_estoque.MenuInterativo()


                else:
                    print()
                    print(18 * "-=")
                    print(f"Valor informado : {pergunta_1_busca_por_valor_de_estoque}")
                    print(f"Total de livros com valor estimado em estoque: "
                          f"{len(self.livros) - controle_de_iteracoes_busca_por_valor_de_estoque}")
                    print()
                    pergunta_3_busca_por_valor_de_estoque = input("Gostaria de solicitar uma nova busca (s/n)? ")

                    if pergunta_3_busca_por_valor_de_estoque.lower() == "n":
                        opcao_escolhida_busca_por_valor_de_estoque.MenuInterativo()

            else:
                if pergunta_1_busca_por_valor_de_estoque == "0":
                    opcao_escolhida_busca_por_valor_de_estoque.MenuInterativo()


SistemaDeCadastros().MenuInterativo()
