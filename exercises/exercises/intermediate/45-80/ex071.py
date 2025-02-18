# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor_sacado a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor_sacado serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
def withdraw_money (withdrawal_value):
    banknotes = [50, 20, 10, 1]
    amount_banknote = {}
    
    for banknote in banknotes:
        amount = withdrawal_value // banknote
        withdrawal_value %= banknote
        amount_banknote[banknote] = amount

    return  amount_banknote

def request_value():
    while True: 
        try:
            withdrawal_value = int(input('Qual o valor a ser sacado: '))
            if withdrawal_value <= 0:
                print('Por Favor, Digite um valor valido!')
                continue
            return withdrawal_value
        except ValueError:
            print('Por Favor, Digite um valor valido!')

request_withdraw_money = request_value()

# Calcula a quantidade de cedulas de cada valor
result = withdraw_money(request_withdraw_money)


for banknote, amount in result.items():
    if amount > 0:
        print(f'Cédulas de R${banknote}: {amount}')

    