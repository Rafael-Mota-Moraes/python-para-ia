class Animal:
    def __init__(self, nome):
        self.nome = nome


class Predador(Animal):
    def cacando(self):
        print(f'{self.nome} animal está caçando!')


class Presa(Animal):
    def fugindo(self):
        print(f'{self.nome} animal está sendo caçado!')


class Coelho(Presa):
    pass


class Tigre(Predador):
    pass


class Golfinho(Predador, Presa):
    pass


coelho = Coelho('Bunny')
coelho.fugindo()

tigre = Tigre('Tiger')
tigre.cacando()

golfinho = Golfinho('Walle')
golfinho.cacando()
golfinho.fugindo()
