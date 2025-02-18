
while True:
    # Error Cheking
    try:
        num = int(input('Digite um numero para saber sua tabuada: '))
    except ValueError:
        print('Por favor, Digite um valor valido!')
        continue
    #
    for i in range(1, 11):
        result = i * num
        print(f'{num} X {i} = {result}')

    continue1 = input('Deseja Continuar? [S/N]: ').lower()
    # Error Cheking
    while continue1 not in ['s', 'n']:
        continue1 = input('Deseja Continuar? [S/N]: ').lower()
    if continue1 == 'n':
        break

print('Finalizado!')