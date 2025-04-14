from colorama import Fore, Style
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def ligar(self):
        print(Fore.YELLOW + Style.BRIGHT + f'Ligando {self.marca} {self.modelo}')
    def desligar(self):
        print(Fore.YELLOW + Style.BRIGHT + f'Desligando {self.marca} {self.modelo}')

marca = 'Porshe'
modelo = '911'

porshe = Carro(marca, modelo)

Carro.ligar(porshe)
from time import sleep
for i in range(5):
    print(Fore.RED + 'VRRROOOOMMMM')
    sleep(1)
sleep(2)
Carro.desligar(porshe)