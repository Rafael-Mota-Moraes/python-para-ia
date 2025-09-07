class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia


class Carro:
    def __init__(self):
        self.motores = []

    def adicionar_motor(self, motor):
        self.motores.append(motor)

    def listar_motores(self):
        for motor in self.motores:
            print(
                f'Marca: {motor.marca} - {motor.potencia} cavalos de potência.')


motor_v6 = Motor('Ford', 300)
motor_v8 = Motor('Ferrari', 800)

carro = Carro()
carro.adicionar_motor(motor_v6)
carro.adicionar_motor(motor_v8)
carro.listar_motores()
