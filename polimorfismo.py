class Ave:
    def voar(self):
        print("Voando...")

class Pardal(Ave):
    def voar(self):
        super().voar()

class Avestruz(Ave):
    def voar(self):
        print("Avestruz não pode voar!")

def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())