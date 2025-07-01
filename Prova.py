class Pessoa:

    __todas_as_pessoas = [] # << Este é um atributo da Classe. E como ele é global, não precisa ter um @property.

    def __init__(self, nome_completo, cpf, telefone, email):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return (f'| Nome: {self.nome_completo}\n'
                f'| CPF: {self.cpf}\n'
                f'| Telefone: {self.telefone}\n'
                f'| Email: {self.email}')

    # Método de classe é usado para instanciar objetos através da entrada do usuário.

    @classmethod
    def criar_pessoa(cls):
        nome_pessoa = input('Digite o nome da pessoa: ')
        cpf_pessoa = input('Digite o CPF da pessoa: ')
        telefone_pessoa = input('Digite o telefone da pessoa: ')
        email_pessoa = input('Digite o email da pessoa: ')

        nova_pessoa = Pessoa(nome_pessoa,cpf_pessoa,telefone_pessoa,email_pessoa)

        Pessoa.__todas_as_pessoas.append(nova_pessoa)

    def altera_contato(self, tel_novo,email_novo):
        self.telefone = tel_novo
        self.email = email_novo

    def altera_contato_input(self):
        novo_telefone = input('digite o novo telefone: ')
        novo_email = input('digite o novo email: ')

        if novo_telefone != "++":
            self.telefone =novo_telefone

        if novo_email != "++":
            self.email = novo_email

        return f'{self.email}, {self.telefone}'


class Cliente(Pessoa):

    _todos_os_clientes = []

    def __init__(self, nome_completo, cpf, telefone, email, cep, endereco_completo):
        super().__init__(nome_completo, cpf, telefone, email)

        self.cep = cep
        self.endereco_completo = endereco_completo

    @classmethod
    def criar_cliente(cls):

        nome_cliente = input('Digite o nome do cliente: ')
        cpf_cliente = input('Digite o CPF do cliente: ')
        telefone_cliente = input('Digite o telefone do cliente: ')
        email_cliente = input('Digite o email do cliente: ')
        cep_cliente = input('Digite o CEP do cliente: ')
        endereco_cliente= input('Digite o endereço do cliente: ')

        cliente_novo = Cliente(nome_cliente,cpf_cliente,telefone_cliente,email_cliente,cep_cliente,endereco_cliente)
        cls._todos_os_clientes.append(cliente_novo)

        return (f'\nCliente criado com sucesso \n'
                f'> {cliente_novo.nome_completo}\n'
                f'> {cliente_novo.cpf}\n'
                f'> {cliente_novo.email}\n'
                f'> {cliente_novo.cep}\n'
                f'> {cliente_novo.endereco_completo}\n')

    def info(self):
        return (f'| Nome: {self.nome_completo}\n'
                f'| CPF: {self.cpf}\n'
                f'| Telefone: {self.telefone}\n'
                f'| Email: {self.email}\n'
                f'| CEP: {self.cep}\n'
                f'| Endereço Completo: {self.endereco_completo}')

    def altera_endereco(self, cep_novo, endereco_novo):
        self.cep = cep_novo
        self.endereco_completo = endereco_novo

    @classmethod
    def acesso_lista_clientes(cls):
        return cls._todos_os_clientes


class Entregador(Pessoa):

    _todos_os_entregadores = []

    def __init__(self, nome_completo, cpf, telefone, email, empresa):
        super().__init__(nome_completo, cpf, telefone, email)
        self.empresa = empresa
        self.lista_entregas = []

    @classmethod
    def criar_entregador(cls):
        nome_entregador = input('Digite o nome do entregador: ')
        cpf_entregador = input('Digite o CPF do entregador: ')
        telefone_entregador = input('Digite o telefone do entregador: ')
        email_entregador = input('Digite o email do entregador: ')
        empresa_entregador = input('Digite o nome da empresa do entregador: ')

        novo_entregador = Entregador(nome_entregador,
                                     cpf_entregador,
                                     telefone_entregador,
                                     email_entregador,
                                     empresa_entregador)

        cls._todos_os_entregadores.append(novo_entregador)

        return (f"Entregador criado:\n"
               f'> {novo_entregador.nome_completo}\n'
                f'> {novo_entregador.cpf}\n'
                f'> {novo_entregador.email}\n'
                f'> {novo_entregador.telefone}\n'
                f'> {novo_entregador.empresa}\n')

    @classmethod
    def acesso_lista_entregadores(cls):
        return cls._todos_os_entregadores

    def info(self):
        return (f'| Nome: {self.nome_completo}\n'
                f'| CPF: {self.cpf}\n'
                f'| Telefone: {self.telefone}\n'
                f'| Email: {self.email}\n'
                f'| Empresa: {self.empresa}\n')

    def aloca_entrega(self, nova_entrega):
        pass


class Entrega:

    todas_as_entregas = []

    def __init__(self, cod_entrega, entregador, cliente, situacao):
        self.cod_entrega = cod_entrega
        self.entregador = entregador
        self.cliente = cliente
        self.situacao = situacao

    @classmethod
    def criar_entrega(cls):
        nome_codigo = input('digite o nº do código: ')
        nome_entregador = input('digite o nome do entregador: ')
        nome_cliente = input('digite o nome do cliente: ')
        nome_situacao = input('Digite a situação da entrega: ')

        obj_entregador = None
        obj_cliente = None

        for entregador in Entregador.acesso_lista_entregadores():
            if entregador.nome_completo == nome_entregador.lower():
                obj_entregador = entregador
                break

        for cliente in Cliente.acesso_lista_clientes():
            if cliente.nome_completo == nome_cliente.lower():
                obj_cliente = cliente
                break

        if obj_entregador is None:
            return f'Entregador não encontrado'

        if obj_cliente is None:
            return 'Cliente não encontrado'


        nova_entrega = Entrega(nome_codigo, obj_entregador, obj_cliente, nome_situacao)
        return (f'Entrega Cadastrada:\n'
                f'Código: {nova_entrega.cod_entrega}\n'
                f'Entregador:\n'
                f'{nova_entrega.entregador}\n'
                f'Cliente:\n'
                f'{nova_entrega.cliente}\n'
                f'Situação: {nova_entrega.situacao}\n')

    def info(self):
        return (f'Entrega/Situação: #{self.cod_entrega} / {self.situacao}\n'
                f'Entregador: {self.entregador.nome_completo}\n'
                f'Endereço: {self.cliente.endereco_completo}\n'
                f'Cliente: {self.cliente.nome_completo} / {self.cliente.cpf}')

    def atualiza_situacao(self,nova_situacao):

        self.situacao = nova_situacao
        return (f'Situação atualizada:\n'
                f'{nova_situacao}')


if __name__ == '__main__':

    #Pessoa.criar_pessoa()

    # pessoa1 = Pessoa('Leonardo','04188248000','5199365784','Leo@gmail.com')
    # print(pessoa1)
    # print()
    # print(pessoa1.altera_contato_input())
    # print()

    # print(Cliente.criar_cliente())
    # print(Entregador.criar_entregador())
    # print(Cliente.criar_cliente())
    # print(Entrega.criar_entrega())
    entrega1 = Entrega("001",
                       Entregador('leo','01','5190','leo@','leleo00'),
                       Cliente('leo','01','5190','leo@','leleo00','Acesso b'),
                       'a caminho')

    print(entrega1.info())