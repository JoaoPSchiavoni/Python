#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0 for _ in range(3)] for _ in range(3)]


def coleta_dados():    
    for l in range(3):
        for c in range(3):
            while True:
                try:
                    matriz[l][c] =int(input(f'Digite um valor para [{l}, {c}]: '))
                    break
                except ValueError:
                    print('VALOR INVALIDO FAVOR DIGITE NOVAMENTE')
def linhas_colunas():                        
    for l in range (0, 3):
        for c in range(0, 3):
            print(f'[{matriz[l] [c]}] ', end='')
        print()
coleta_dados()
linhas_colunas()

soma= sum(matriz[0]), sum(matriz[1]), sum(matriz[2])
soma = sum(soma)
seg_linha = matriz[1]



print(f'a soma dos valores {soma}')
print(f'a soma  dos  valores do meio {sum(matriz[1])}')
print(max(seg_linha))