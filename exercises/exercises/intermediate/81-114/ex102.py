# Crie um programa que tenha uma função fatorial() 
# que receba dois parâmetros: o primeiro que indique o número a calcular e 
# outro chamado show, que será um valor lógico (opcional) indicando se será 
# mostrado ou não na tela o processo de cálculo do fatorial.

def factorial(num, show=False):
    from math import factorial
    result = 1

    for i in range(1, num + 1):
        result *= i
        if show:
            if i == num:
                print(f'{i} * ', end='')
            else:
                print(f'{i} * ', end='')


    print(result)
    return result

factorial(5, show=True)
