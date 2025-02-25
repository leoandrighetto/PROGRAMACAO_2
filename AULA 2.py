def calculo(a,b,c):
        if c.lower() == "+":
            print(a+b)
        elif c.lower() == "-":
            print(a-b)
        elif c.lower() == "*":
            print(a*b)
        elif c.lower() == "/":
            print(a/b)

def somalista(a=[]):
    return sum(a)

def teste(**teste):
    for a, b in teste.items():
        print(f'{a}: {b}')

def coisa(*a):
    return a


calculo(10,2,'+')
calculo(10,2,'-')
calculo(10,2,'*')
calculo(10,2,'/')

print()

print(somalista([1,1,1,1,1]))

print()


print(coisa(1,2,3))
print()
teste(nome='Leonardo',idade="27",profissão='Programador')






# Lista de Exercícios - Funções

# Crie uma função que recebe dois argumentos, nome e sobrenome, e retorna uma string com o nome completo.
def doisargumentos(nome,sobrenome):
    print(nome,sobrenome)

doisargumentos("Leonardo","Linhares")

# Crie uma função que realize operação de soma para dois argumentos recebidos.
def soma(a,b):
    print(a+b)
soma(2,2)

# Crie uma função que receba dois argumentos double, realize as operações aritméticas básicas (soma, subtração, multiplicação e divisão) entre os valores e escreva na  tela os resultados.
def somafloats(a=float,b=float):
    print(a+b)
    print(a - b)
    print(a * b)
    print(a / b)

somafloats(4.6,2.4)

# Crie uma função que receba uma lista de inteiros como argumento e tem como retorno o menor valor contido no lista.

def menorvalorlista(a=[]):
    print(min(a))

menorvalorlista([1,5,6])

# Crie uma função que receba uma lista de double como argumento e tenha como retorno o somatório dos valores contidos.

def somalistafloat(a=[]):
    print(sum(a))

somalistafloat([2.3,2.3])

# Crie uma função que receba uma lista de inteiros como argumento e tem como retorno o índice do menor valor contido no lista.

def menorindice(a=[]):
    print(a.index(min(a)))

menorindice([5,4,1])

# Receba duas listas de inteiros como argumentos, multiplique os valores entre as listas índice a índice, e retorne o lista resultante da operação.

def duaslistas(a=[],b=[]):
    lista=[]
    for i in range(len(a)):
        c=a[i]+b[i]
        lista.append(c)

    print(lista)

duaslistas([1,2,3,4],[1,2,3,4])
# Receba duas listas de string, concatena os valores contidos índice a índice separando os por “:” e escreva os resultados na tela.

def listasstring(a=[],b=[]):
    for i in range(len(a)):
        print(f"{a[i]}:{b[i]}")
listasstring(['Leo','Lena','Lucas'],['Eu','Irmã','Irmão'])

# Crie uma função que receba duas matrizes de double como argumento e escreva na tela o resultado das operações de soma e subtração entre elas.

def somamatrizes(a=[[],[]],b=[[],[]]):

    c = []
    d = []
    for i in range(2):
        for t in range(2):
            c.append(a[i][t] + b[i][t])
            d.append(a[i][t] - b[i][t])

    print(c)
    print(d)

somamatrizes([[5.0,4.1],[5.0,4.1]],[[4.0,1.1],[4.0,1.1]])
