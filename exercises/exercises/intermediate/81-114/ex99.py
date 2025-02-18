# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def bigger(*num):
    print(num)
    print(f'Foram informados {len(num)} o Maior numero foi {max(num)}')
    print('+-'*15)
bigger(9, 2 , 10, 5, 0, 2, 19)

