from colorama import Fore, Style, init
import os
from time import sleep

#starts colorama
init(autoreset=True)

def display_registered_people(filename):
    '''Function to display registered people'''
    if not os.path.exists(filename):
        print(Fore.RED + 'Nenhuma pessoa cadastrada.')

    else:
        with open(filename, 'r') as file:
            data = file.read()
            if data.strip() == "":
                print(Fore.RED + Style.BRIGHT + 'Nenhuma pessoa cadastrada.')
                print()
            else:
                print(Fore.BLUE + '-' * 30)
                print(Fore.GREEN + Style.BRIGHT + 'Pessoas Cadastradas:')
                print(Fore.BLUE + '-' * 30)
                print(data)
                print(Fore.BLUE + '-' * 30)

def newfile(filename):
    '''Function to create a new file'''
    
    print(Fore.GREEN + f'Arquivo {filename} Funcionando Corretamente.')
    try:
        arq = (filename, 'wt+')
        arq.close()
        #    print(Fore.RED + 'Nenhuma pessoa cadastrada.')
    except Exception as error:
        print(Fore.RED + f'Erro ao criar arquivo. : {error}')

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



'''Function that registers a person'''
'''Criar uma classe pessoa com nome, idade,sexo,peso e cadastrar no arquivo'''


def register(filename, name='Desconhecido', idade=0):
    try:
        arq = open(filename, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            arq.write(f'{name}; {idade}', 'at')
        except:
            print('Houve um erro ao tentar escrever os dados')
        else:
            print(f'Novo registro de {name} adicionado')
            arq.close()
    

def Remove_person():
    '''Function that removes a person'''
    '''Remover uma pessoa do arquivo'''
    pass

def HeaderMenu(text):
        ClearScreen()
        print('-_' * 20)
        print(Fore.YELLOW + Style.BRIGHT + text.center(20))
        print('-_' * 20)
        print()
        sleep(1)