# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.


def area():
    width = float(input('Largura em  Metros:  '))
    length = float(input('Comprimento em metros:  '))
    total_area = width * length
    print(f'A area Total do terreno {total_area:2f}')

area()