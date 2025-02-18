def InteractiveHelp(text):
        help(text)

while True:
    msg = str(input('Digite o comando ou biblioteca que deseja ajuda: '))
    continue1 = input('Deseja sair? [S/N] ').upper()
    if continue1 == 'S':
        break
    else:
         InteractiveHelp(msg)
    print('Fim do Programa')