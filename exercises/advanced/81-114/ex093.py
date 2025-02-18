#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida. No final,
#Tudo isso será guardado em um dicionário,
#Incluindo o total de gols feitos durante o campeonato.
    
dados = {}

def set_player_data():
    gols = []
    dados['Nome'] = input('Nome do Jogador: ')
    partidas = int(input('Quantas partidas: '))
    for partida in range(partidas): 
        gols.append(int(input(f'Quantos gols na partida {partida+1}: ')))
    dados['Gols'] = gols
    dados['Total'] = sum(gols)

set_player_data()
print()
for key, item in dados.items():
    print(f'O Campo {key} tem o valor {item}')
print()
print(dados)
print()
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} Partidas')
print()
for partida in range(len(dados['Gols'])):
    print(f'na Partida {partida+1}, fez {dados["Gols"][partida]} Gols')
