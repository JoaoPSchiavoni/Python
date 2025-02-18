def increase(amount=0, tax=0, format=False):
    '''Increase the value of the amount by the tax percentage
    :param amount: The amount that will be increased
    :param tax: The percentage of the increase
    :param format: If True, the result will be formatted as currency'''
    amount = amount + (amount * tax / 100)
    return amount if format is False else currency(amount)


def decrease(amount=0, tax=0, format=False):
    '''Decrease the value of the amount by the tax percentage
    :param amount: The amount that will be decreased
    :param tax: The percentage of the decrease
    :param format: If True, the result will be formatted as currency'''
    amount = amount - (amount * tax / 100)
    return amount if format is False else currency(amount)

def double(amount=0, format=False):
    '''Double the value of the amount
    :param amount: The amount that will be doubled
    :param format: If True, the result will be formatted as currency'''
    amount *= 2
    return amount if format is False else currency(amount)

def half(amount=0, format=False):
    '''Half the value of the amount
    :param amount: The amount that will be halved
    :param format: If True, the result will be formatted as currency'''
    tot = amount / 2
    return amount if not format else currency(tot)

def currency(amount=0, currency='R$ '):
    '''Return the amount formatted as currency
    :param amount: The amount that will be formatted
    :param currency: The currency that will be used'''
    return f'{currency}{amount:.2f}'.replace('.', ',')

 
def resume(amount=0, tax_increase=0, tax_decrease=0):
    '''Print a resume of the value
    :param amount: The amount that will be analyzed
    :param tax_increase: The percentage of the increase
    :param tax_decrease: The percentage of the decrease'''
    print('-' * 30)
    print('RESUME OF THE VALUE'.center(30))
    print('-' * 30)
    print(f'Entered value: \t{currency(amount)}')
    print(f'Double the value: \t{double(amount, True)}')
    print(f'Half the value: \t{half(amount, True)}')
    print(f'Increase {tax_increase}%: \t{increase(amount, tax_increase, True)}')
    print(f'Decrease {tax_decrease}%: \t{decrease(amount, tax_decrease, True)}')
    print('-' * 30)

def input_price(prompt):
    '''Read a float price from the user
    :param prompt: The message that will be shown to the user'''

    # Read the price from the user
    price = input(prompt).replace(',', '.')

    # Check if the price is a valid float number
    try:

        float_price = float(price)
        return float_price
    
    except ValueError:
        print("Erro: a string não pode ser convertida para um número float")
        return None
    
def main():
    '''Main function of the module'''

    # Read the price from the user
    float_price = input_price('Enter the price: $ ')

    # If the price is valid, show the resume
    if float_price is None:
        resume(float_price, 10, 5)
    else:    
        resume(float_price, 10, 5)

def floatInput(num):
    '''Function to get a float input from user
    :param num: float: number to be inputed'''
    
    from colorama import Fore, Style
    while True:
        try:
            num = float(input(Fore.GREEN + Style.BRIGHT + 'Digite um numero: '))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + 'Valor digitado Invalido. Tente novamente')
        
    print(Fore.MAGENTA + f'Voce digitou o numero {num}')