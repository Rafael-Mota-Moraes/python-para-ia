class Cachorro:
    def emitir_som(self):
        print('Au au')


class Gato:
    def emitir_som(self):
        print('Miau')


animais = [Gato(), Cachorro()]

for a in animais:
    a.emitir_som()
