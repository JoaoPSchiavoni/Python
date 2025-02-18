#Crie um programa onde o usuário digite uma expressão qualquer
#que use parênteses. Seu aplicativo deverá analisar se a expressão
#passada está com os parênteses abertos
#e fechados na ordem correta.

expressao = input('Digite sua expressao: ')
abertura = expressao.count('(')
fechamento = expressao.count(')')

soma = abertura+fechamento

if soma % 2 == 0:
    print(f'Sua expressao esta correta')
else:
    print(f'Sua expressao esta invalida!')
