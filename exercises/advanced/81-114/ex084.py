#Faça um programa que leia nome e peso de várias dados, 
#guardando tudo em uma lista. No final, mostre:
#A) Quantas dados foram cadastradas.
#B) Uma listagem com as dados mais pesadas.
#C) Uma listagem com as dados mais leves.





dados = []
maior = menor = 0
def get_people():
    global maior, menor
    while True:
        try:
            nome = (input('Nome: '))
            peso = (int(input('peso: ')))
            dados.append([nome, peso])
            if len(dados) == 1:
                maior = menor = peso
            else:
                if peso > maior:
                    maior = peso
                if peso < menor:
                    menor = peso

        except ValueError:
            print('Valor invalido!')
            continue

        while True:
            resposta = input('Deseja continuar? [S/N]: ').lower()
            if resposta in ['s', 'n']:
                break
            else:
                print('Resposta inválida. Digite "S" para sim ou "N" para não.')             
        if resposta == 'n':
            break
get_people()
print()
print(f'Foram cadastradas {len(dados)} dados')
print(f'O maior peso foi de {maior}, ', end='')  
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}, ', end='' ) 
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')

