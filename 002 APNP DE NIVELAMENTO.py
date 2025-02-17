import sys

def menu():

    print(15* '-=')
    print("F.1 = CADASTRO DE ALUNO")
    print("F.2 = INFORMAÇÕES DE ALUNOS")
    print('F.3 = MODIFICAR NOTA DE ALUNO')
    print('F.4 = MÉDIA DAS NOTAS DOS ALUNOS')
    print('F.0 = SAIR DO SISTEMA')
    print(15* '-=')

    while True:

        per = input('Digite a função desejada (ex: "f1"): ')

        if per.lower()=='f1':
            cadastro()

        elif per.lower()=='f2':
            informacoes()

        elif per.lower()=='f3':
            modNotas()

        elif per.lower() =='f4':
            media()

        elif per.lower()=='f0':
            print()
            print('O SISTEMA FOI ENCERRADO!')
            sys.exit()
        else:
            print('FUNÇÃO INVÁLIDA.')

alunos = []

def cadastro():

    while True:

        aluno = []

        while True:
            nome = str(input('Digite o nome do aluno: '))
            if not nome.replace(' ','').isalpha():
                print('DADOS INVÁLIDOS. Os nomes só podem conter letras')
            else:
                aluno.append(nome)
                break

        while True:
            try:
                nota = float(input('Digite a nota do aluno: '))
                if nota >=0 and nota <= 10:
                    aluno.append(nota)
                    break
                else:
                    print('DADOS INVÁLIDOS. Digite apenas números de 1 a 10')
            except ValueError:
                print('DADOS INVÁLIDOS.Digite apenas números de 1 a 10')

        alunos.append(aluno)


        per = input('Deseja adicionar mais alunos(S/N)? ')

        if per.lower() == "n":
            menu()
            break
        elif per.lower() != "s":
            print('OPÇÃO INVÁLIDA')


def informacoes():
    if not alunos:
        print('NÃO EXISTEM ALUNOS CADASTRADOS!')
        per = input('Deseja cadastrar um aluno (S/N)? ')
        if per.lower() =='s':
            cadastro()
        else:
            menu()
        
    else:
        for i, a in enumerate(alunos):
            #FOR NUMERAÇÃO , ALUNO->(SUBLISTA)<  IN ENUMERATE(LISTA):
            #ALUNOS = [[NOME,NOTA],[NOME,NOTA]]
            
            print (f'NOME: {a[0]} | MATRÍCULA: {i} | NOTA {a[1]} ')

            #a[0] = o índice 0 na sublista aluno é o NOME.
            #i = é uma iteração que começa no número 0 (MATRÍCULA)
            #a[1] = o índice 1 na sublista aluno é a NOTA.

        while True:    
            per = input('Deseja cadastrar um novo aluno (S/N)? ')
            if per.lower()=='s':
                cadastro()
            elif per.lower()=='n':
                menu()
            else:
                print('OPÇÃO INVÁLIDA!')


def modNotas():
    if not alunos:
        print('NÃO EXISTEM ALUNOS CADASTRADOS!')
        per = input('Deseja cadastrar um aluno (S/N)? ')
        if per.lower() =='s':
            cadastro()
        else:
            menu()
    else:
        
        while True:
            matricula = int(input('Nº da matrícula: '))
            try:
                nova = float(input('Nova  nota: '))

                if nova >=0 and nova <= 10:
                    alunos[matricula][1] = nova

                    print('NOTA ATUALIZADA!')

                    while True:
                        per = str(input('Deseja atualizar mais notas(S/N)? '))
                        if per.lower() == 'n':
                            menu()
                        elif per.lower() != 's':
                            print('OPÇÃO INVÁLIDA!')
                        else:
                            break
                   
                else:
                    print('DADOS INVÁLIDOS. Digite apenas números de 1 a 10')

            except ValueError:
                print('DADOS INVÁLIDOS.Digite apenas números de 1 a 10')

def media():
    if not alunos:
        print('NÃO EXISTEM ALUNOS CADASTRADOS!')
        per = input('Deseja cadastrar um aluno (S/N)? ')
        if per.lower() =='s':
            cadastro()
        else:
            menu()
    
    else:
        soma = 0
        for i in alunos:
            soma+=i[1]

        cal = soma/len(alunos)
        print(f'MÉDIA DOAS ALUNOS = {cal:.2f}')


        
menu()
