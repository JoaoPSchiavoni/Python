#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
#sabendo que o vencedor tirou o maior número no dado

from random import randint

players = {}
def computer_dice():
    global players
    computer_dice_value = [randint(1, 6) for _ in range(3)]
    dice_sum = sum(computer_dice_value)
    players['Computer'] = {'Name': 'Machine', 'Dice': computer_dice_value, 'SumDices': dice_sum}

def players_dice_values_and_name():
    global players
    for i in range(3):
        player_name = input(f'Qual o nome do {i+1}º Player: ') 
        dice_value = [randint(1, 6) for _ in range(3)]
        dice_sum = sum(dice_value)
        players[i] = {'Name': player_name, 'Dice': dice_value, 'SumDices': dice_sum}  

computer_dice() 
players_dice_values_and_name()


organized_players = sorted(players.items(), key=lambda x: x[1]['SumDices'], reverse=True)

for key, value in organized_players:
    print(f'{value["Name"]} tem a soma dos dados igual a {value["SumDices"]}')
    



