salario = float(input('Digite o Salario: '))

if salario <= 1250.00:
    aumento = salario * 0.10
    print('O aumento sera de R${:.2f} totalizando R${:.2f}'.format(aumento, aumento + salario))
else:
    aumento = salario * 0.15
    print('O aumento sera de R${:.2f} totalizando R${:.2f}'.format(aumento, aumento + salario))