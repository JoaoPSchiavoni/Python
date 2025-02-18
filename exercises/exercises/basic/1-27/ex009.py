num = int(input('Digite um numero para saber sua tabuada: '))

print(f'tabuada do {num}')

for i in range(1, 11):
    v = num*i
    print(f'{num} X {i} = {v}')
    