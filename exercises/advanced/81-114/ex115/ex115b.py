import lib
from colorama import Fore, Style


filename = 'people.txt'
lib.newfile(filename)


'''displays a menu of options'''

while True:
    
    lib.welcome_mensage()
    lib.Show_optionMenu()

    print()
    option = lib.IntInput(Fore.BLUE + Style.BRIGHT + 'Digite uma opcao: ')
    print()

    if option == 4:
        lib.HeaderMenu('Saindo do Sistema...')
        print(Fore.WHITE + Style.BRIGHT + 'Sistema Encerrado') 
        break

    elif option == 3:
        lib.HeaderMenu('Removendo pessoa...')

    elif option == 2:
        lib.HeaderMenu('Cadastrando nova pessoa...')
        name = input('Nome: ')
        age = lib.IntInput('Idade: ')
        lib.register(filename, name, age)

    elif option == 1:
        lib.HeaderMenu('Acessando pessoas Cadastradas...')
        lib.display_registered_people1('people.txt')

    else:
        print('Opcao invalida, tente novamente')