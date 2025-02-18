day = int(input('Quantos dias alugado: '))
Km = float(input('Quantos Km rodado: '))
valor = (day * 60) + (Km * 0.15)
print(f'O total a pagar e de {valor:.2f}')