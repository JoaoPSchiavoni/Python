print(''' 
''')
num1 = int(input('Digite o Primeiro Numero: '))
num2 = int(input('Digite o Segundo Numero: '))
print('''
      [1] Somar 
      [2] Mutiplicar
      [3] Maior
      [4] Mudar numero
      [5] Finalizar
      ''')

while True:
    button_option = int(input('Digite uma das opcoes acima : '))
    if button_option == 1:
        result = num1 + num2
        print(f'{num1} + {num2} = {result}')
    elif button_option == 2:
        result = num1 * num2
        print(f'{num1} X {num2} = {result}')
    elif button_option == 3:
        if num1 > num2:
            print(f'O valor {num1} é Maior')
        else:
            print(f'O valor {num2} é Maior')
    elif button_option == 4:
        num1 = int(input('Digite o Primeiro Numero: '))
        num2 = int(input('Digite o Segundo Numero: '))
    elif button_option == 5:
        print(f'Programa finalizado!')
        break
    else:
        print('Opçao invalida! Insira um valor valido.')


