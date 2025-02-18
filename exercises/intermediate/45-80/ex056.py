soma = 0
woman_less20 = 0
older_men = 0
oldest_man_name = ''
for person in range (5):
    name = input(f'Qual o nome da {person+1}ª pessoa : ')
    age = int(input(f'Qual a idade de {name} : '))
    gender = input(f'Qual o Sexo de {name} M/F : ').upper()
    soma += age
    
    if gender == 'M':
        if age > older_men:
            older_men = age
            oldest_man_name = name
    if gender == 'F':
        if age <= 20:
            woman_less20 += 1
print(f'A media de idade do Grupo e {soma/4}')
print(f'O homem mais velho e {oldest_man_name} com {older_men}')
print(f'atualmente tem {woman_less20} mulheres com menos de 20 anos')
        

