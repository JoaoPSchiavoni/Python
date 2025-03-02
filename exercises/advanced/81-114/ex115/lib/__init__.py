from colorama import Fore, Style, init
import os
from time import sleep

init(autoreset=True)

def display_registered_people(filename):
    try:
        with open(filename, 'rt') as a:
            line_design('Pessoas Cadastradas:')
            for line in a:
                data = line.split(';')
                data[1] = data[1].replace('\n', '')
                print(Fore.YELLOW + f'Nome:{data[0]:<17}{data[1]:>3} anos')
                print(Fore.BLUE + '-' * 30)
    except:
        print(Fore.RED + 'erro ao ler arquivo')

def line_design(txt):
    '''Function that displays a line design'''
    print(Fore.BLUE + '-' * 30)
    print(Fore.GREEN + Style.BRIGHT + 'Pessoas Cadastradas:')
    print(Fore.BLUE + '-' * 30)

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
    '''Screen clearing function'''   
    os.system('cls' if os.name == 'nt' else 'clear')

def Show_optionMenu():
    '''Function that displays a menu of options'''

    init(autoreset=True)
    print(Fore.BLUE + Style.BRIGHT + '-' * 30)
    print((Fore.MAGENTA + Style.BRIGHT + 'MENU PRINCIPAL').center(40))
    print(Fore.BLUE + Style.BRIGHT + '-' * 30)
    print(Fore.GREEN + Style.BRIGHT + '1 - Ver pessoas Cadastradas')
    print(Fore.GREEN + Style.BRIGHT + '2 - Cadastrar nova Pessoa')
    print(Fore.GREEN + Style.BRIGHT + '3 - Remover Pessoa')
    print(Fore.GREEN + Style.BRIGHT + '4 - Sair do Sistema')
    print(Fore.BLUE + Style.BRIGHT + '-' * 30)

def Menu():
    from time import sleep
    '''Function that displays a menu of options'''

    while True:
        
        welcome_mensage()
        Show_optionMenu()

        print()
        option = IntInput(Fore.BLUE + Style.BRIGHT + 'Digite uma opcao: ')
        if option == 3:
            print(Fore.RED  + Style.BRIGHT + 'Saindo do Sistema...')
            sleep(2)
            print()
            print(Fore.WHITE + Style.BRIGHT + 'Sistema Encerrado') 
            break
        elif option == 2:
            print(Fore.RED + Style.BRIGHT + 'Cadastrando nova pessoa...')
            sleep(3)
        elif option == 1:
            print(Fore.RED + Style.BRIGHT + 'Pessoas Cadastradas...')
            sleep(3)
            display_registered_people('people.txt')

def welcome_mensage():
    '''Function that displays a welcome message'''
    print(Fore.BLUE + Style.BRIGHT + '-' * 30)
    print((Fore.CYAN + Style.BRIGHT + 'Bem-vindo ao Sistema de Gerenciamento').center(40))

def newfile(filename):
    '''Function to create a new file'''
    try:
        with open(filename, 'a+') as arq:
            print(Fore.GREEN + f'Arquivo {filename} Funcionando Corretamente.')

    except Exception as error:
        print(Fore.RED + f'Erro ao criar arquivo. : {error}')

def register(filename, name='Desconhecido', idade=0):
    '''Function to register a new person'''
    try:
        with open(filename, 'a') as arq:
            arq.write(f'{name};{idade}\n')
            print(f'Novo registro de {name} adicionado')
    except Exception as error:
        print(f'Houve um erro ao tentar escrever os dados: {error}')


def HeaderMenu(text):
        '''Function that displays a header menu'''
        ClearScreen()
        print('-_' * 20)
        print(Fore.YELLOW + Style.BRIGHT + text.center(20))
        print('-_' * 20)
        print()
        sleep(1)