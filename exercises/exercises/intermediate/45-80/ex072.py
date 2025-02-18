num = ('Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')


def validacaoerro():
    user_input = -1
    while True:
        user_input = (input('Digite um numero entre 1 e 10: '))
        if user_input.isdigit():
            user_num = int (user_input)
            if 1 <= user_num <= 10:
               return user_num
        print('Número fora do intervalo! Por favor, digite um valor válido.')

valid_num = validacaoerro()
if 1 <= valid_num <= 10:
    print(f'O Valor digitado foi {valid_num} e corresponde a {num[valid_num-1]}')
