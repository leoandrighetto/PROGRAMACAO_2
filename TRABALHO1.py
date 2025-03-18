class Livros:
    def __init__(self, titulo, codigo, editora, area, ano, valor, quantidade_em_estoque):
        self.titulo=titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.quantidade_em_estoque = quantidade_em_estoque

    def CadastroDeLivros(self,Livros):
        print(10 * "-=")
        print("CADASTRO DE LIVRO")
        print()

        registro_de_livros = {}

        while True:

            self.livro={}

            codigo = int(input("Informe o código do Livro: "))
            livro.update({"codigo": codigo})
            titulo = input("Informe o título do Livro: ")
            livro.update({"titulo":titulo})
            editora = input("Informe a editora  do Livro: ")
            livro.update({"editora":editora})
            categoria = input("Informe a categoria do Livro: ")
            livro.update({"categoria":categoria})
            valor = int(input("Informe o valor do Livro: "))
            livro.update({"valor": valor})
            quantidade_em_estoque = int(input("Informe a quantidade em estoque do Livro: "))
            livro.update({"quantidade_em_estoque":quantidade_em_estoque})

            registro_de_livros[codigo]=self.livro

            print()
            interação_1 = input("Deseja cadastar mais livros (S/N)? ")

            if interação_1.lower() == "n":
                break

        for i,a in registro_de_livros.items():
            print(f"{i}-{a}")

Livros.CadastroDeLivros(Livros)



