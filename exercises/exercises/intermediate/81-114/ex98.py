#Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, 
# fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def count(beginning, end, step):
    if step > 0:
        end += 1
    else:
        end -= 1

    for value in range (beginning, end, step):
        print(value,' ', end=' ➡️ ')
    
    print('Fim')
    print('=-'*10)

count(1, 10, 1)
count(10, -1, -2)
b = int(input('Digite onde comeca: '))
e = int(input('Digite onde Termina: '))
s = int(input('Digite Pulando de quanto em quanto: '))
count(b, e, s)