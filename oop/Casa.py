class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros

    def mostrar_cor(self):
        print(f'A cor da casa é: {self.cor}')

    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quartos')

    def mostrar_banheiros(self):
        print(f'Esta casa tem {self.banheiros} banheiros')

    def adicionar_quarto(self):
        self.quartos = self.quartos + 1
