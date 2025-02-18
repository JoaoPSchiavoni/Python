# Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def IntInput(num=0):
    from colorama import Fore, Style
    while True:
        try:
            num = int(input(Fore.GREEN + Style.BRIGHT + 'Digite um numero: '))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Valor digitado Invalido. Tente novamente')
        
    print(Fore.MAGENTA + f'Voce digitou o numero {num}')   
            

