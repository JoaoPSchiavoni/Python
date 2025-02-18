pair = 0
for i in range(0, 6):
    num = int(input(f'Digite o {i}º Numero: '))
    if num % 2 == 0:
        pair += num
print(f'a soma entre os numeros pares {pair}')