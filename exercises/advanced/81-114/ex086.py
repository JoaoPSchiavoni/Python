#Crie um programa que declare uma matriz de dimensão 3x3
#e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]

def coleta_dados():
    global matriz
    for l in range(0, 3):
        for c in range(0, 3):
            matriz[l][c] =int(input(f'Digite um valor para [{l}, {c}]: '))

def linhas_colunas():                        
    for l in range (0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l] [c]}] ', end='')
        print()

linhas_colunas()
