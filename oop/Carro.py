class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.ligado = True
        self.seta = None

    def informacoes(self):
        print(f'A cor do carro é: {self.cor}.')
        print(f'O ano do carro é: {self.ano}.')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('Agora o carro está ligado')
        else:
            print('O carro está ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro estava desligado')

    def ligar_seta(self, direcao):

        if not self.ligado:
            print('O carro está desligado, ligue o carro primeiro')
        else:
            self.seta = direcao
            print(f'Seta ligada para a {self.seta}')


carro1 = Carro('Branco', 2010)
carro1.informacoes()
carro1.ligar()
carro1.desligar()
carro1.ligar()
carro1.ligar_seta('esquerda')
carro1.ligar_seta('direita')
