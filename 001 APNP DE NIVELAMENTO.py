
def menu():
    print()
    print("F1 = CADASTRO")
    print("F2 = INFORMAÇÕES")
    print('F3 = MODIFICAR NOTA DO ALUNO')
    print('F4 = SAIR DO SISTEMA')
    print()
    while True:

        per = input('Digite a função desejada (ex: f1): ')

        if per.lower()=='f1':
            cadastro()

        elif per.lower()=='f2':
            informacoes()

        elif per.lower()=='f3':
            modNotas()

        elif per.lower()=='f4':
            print('O SISTEMA FOI FECHADO.')
            break
        else:
            print('FUNÇÃO INVÁLIDA.')

alunos = []

def cadastro():

    
    while True:

        aluno = []
        nome = input('Digite o nome do aluno: ')
        aluno.append(nome)

        nota = float(input('Digite a nota do aluno: '))
        aluno.append(nota)

        alunos.append(aluno)
        p = input('Deseja adicionar mais alunos(S/N)? ')

        if p.lower() == "n":
            menu()

def informacoes():
    if not alunos:
        print('NÃO EXISTEM ALUNOS CADASTRADOS!')
        per = input('Deseja cadastrar um aluno (S/N)? ')
        if per.lower() =='s':
            cadastro()
        else:
            menu()
        
    else:
        b = 000        
        for i,a in alunos:
            print (f'ALUNO: {i} | MATRÍCULA: {b} | NOTA {a} ')
            b+= 1
        while True:    
            per = input('Deseja cadastrar um novo aluno (S/N)? ')
            if per.lower()=='s':
                cadastro()
            elif per.lower()=='n':
                menu()
            else:
                print('OPÇÃO INVÁLIDA!')


menu()
