#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter 
#apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas

numeros = []
def guardar_num():
    while True:
        try:
            print()
            num = int(input(f'valor: '))
            print()
            print(f'Valor {num} foi adicionado a Lista!')
            print()
            return num
        except ValueError:
            print('O valor digitado esta invalido, Favor digitar apenas numeros.')

def continua():
    while True:
        resposta = input('Voce deseja continuar? [S/N]: ').lower()
        if resposta in ['s', 'n']:
            return resposta
        else:
            print('Resposta inválida. Digite "S" para sim ou "N" para não.')
            print()

impares = []
pares = []

while True:
    num = guardar_num()
    numeros.append(num)
    if continua() == 'n':
        print()
        break
    
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

        

print(f'Foram digitados {len(numeros)} numeros')
print()
print(f'{numeros}')
print(f'{impares} numeros impares digitados')
print(f'{pares} numeros pares digitados')