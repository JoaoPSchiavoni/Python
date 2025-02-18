menor = None
maior = 0
for weigh in range(5):
    weitgh = float(input(f'Digite o peso {weigh+1} : '))
    if maior == 0 or weitgh > maior:
        maior = weitgh
    if menor is None or weitgh < menor:
        menor = weitgh
    
print(f'{maior:.2f} este foi o maior peso escrito')
print(f'{menor:.2f} este foi o menor peso escrito')