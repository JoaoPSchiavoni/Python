numeros = []

# Pede 3 valores ao Usuario e Armazena
for i in range (1, 4):
    x = int(input(f'Digite {i}º numero: '))
    numeros.append(x)

# Organiza a lista do Maior para o Menor
numeros.sort()

print(f'O Menor Numero Digitado foi {numeros[0]}')
print(f'O Maior Numero Digitado foi {numeros[2]}')