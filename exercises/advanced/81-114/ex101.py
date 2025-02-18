# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto 
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def CurrentYear():
    global current_year
    """A funcao Pega o ano atual
    e a data atual 
     da Biblioteca datetime
    """
    from datetime import datetime
    # Obtem Data e Hora Atual
    current_date = datetime.now()
    # Obtem o Ano Atual
    current_year = current_date.year

def vote(year):
    age = current_year - year
    if age < 16:
        return 'Voto NEGADO'
    elif 16 <= age < 18:
        return 'Voto Opcional'
    else:
        return 'Voto OBRIGATORIO'
    
CurrentYear()
result = vote(int(input('Ano de Nascimento: ')))
print(result)
