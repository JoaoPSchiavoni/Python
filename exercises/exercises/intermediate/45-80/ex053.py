print('Palindromos sao frases ou palavras que lidas de tras para a frente permanece igual ')
palindromo = str(input(' Digite uma frase para saber se ela e um palindromo: ')).upper()
text_no_space = palindromo.replace(" ", "").replace("\t", "")
invert_text = text_no_space[::-1]
if invert_text == text_no_space:
    print(f'{palindromo} e um palindromo')
else:
    print(f'{palindromo} nao e um palindromo')
