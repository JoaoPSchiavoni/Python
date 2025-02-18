valores = []
for n in range(5):
    num = int(input(f'{n} Valor: '))
    if len(valores) == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
print('Valores em ordem crescente:', valores)
