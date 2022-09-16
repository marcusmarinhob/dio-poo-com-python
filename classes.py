class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valore = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmm...")


b1 = Bicicleta("azul", "caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()