import random
lista = []
for i in range(1, 6):
    aluno = input('Nome do Aluno: ')
    lista.append(aluno)
random.shuffle(lista)
print(lista[0])
