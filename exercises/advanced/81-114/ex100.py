# Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a 
# soma entre todos os valores pares sorteados pela função anterior.

num_list = []

def raffle():
    from random import randint
    for c in range(5):
        while True:
            num = (randint(1, 10))
            if num not in num_list:
                num_list.append(num)
                break
    print(num_list)

def SumEven():
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    print(even_list)
    print(sum(even_list))

raffle()
SumEven()
