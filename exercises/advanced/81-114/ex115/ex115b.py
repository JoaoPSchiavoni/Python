import lib
from colorama import Fore, Style
from time import sleep

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
        print('-_' * 20)
        print(Fore.RED  + Style.BRIGHT + 'Saindo do Sistema...' .center(20))
        print('-_' * 20)
        sleep(2)
        print()
        print(Fore.WHITE + Style.BRIGHT + 'Sistema Encerrado') 
        break

    elif option == 3:
        lib.ClearScreen()
        print('-_' * 20)
        print(Fore.RED + Style.BRIGHT + 'Remover pessoa...'.center(20))
        print('-_' * 20)
        print()
        sleep(2)

    elif option == 2:
        lib.ClearScreen()
        print('-_' * 20)
        print(Fore.YELLOW + Style.BRIGHT + 'Cadastrando nova pessoa...'.center(20))
        print('-_' * 20)
        print()
        sleep(0)
        name = input('Nome: ')
        age = input('Idade: ')
        gender = input('Sexo: ')
        heigh = input('Altura: ')
        person = {name, age, gender, heigh}

        for i in person:


            file = open('people.txt', 'a')
            file.writelines(person)

    elif option == 1:
        lib.ClearScreen()
        print('-_' * 20)
        print((Fore.YELLOW + Style.BRIGHT + 'Acessando pessoas Cadastradas...').center(40))
        print('-_' * 20)
        print()
        sleep(2)
        lib.display_registered_people('people.txt')

