woman_less20 = 0
maiority = 0
men = 0
while True:
    try:
        age = int(input('IDADE: '))
    except ValueError:
        print('Por Favor, Insira um valor valido!')
        continue

    sex = input('SEXO [M/F]: ').lower()
    while sex not in ['m', 'f']:
        sex = input('SEXO [M/F]: ').lower()

    if age <= 20 and sex == 'f':
        woman_less20 += 1
    if age >= 18:
        maiority += 1
    if sex == 'm':
        men += 1

    continue1 = input('Deseja continuar? [S/N]: ').lower()
    while continue1 not in ['s', 'n']:
        continue1 = input('Deseja continuar? [S/N]: ').lower()
    if continue1 == 'n':
        break
print(f'Total de pessoas com mais de 18 anos foi de {maiority}')
print(f'Ao todo temos {men} Homens Cadastrados')
print(f'E temos {woman_less20} Mulheres com menos de 20 anos')