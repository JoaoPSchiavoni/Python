count = 0
list1 = []
while True:
    # Error checking
    try:
        num = int(input('Digite um Numero: '))
    except ValueError:
        print('Por Favor, Digite um Valor valido!')
        continue
    
    list1.append(num)
    count += 1

    continue1 = input('Deseja CONTINUAR? [S/N]: ').lower()

    # Error checking
    while continue1 not in ['s', 'n']:
        continue1 = input('Deseja CONTINUAR? [S/N]: ').lower()
    if continue1 == 'n':
        break

#Calculate the average
media = sum(list1) / count
print(f'A Media entre os Valores Digitados {media:.2f}')
print(f'O Maior Valor Digitado foi {max(list1)}')
print(f'O Menor Valor Digitado foi {min(list1)}')