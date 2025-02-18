while True:
    try:
        primeiro = int(input('Digite o termo: '))
    except ValueError:
        print('Por favor, insira um número válido.')
        continue
    while True:
        try:
            razao = int(input('Digite a Razao: '))
            break
        except ValueError:
            print('Por favor, insira um número válido.')

    a = primeiro + (11 - 1) * razao

    
    for i in range(primeiro, a, razao):
        print(f'{i}', end='➡')
    
    print('Fim.')
    continue1 = str(input('Deseja continuar? [S/N] : ')).lower()
    while continue1 not in ['s' , 'n']:
        continue1 = str(input('Deseja continuar? [S/N] : ')).lower()
    if continue1 == 'n':
       break
        
print('Finalizado')