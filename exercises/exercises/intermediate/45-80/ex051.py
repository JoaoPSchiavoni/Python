#A = a1 + (n -1) * r

primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a Razao: '))
a = primeiro + (11 - 1) * razao
for i in range(primeiro, a, razao):
    print(f'{i}', end='➡')
print('ACABOU')