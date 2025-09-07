class Escola():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Meu nome é: {self.nome}')


class Aluno(Escola):
    def __init__(self, nome, idade, ano):
        super().__init__(nome, idade)
        self.ano = ano

    def apresentar(self):
        print(f'Meu nome é: {self.nome} e tenho {self.idade} anos')


class Professor(Escola):
    def __init__(self, nome, idade, ano):
        super().__init__(nome, idade)
        self.ano = ano

    def apresentar(self):
        print(f'Eu sou o professor')


class Assistente(Escola):
    def __init__(self, nome, idade, ano):
        super().__init__(nome, idade)
        self.ano = ano

    def apresentar(self):
        print(f'Eu sou assistente')


a1 = Aluno('Marcos', 12, 8)
a1.apresentar()
p1 = Professor('João', 47, 5)
p1.apresentar()
as1 = Assistente('Ana Maria', 29, 'Bloco C')
as1.apresentar()
