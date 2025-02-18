x = int(input('Digite um Numero: '))
y = int(input('Digite outro Numero: '))

#Verificacao de qual valor é maior
if x > y:
    print(f'O Primeiro valor {x} é Maior')
elif y > x:
    print(f'O Segundo valor {y} é Maior')
else:
    print(f'Os valores sao iguais')