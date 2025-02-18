x = float(input('Digite o primeiro numero: '))
y = float(input('Digite o segundo numero: '))
z = float(input('Digite o terceiro numero: '))

# Verificacao para saber se os valores formam um triangulo
if x + y > z and x + z > y and y + z > x:
    print('esses valores formam um triangulo! ')
else:
    print('esses valores nao formam um triangulo!')