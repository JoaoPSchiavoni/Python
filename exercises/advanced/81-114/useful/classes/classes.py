import math

class SoccerPlayer:
    name = ''
    goals = 0
    matches = 0
    def __init__(self, name, goals, matches):
        self.name = name
        self.goals = goals
        self.matches = matches
        self.total_goals = sum(goals)
        self.average_goals = self.total_goals / matches
        print(f'{name} fez {self.total_goals} gols em {matches} partidas, com uma media de {self.average_goals:.2f} gols por partida')
    

class Carro:
    def __init__(self, marca, potencia, modelo):
        self.marca = marca
        self.potencia = potencia
        self.modelo = modelo
    
    def ligar(self):
        return f'Ligando {self.marca} {self.modelo}'
    def desligar(self):
        return f'Desligando {self.marca} {self.modelo}'

carro1 = Carro('PORSCHE', '400cv', '911')

class Character:
    def __init__(self, healf, damage, speed):
        self.healf = healf
        self.damage = damage
        self.speed = speed

    def incress_speed(self):
        self.speed *= 2

mage = Character(60, 90, 20)
warrior = Character(120, 50, 20)
ninja = Character(80, 40, 40)


class Dice:
    name = ""
    sum_result = 0
    values = []
    def __init__(self, name):
        self.name = name
        self.values = [randint(1, 6) for _  in range(3)]
        self.sum_result = sum(self.values)
        print("Dice created successfully: " + self.name)
 
    def to_string(self):
        return "Name: " + self.name + "\n"+ "Sum: " + str(self.sum_result) +"\n"+  "Values: " + str(self.values) + "\n\n"

#diceList = []
#for i in range(3):
#    diceList.append(Dice(input(f'Qual o nome do {i+1}º Player: ')))
#diceList.append(Dice("Computer"))
#reordedList = sorted(diceList, key=lambda dice: dice.sum_result, reverse=True)
#for dice in reordedList:
#    print(dice.to_string())

porshe = Carro('Porshe', '400cv', '911')
Carro.ligar(porshe)