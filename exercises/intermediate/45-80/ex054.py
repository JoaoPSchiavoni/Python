menor = 0
maior = 0
for person in range(7):
    idade = int(input(f'quantos anos a {person+1} tem:'))
    if idade <= 17:
        menor += 1
    else:
        maior += 1
print(f'{menor} sao menores de idade')
print(f'{maior} sao maiores de idade')