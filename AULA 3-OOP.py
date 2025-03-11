class Pessoa:
    def __init__(self):
        nome =''
        sobrenome=''
        idade=''

if __name__ == '__main__':
    p1=Pessoa()
    p2=Pessoa()
    p3=Pessoa()
    p1.nome='Leonardo'
    p1.sobrenome='Andrighetto'
    p1.idade='27'
    p2.nome = 'Paola'
    p2.sobrenome = 'Medina'
    p2.idade = '27'
    p3.nome = 'Millena'
    p3.sobrenome = 'Andrighetto'
    p3.idade = '23'

print(p1.nome,p1.sobrenome,p1.idade)
print(p2.nome,p2.sobrenome,p2.idade)
print(p3.nome,p3.sobrenome,p3.idade)

class Pessoa:
    def __init__(self,nome,sobrenome,idade):
        self.nome=nome
        self.sobrenome=sobrenome
        self.idade=idade

    def __str__(self):
        return f'Nome: {self.nome} Sobrenome: {self.sobrenome} Idade: {self.idade}'


if __name__ == '__main__':

    p1=Pessoa("Leonardo",'andrigheto','27')
    p2=Pessoa("Paola",'Medina','27')
    p3=Pessoa('Millena','Andrighetto','23')

    print(p1)
    print(p2)
    print(p3)


class Empresa:
    def __init__(self,nome,cnpj,endereco,servico):
        self.nome=nome
        self.cnpj=cnpj
        self.endereco=endereco
        self.servico=servico

    def __str__(self):
        return f'Nome da Empresa: {self.nome}, CNPJ: {self.cnpj},Endereço: {self.endereco}, Serviço: {self.servico}'
if __name__ == '__main__':
    lista_de_empresas=[]
    lista_de_empresas.append(Empresa('Coremei','20321645','rua tal paranauê', 'instalar coisas'))
    lista_de_empresas.append(Empresa('Meumei','6548987','rua tal taltal', 'instalar mais coisas'))
    lista_de_empresas.append(Empresa('BlaBlamei','65465465','rua tal paranauê', 'instalar muito mais coisas'))
    for i in lista_de_empresas:
        print(i)

print()

class Remedio:
    def __init__(self,nome,tarja,valor,laboratorio,estoque):
        self.nome=nome
        self.tarja=tarja
        self.valor=valor
        self.laboratorio=laboratorio
        self.estoque=estoque

    def __str__(self):

        return f'Nome do remédio: {self.nome}, Tarja: {self.tarja},Valor: {self.valor} Laboratorio: {self.laboratorio}, Estoque: {self.estoque}'
if __name__ == '__main__':
    lista_de_remedios=[]
    lista_de_remedios.append(Remedio('Paracetamol','branca',"12,33",'Av. Parana','1234'))
    lista_de_remedios.append(Remedio('Dipirona','Branca','34,34','Av. Paranauê','654897'))
    lista_de_remedios.append(Remedio('Fluvelozfurioz','Roxa','23,34','Av. Bonar figueiro','979784'))
    for i in lista_de_remedios:
        print(i)

print()

class Funcionario:
    def __init__(self,nome,sobrenome,cpf,salario,cargo):
        self.nome=nome
        self.sobrenome=sobrenome
        self.cpf=cpf
        self.salario=salario
        self.cargo=cargo

    def __str__(self):
        return f'Nome do Funcionario: {self.nome} {self.sobrenome}, CPF: {self.cpf}, Salario: {self.salario}, Cargo: {self.cargo}'


if __name__ == '__main__':
    lista_de_funcionarios=[]
    lista_de_funcionarios.append(Funcionario('Leonardo','Andrighetto','0456789421','5.000','Programador'))
    lista_de_funcionarios.append(Funcionario('Paola', 'Medina', '65498731', '5.000', 'Programadora'))
    lista_de_funcionarios.append(Funcionario('Millena', 'Andrighetto', '111223546', '5.000', 'Escritora'))

for i in lista_de_funcionarios:
    print(i)

print()

class Livro:
    def __init__(self,titulo,isbn,valor,autor,editora,estoque):
        self.titulo=titulo
        self.isbn=isbn
        self.valor=valor
        self.autor=autor
        self.editora=editora
        self.estoque=estoque
    def __str__(self):
        return f"Título: {self.titulo}, ISBN: {self.isbn}, Valor: {self.valor}, Autor: {self.autor}, Editora: {self.editora}, Estoque: {self.estoque}"


if __name__ == '__main__':
    lista_de_livros=[]
    lista_de_livros.append(Livro('Harry Potter','6548789','44,35','J.K Rowling','Maravilha','9.456.554'))
    lista_de_livros.append(Livro('Harry Potter 2','1234545','23,77','J.K Rowling','Maravilha','6.776.876'))
    lista_de_livros.append(Livro('Harry Potter 3','123423','46,56','J.K Rowling','Maravilha','9.123.456'))

    for i in lista_de_livros:
        print(i)
