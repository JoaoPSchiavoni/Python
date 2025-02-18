count = 0
soma = 0
print('========================')
while True:
    try:
        n = int(input('Digite um numero: '))
    except ValueError:
        print('Por favor, Digite um Valor valido! ')
        continue

    countnue1 = input('Deseja digitar continuar? [S/N]: ').upper()
    soma += n
    count += 1
    while countnue1 not in['S', 'N']:
        countnue1 = input('Deseja digitar continuar? [S/N]: ').upper()
    if countnue1 == 'N':
        break
print(f'Voce digitou {count} Numeros. A soma entre eles deu {soma}')
