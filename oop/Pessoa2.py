class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é: {self.nome} e tenho {self.idade} de idade')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        self.cargo = cargo
        super().__init__(nome, idade)

    def trabalhar(self):
        print(f'{self.nome} trabalha no cargo de {self.cargo}')


class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'Compra aprovada!')
            print(f'Seu novo saldo é de: {self.saldo}')
        else:
            print('Saldo insuficiente')


f1 = Funcionario('Maria', 38, 'Gerente de contas')
f1.apresentar()
f1.trabalhar()

c1 = Cliente('Artur', 16, 200)
c1.apresentar()
c1.comprar(10)
c1.comprar(200)
