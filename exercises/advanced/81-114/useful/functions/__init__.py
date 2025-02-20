from colorama import Fore, Style, init
from time import sleep
def IntInput(prompt):
    '''Function to get an integer input from user
    :param prompt: int: number to be inputed'''
    

    try:
        num = int(input(prompt))
        return num

    except ValueError:
        print(Fore.RED + Style.BRIGHT + 'Valor digitado Invalido. Tente novamente')
           


def raffle():
    '''A Funcao randomiza 5 numeros
    de 1 a 10'''
    num_list = []
    from random import randint
    for c in range(5):
        while True:
            num = (randint(1, 10))
            if num not in num_list:
                num_list.append(num)
                break
    print(num_list)


def CurrentYear():
    """A funcao Pega o ano atual
    e a data atual 
     da Biblioteca datetime
    """
    from datetime import datetime
    # Obtem Data e Hora Atual
    current_date = datetime.now()
    # Obtem o Ano Atual
    current_year = current_date.year


def floatInput(prompt):
    '''Function to get a float input from user
    :param prompt: float: number to be inputed'''

    num = float(input(prompt))

    try:
        float_num = float(num)
        return float_num

    except ValueError:
        print(Fore.RED + Style.BRIGHT + 'Valor digitado Invalido. Tente novamente')
        

def main_ex113():
    '''Main function of the module'''

    int_num = IntInput(Fore.GREEN + Style.BRIGHT + 'Digite um numero:')
    float_num = floatInput(Fore.GREEN + Style.BRIGHT + 'Digite um numero Real: ')

    print(Fore.BLUE + Style.BRIGHT + f'Número inteiro digitado: {int_num}')
    print(Fore.BLUE + Style.BRIGHT + f'Número real digitado: {float_num}')



