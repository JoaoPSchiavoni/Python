champions_league = ('Liverpool', 'Inter', 'Barcelona', 'Borussia', 'Atalanta', 'Leverkusen', 'Arsenal', 'Monaco', 'Aston Villa', 'Sporting', 'Stade Brestois' , 'LOSC', 'Bayern', 'Benfica', 'Atletico Madrid', 'Milan', 'Man City', 'PSV', 'Juventus', 'Celtic')
print('[A] Mostrar os 5 primeiros colocados da tabela')
print('[B] Mostrar os ultimos 4 colocados da tabela')
print('[C] Lista com os times em ordem alfabetica')
print('[D] Em que posicao esta o Leverkusen ')

user_input = input('Digite a Opcao desejada: ').lower()
while user_input not in ['a', 'b', 'c', 'd']:
    print('Digite uma das opcoes acima')
    user_input = input('Digite a Opcao desejada: ').lower()

if user_input == 'a':
    print('Os 5 primeiros colocados sao: ')
    for club in champions_league[:5]:
        print()
        print(club)
        print()
elif user_input == 'b':
    print('Os ultimos 4 colocados da tabela sao')
    for club in champions_league[-4:]:
        print()
        print(club)
        print()
elif user_input == 'c':
    print('Times em ordem alfabética:')
    for club in sorted(champions_league): 
        print()
        print(club)
        print()
elif user_input == 'd':
    posicao = champions_league.index('Leverkusen') + 1 
    print(f'O Leverkusen está na posição {posicao}')