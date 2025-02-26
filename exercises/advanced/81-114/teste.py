nome='teste.txt'
try:
    a=open(nome, 'wt+')
except:
    print('Erro ao abrir o arquivo')
