#Crie um programa que leia nome, 
#ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
#além da idade, com quantos anos a pessoa vai se aposentar. depois de 35 anos de contribuicao.

#SONO UNA RAGAZZA

dados = {}

def GetDados():
    this_year = 2024
    global dados
    dados['Nome'] = str(input('Nome: '))
    this_year -= int(input('Ano de nascimento: ')) 
    dados['Idade'] = this_year
    ctps = int(input('CTPS: '))
    if ctps != 0:
        dados['Ctps'] = ctps
        contrib = int(input('ano de contratacao: '))
        dados['Ano de Contratacao'] = contrib
        if contrib - 2024 >= 35:
            dados['Aposentadoria'] = 'Ja Pode se Aponsentar!'
        else:
            contrib = 35 - (contrib - 2024) 
            
            dados['Idade Prevista para a Aposentadoria'] = contrib

GetDados()
print()
for key, item in dados.items():
    print(f'{key} tem o valor {item}')

print()

