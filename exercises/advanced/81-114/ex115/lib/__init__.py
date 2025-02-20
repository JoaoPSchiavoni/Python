from colorama import Fore, Style, init
import os
from time import sleep

def IntInput(prompt):
    '''Function to get an integer input from user
    :param prompt: int: number to be inputed''' 
    try:
        num = int(input(prompt))
        return num
    except ValueError:
        print(Fore.RED + Style.BRIGHT + 'Valor digitado Invalido. Tente novamente')
        sleep(2)

def ClearScreen():
    '''Funcao que Limpa a tela'''
    os.system('cls' if os.name == 'nt' else 'clear')

def Show_optionMenu():
    '''Funcao que exibe um menu de opcoes'''

    init(autoreset=True)
    print(Fore.BLUE + Style.BRIGHT + '-' * 30)
    print((Fore.MAGENTA + Style.BRIGHT + 'MENU PRINCIPAL').center(40))
    print(Fore.BLUE + Style.BRIGHT + '-' * 30)
    print(Fore.GREEN + Style.BRIGHT + '1 - Ver pessoas Cadastradas')
    print(Fore.GREEN + Style.BRIGHT + '2 - Cadastrar nova Pessoa')
    print(Fore.GREEN + Style.BRIGHT + '3 - Sair do Sistema')
    print(Fore.BLUE + Style.BRIGHT + '-' * 30)

def Menu():
    from time import sleep
    '''Funcao que exibe um menu de opcoes'''
    while True:
        ClearScreen()
        welcome_mensage()
        Show_optionMenu()
        print()
        option = IntInput(Fore.BLUE + Style.BRIGHT + 'Digite uma opcao: ')
        if option == 3:
            print(Fore.RED + Style.BRIGHT + 'Saindo do Sistema...')
            sleep(2)
            print(Fore.WHITE + Style.BRIGHT + 'Sistema Encerrado') 
            break       
        elif option == 2:
            print(Fore.RED + Style.BRIGHT + 'Cadastrando nova pessoa...')
            sleep(3)
        elif option == 1:
            print(Fore.RED + Style.BRIGHT + 'Pessoas Cadastradas...')
            sleep(3)

def welcome_mensage():
    print((Fore.RED + Style.BRIGHT + 'Bem-vindo ao Sistema de Gerenciamento').center(40))