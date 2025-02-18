#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random  import randint
variavel = 1
lista = [1,2,3,4]
def get_amount():
    while True:
        global amount
        try:
            amount = int(input('QUantos jogos da MEGASENNA?: '))
            break
        except ValueError:
            print('O valor digitado esta ERRADO')
            continue

def random_number():
    global numbers
    numbers = []
    for c in range(amount):
        for num in range(6):
            num=(randint(1,60))
            if num not in numbers:
                numbers.append(num)
                numbers.sort()
        print(numbers)
        numbers.clear()    


get_amount()
random_number()