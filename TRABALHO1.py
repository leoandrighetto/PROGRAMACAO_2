class Livros:
    def __init__(self, titulo, codigo, editora, area, ano, valor, quantidade_em_estoque):
        self.titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.quantidade_em_estoque = quantidade_em_estoque

    def CadastroDeLivros(self):
        print(10 * "-=")
        print("CADASTRO DE LIVRO")
        print()
        codigo = input("Informe o código do Livro: ")
        titulo = input("Informe o título do Livro: ")
        editora = input("Informe a editora  do Livro: ")
        categoria = input("Informe a categoria do Livro: ")
        valor = input("Informe o valor do Livro: ")
        quantidade_estoque = input("Informe a quantidade em estoque do Livro: ")

        registro_de_livros = {codigo[]}
