#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: 
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~



def write(txt):
    print('-'*len(txt+4))
    print(f'  {txt}')
    print('-'*len(txt+4))

msg = str(input('Digite o texto: '))
write(msg)