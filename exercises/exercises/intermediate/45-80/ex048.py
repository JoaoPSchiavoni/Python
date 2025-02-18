"""faca um programa que calcula a soma entre 
todos os numeros impares que sao 
multiplos de 3 e que se encontram no intervalo de 1 ate 500."""
add = 0
for num in range(1,501):
    if num % 3 == 0 and num != 0:
        add += num 
print(f"A soma entre todos os números ímpares que são múltiplos de 3 no intervalo de 1 até 500 é: {add}")  