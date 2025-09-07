from Casa import Casa
from Carro import Carro
from Pessoa import Pessoa

print('####################')
casa1 = Casa('Azul', 2, 1)
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.mostrar_quartos()
print('####################')
carro1 = Carro('Branco', 2010)
carro1.informacoes()
carro1.ligar()
carro1.desligar()
carro1.ligar()
carro1.ligar_seta('esquerda')
carro1.ligar_seta('direita')
print('####################')
colaborador1 = Pessoa('João', 36, 'Assistente Junior')
colaborador2 = Pessoa('Carlos', 45, 'Dev Junior')

colaborador1.informacoes()
colaborador1.promover('Assitente Pleno')
colaborador1.informacoes()
print('####################')
