print('==============Sequencia Fibonacci==============')

while True:
    try:
        n = int(input('Digite a quantidade desejada de termos: '))
    except ValueError:
        print('Por favor, Digite um valor valido!')
        continue
   
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    
    print()

    continue1 = input('Deseja continuar? [S/N] : ').lower()
    while continue1 not in ['s', 'n']:
        continue1 = input('Deseja continuar? [S/N] : ').lower()
    if continue1 == 'n':
        break

print('Finalizado')