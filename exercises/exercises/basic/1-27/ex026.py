x = str(input('Digite uma frase: ')).lower()
print('A letra A apareceu {} vezes'.format(x.count('a')))
print('A primeira letra A apareceu na posicao {}'.format(x.find('a')))
print('A ultima letra A apareceu na posicao {}'.format(x.rfind('a')))