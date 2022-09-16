from distutils import core


class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass


moto = Motocicleta("vermelho", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "EFG-5678", 4)
carro.ligar_motor()

caminhao = Caminhao("azul", "IJK-9012", 8)
caminhao.ligar_motor()