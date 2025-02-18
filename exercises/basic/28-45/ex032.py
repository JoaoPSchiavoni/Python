ano = int(input('Digite um ano para saber se ele e bissexto: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")

else:
    print(f"{ano} nao é um ano bissexto.")