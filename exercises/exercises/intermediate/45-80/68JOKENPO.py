from colorama import Style, Fore, Back, init
from random import choice
import time



init(autoreset=True)
jokenpo = ('Pedra', 'Papel', 'Tesoura')
#jokenpo = [1, 2, 3]
while True:
    undefeated = 0
    while True:    
        print()
        print(Fore.RED + Style.BRIGHT + '+-+-+-+-+JOKENPO+-+-+-+-+')
        print(Fore.GREEN + Style.BRIGHT + '''        PEDRA    [1]
        PAPEL    [2]
        TESOURA  [3]''')
        print(Fore.RED + Style.BRIGHT + '+-+-+-+-+JOKENPO+-+-+-+-+')
        print()

        # Error Checking
        try:
            player_choice = int(input(Fore.YELLOW + Style.BRIGHT + 'Qual Sua Escolha: '))
            if player_choice not in [1, 2, 3]: 
                raise ValueError
        except ValueError:
            print(Fore.RED + Style.BRIGHT + Back.YELLOW +'OPCAO INVALIDA!'+ Back.RESET)
            continue

        computer_choice = choice(jokenpo)
        player_choice_iten = jokenpo[player_choice-1]

        print()
        print(Fore.MAGENTA + Style.BRIGHT+'READY')
        print()
        
        for c in range(3, -1, -1):
            if c != 0:
                print(c)
            tempo = time.sleep(1)
        
        print()
        print(Fore.LIGHTCYAN_EX+ Style.BRIGHT+computer_choice) 
        print()
        
        if player_choice_iten == computer_choice:
            print(Fore.BLUE + Back.WHITE + Style.BRIGHT+'Empate!')
        
        elif player_choice_iten == 1 and computer_choice == 'Tesoura' or \
        player_choice_iten == 2 and computer_choice == 'Pedra' or \
        player_choice_iten == 3 and computer_choice == 'Papel':
            print(Fore.BLACK + Style.BRIGHT + Back.GREEN +f'VOCE GANHOU'+ Back.RESET)
            undefeated += 1

        else:
            if     undefeated <= 1:
                print(Fore.WHITE + Style.BRIGHT+ Back.RED+ f'VOCE É FRACO'+Back.RESET)
            print(Fore.WHITE + Style.BRIGHT+ Back.RED+ f'VOCE PERDEU! Voce ganhou {undefeated} vezes'+Back.RESET)
            break
    
    print() 
        #Continuar
    continue1 = input(Fore.LIGHTRED_EX + Style.BRIGHT+ Back.LIGHTWHITE_EX+ 'DENOVO? [S/N] : '+Back.RESET).lower()
        
    while continue1 not in ['s', 'n']:
        continue1 = input(Fore.LIGHTRED_EX + Style.BRIGHT+ Back.LIGHTWHITE_EX+ 'DENOVO? [S/N] : '+Back.RESET).lower()
    if continue1 == 'n':
        print()
        break
print(Fore.BLACK+ Back.WHITE+ Style.BRIGHT+ 'FINALIZADO'+Back.RESET)


            