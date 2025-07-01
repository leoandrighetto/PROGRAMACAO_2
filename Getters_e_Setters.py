"""
    Métodos de acesso e modificação são usados para controlar atributos protegidos ou
    privados das instâncias. E podem ser usados para validação também.
"""

class Pessoa:

    def __init__(self, nome, telefone):
        self.nome = nome
        self._telefone = telefone

    def __str__(self):
        return f'Nome: {self.nome} | Telefone: {self._telefone}'

    # decorador que transforma um método comum em um getter,
    # que por sua vez, retorna um atributo protegido.
    @property
    def telefone(self):
        return self._telefone

    # Decorador que devolve o valor do objeto, modificado, ou de forma segura.
    @ telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

"""
Desta forma, o usuário nunca irá conseguir acessar DIRETAMENTE o atributo telefone.
Quem irá se encarregar deste trabalho será os métodos de acesso e modificação.
"""