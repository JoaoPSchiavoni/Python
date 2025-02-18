#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

def continue1():
    while True:
        resposta = input('Voce deseja continuar? [S/N]: ').lower()
        if resposta in ['s', 'n']:
            return resposta
        else:
            print('Resposta inválida. Digite "S" para sim ou "N" para não.')

def guardar_num():
    while True:
        try:
            num = int(input('Digite um valor: '))
            print(f'Valor {num} foi adicionado a Lista!')
            return num
        except ValueError:
            print('Valor digitado inválido! Favor digitar apenas números.')
            

lista = []
num_5 = 5
while True:
    num = guardar_num()
    lista.append(num)
    if continue1() == 'n':
        break

lista.sort(reverse=True)

print(f'Foram digitados {len(lista)} numeros')
print(f'A lista em ordem ordenanda {lista}')
if num_5 in lista:
    print(f'O número {num_5} está na lista.')

else:
    print(f'O número {num_5} não está na lista.')

            
