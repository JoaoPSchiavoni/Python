#Crie um programa onde o usuário possa digitar sete valores numéricos
#e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.


numeros = []

# solicita ao usuario entrada dos numeros
for i in range(7):
    numeros.append(int(input(f'Digite {i+1} numero: ')))
# separacao do numeros em pares e impares
even = [num for num in numeros if num % 2 == 0]
odd = [num for num in numeros if num % 2 != 0]
# ordenacao dos numeros
even.sort()
odd.sort()
# combina todos em uma unica lista
numeros = even + odd
print(numeros)