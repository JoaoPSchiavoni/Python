km = int(input('Quantos KM ate o destino: '))

if km <= 200:
    x = (km * 0.5) 
    print(f'Valor da passagem R${x:.2f}')
else:
    x = (km * 0.45) 
    print(f'Valor da passagem R${x:.2f}')