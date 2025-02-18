#formas de formatar um print:

l =[1,2,3,4]

#1

print(f'X0 = {l[0]}')
print()

#2

print("X0 = "+str(l[0]))
print()


def linha():
    print()
    print(30*'-=')
    print()

# 1) Crie um algoritmo onde o usuário entra com 10 nomes diferentes em um vetor.

l=[]
for i in range(10):
    b = input('DIGITE UM NOME: ')
    l.append(b)

for i in l:
    print(l)

linha()


# 2) Faça um algoritmo cuja função seja preencher um vetor de tamanho 10 utilizando o
# comando de entrada de dados da linguagem (usuário entra com o valor). Em seguida
# escreva os valores contidos no vetor.

l2 = []
for i in range(10):
    b = input('DIGITE UM NÚMERO: ')
    l2.append(b)

for i in l:
    print(l2)

linha()

# 3) Faça um algoritmo com um vetor de tamanho 5 onde somente é permitido inserir
# valores maiores que 0 e menores que 10.

l3 = []

while len(l3) != 5:
    a = int(input('DIGITE UM NÚMERO DE 0 A 10: '))
    if 0 <= a <= 10:
        l3.append(a)
    else:
        print('DADO INVÁLIDO. Apenas de 0 a 10: ')

for i in l3:
    print(i)


# 4) Faça um algoritmo com vetor de 5 posições que digite valores e informe quem são
# múltiplos de 10.

l4=[]
for i in range(5):
    a = int(input('DIGITE UM NÚMERO: '))
    l4.append(a)

for i in l4:
    if (i%10) == 0:
        print(f'{i} é múltiplo de 10')
linha()

# 5) Elabore um algoritmo que receba um vetor de 5 posições e escreva os números
# ímpares, e indique em quais posições eles se encontram.

l5=[]
for i in range(5):
    a = int(input('DIGITE UM NÚMERO: '))
    l5.append(a)

for i in l5:
    if (i%2) != 0:
        print(f'{i} é ímpar e está na posição {l5.index(i)} na lista')

linha()

# 6) Elabore um algoritmo que receba um vetor de 5 posições e retorne a soma total
# desses valores.

l6=[]
for i in range(5):
    a = int(input('DIGITE UM NÚMERO: '))
    l6.append(a)
s=0
for i in l6:
    s+=i

print(s)

linha()

# 7) Elabore um algoritmo que receba um vetor de 5 posições e retorne o produto
# (multiplicação) total desses valores.

l6=[]
for i in range(5):
    a = int(input('DIGITE UM NÚMERO: '))
    l6.append(a)
s=1
for i in l6:
    s*=i

print(s)

linha()

# 8) Elabore um algoritmo que informe os valores contidos em uma matriz 2 linhas x 3
# colunas.

l7 = [[1,0,0],[0,1,0]]

for i in range(2):
    for b in range(3):
        print(l7[i][b])
print()
for i in l7:
    print(i)

linha()

# 9) Elabore um algoritmo que informe os valores contidos em uma matriz 4 linhas x 4
# colunas e realize a soma total dos valores existentes.

l8 =[[2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2]]
m = 0

for i in range(4):
    for a in range(4):
        print(l8[i][a])
        m+=l8[i][a]
print()
print(f'a soma dos valores da matriz é {m}')
linha()

# 10) Elabore um algoritmo que exiba na tela os valores contidos em uma matriz [3x3] linha
# a linha e realize a soma dos valores nas mesmas.

l9 =[[2,0,0,0],[0,2,0,0],[0,0,2,0]]
m = 0

for i in range(3):
    print(l9[i])
    for a in range(3):
        m+=l9[i][a]
print()
print(f'a soma dos valores da matriz é {m}')

linha()

# 11) Elabore um algoritmo que exiba na tela os contidos em uma matriz [3x3]
# coluna a coluna e realize a multiplicação dos valores.


l10 = [[1,0,0],[0,1,0],[0,0,1]]
s=0
for i in range(3):
    for a in range(3):
        print(l10[i][a])
        s+=l10[i][a]
print()
print(f'a soma é {s}')
