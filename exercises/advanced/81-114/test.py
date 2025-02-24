class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def ligar(self):
        print( f'Ligando {self.marca} {self.modelo}')
    def desligar(self):
        print( f'Desligando {self.marca} {self.modelo}')

marca = 'porshe'
modelo = '911'

porshe = Carro(marca, modelo)

Carro.ligar(porshe)

Carro.desligar(porshe)