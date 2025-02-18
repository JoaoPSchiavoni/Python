x = int(input('Digite um numero: '))
print('[1] Para Binario')
print('[2] Para Octal')
print('[3] Para Hexadecimal')
c = int(input('Escolha uma das opcoes: '))

# verifica o valor do "Botao" da variavel C, e mostra para o usuario
if c == 1:
    Bi = bin(x)
    print(f'O valor em Binario {Bi}')
elif c == 2:
    Oc = oct(x)
    print(f'O valor em Octal {Oc}')
elif c == 3:
    He = hex(x)
    print(f'O valor em hexadecimal {He}')
else:
    print('O valor digita esta invalido!')

