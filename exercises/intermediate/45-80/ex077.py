
def extrair_vogais(text):
    vogais = 'aeiouAEIOU'
    return ''.join([letra for letra in text if letra in vogais])

tupla_palavras = ('Apple', 'Joao', 'Marcela', "Escola", 'Fernando', 'League')

tupla_vogais = tuple(extrair_vogais(palavra) for palavra in tupla_palavras)

for palavra, vogais in zip(tupla_palavras, tupla_vogais):
    print(f'Palavra: {palavra}')
    print(f'Vogais: {vogais}')
    print('------')

