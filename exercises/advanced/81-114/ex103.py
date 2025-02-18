# Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: o nome de um jogador e 
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a 
# ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

class token:
    """Classe para definir um jogador
    Se caso nome ou total de gols nao for digitado 
    pelo usuario o programa aceitara player como <DESCONHECIDO>
    e total de gols como 0"""
    
    def __init__(self, player = '<DESCONHECIDO>', gols=0):
        self.player = player if player else '<DESCONHECIDO>'
        self.gols = gols if gols else 0

    def SoccerPlayerFile(self):
        return f'O Jogador {self.player} fez {self.gols} na temporada'

#Solicita os dados do jogador ao usuario
player_name = (input('Nome do Jogador: '))
try:
    gols = int(input('Total de Gols na Temporada: '))
except ValueError:
    gols = 0

#Adiciona uma instacia a classe token
token_player = token(player_name, gols)

#imprimindo as iformacoes do jogador
print(token_player.SoccerPlayerFile())