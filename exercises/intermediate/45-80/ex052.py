num = int(input('Digite um número: '))

# Lista de divisores
divisores = []
for c in range(1, num + 1):
    if num % c == 0:
        divisores.append(c)

print(f"Os divisores de {num} são: ", end='')
for divisor in divisores:
    print(f"{divisor} ", end='')
print()  # Para adicionar uma quebra de linha ao final
