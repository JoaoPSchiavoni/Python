#Crie um programa onde o usuário possa digitar vários valores numéricos e 
#cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final,
#serão exibidos todos os valores únicos digitados, em ordem crescente

num = []
while True:
    try:
        number=int(input('Valor: '))
        continue1 = input('Deseja continuar?[S/N]: ').upper()
        while continue1 not in ['S', 'N']:
            continue1 = input('Deseja continuar?[S/N]: ').upper()
        if number not in num:
            num.append(number)
        if continue1 == 'N':
            break
    except ValueError:
        print('valor invalido favor digitar apenas numeros')
num.sort()
print(num)
