n = str(input('Digite nome completo: ')).capitalize().strip()
name = n.split()
print('O primeiro nome: {}'.format(name[0]))
print('O ultimo nome: {}'.format(name[len(name)-1]))