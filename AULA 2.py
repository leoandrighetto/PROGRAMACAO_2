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
