count = 0
lista = []
while True:
    
    try:
        num = int(input('Digite um Numero: '))
    except ValueError:
        print('Por Favor, Digite um valor valido!')
        continue
    lista.append(num)

    #Conta quantos numeros foram digitados
    count += 1
    
    continue1 = input('Deseja Continuar? [S/N]: ').lower()
    while continue1 not in ['s', 'n']:
        continue1 = input('Deseja Continuar? [S/N]: ').lower()
    if continue1 == 'n':
        break

print(f'A soma entre os numeros digitados foi {sum(lista)}')
print(f'Voce digitou {count} Numeros')