class Aluno:
    def __init__(self,nome_completo,curso,matricula):
        self.nome_completo = nome_completo
        self.curso = curso
        self.matricula = matricula
        self.email = f'{self.matricula}@aluno.ifrs.edu.br'
        self.nota = {}


    def info(self):
        print(10*"-=")
        print (f'Nome: {self.nome_completo}\nCurso: {self.curso}\nMatrícula: {self.matricula}\n'
                 f'Email:{self.email}')

    def alterarNotas(self,disciplina,novaNota):
        self.disciplina = disciplina
        self.novaNota = novaNota

        self.nota[self.disciplina] = novaNota

if __name__ == '__main__':
    aluno1 = Aluno("Leonardo","ADS","2024016743")
    aluno1.nota["ADS"] = 10
    aluno2 = Aluno("Lucas","Música","2024016740")
    aluno2.nota["Música"]=10
    aluno3 = Aluno("Millena","Psicologia","2024016850")
    aluno3.nota["Psicologia"]=10

    # aluno1.info()
    # print(aluno1.nota)
    #
    # aluno1.alterarNotas("ADS", 10)
    # aluno1.alterarNotas("Banco de Dados", 8.9)
    # aluno1.alterarNotas("Arq e Org Comp", 9.0)
    #
    # aluno1.info()
    # print(aluno1.nota)
    #
    # aluno2.info()
    # print(aluno2.nota)
    #
    # aluno2.alterarNotas("HTML", 9.8)
    # aluno2.alterarNotas("ADS", 8.9)
    # aluno2.alterarNotas("Metodologia", 7.7)
    #
    # aluno2.info()
    # print(aluno2.nota)
    #
    # aluno3.info()
    # print(aluno3.nota)
    #
    # aluno3.alterarNotas("Programação", 9.8)
    # aluno3.alterarNotas("Libreoffice", 8.9)
    # aluno3.alterarNotas("Metodologia", 7.7)
    #
    # aluno3.info()
    # print(aluno3.nota)

class Produto:
    def __init__(self, marca, modelo, valor, estoque):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.estoque = estoque

    def alterarValor(self, novoValor):
        self.valor=novoValor

    def alterarEstoque(self,novoEstoque):
        self.estoque=novoEstoque

    def info(self):
        print(10 * "-=")
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nValor: {self.valor}\nEstoque: {self.estoque}")


if __name__ == '__main__':
    produto1 = Produto("Tagima", "Squier", 1.000, 274)
    produto2 = Produto("Sizal", "Pencil", 1.987, 387)
    produto3 = Produto("Volvo", "utilitário", 21.244, 837)

    # produto1.info()
    # produto1.alterarValor(1000)
    # produto1.alterarEstoque(1000)
    # produto1.info()
    # 
    # produto2.info()
    # produto2.alterarValor(1000)
    # produto2.alterarEstoque(1000)
    # produto2.info()
    # 
    # produto3.info()
    # produto3.alterarValor(1000)
    # produto3.alterarEstoque(1000)
    # produto3.info()

