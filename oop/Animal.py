class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou o {self.especie} chamado {self.nome}')


class Gato(Animal):
    def emitir_som(self):
        print('miau')

    def arranhar(self):
        print('o gato está arranhando')


class Cachorro(Animal):
    def emitir_som(self):
        print('au au au')


class Elefante(Animal):
    pass


gato1 = Gato('Felix', 'Branco', 'Siames')
gato1.apresentar()
gato1.emitir_som()
gato1.arranhar()

cachorro1 = Cachorro('Russo', 'Preto', 'Pastor Alemão')
cachorro1.apresentar()

elefante1 = Elefante('Fred', 'Marrom', 'Asiático')
elefante1.apresentar()
