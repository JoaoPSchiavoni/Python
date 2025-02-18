
#Crie um programa que leia nome, sexo e idade de várias pessoas, 
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
age_count = 0
data = []
colheres = []
average_people = []
def Continue():
    while True:
        answer = input('Voce deseja continuar? [S/N]: ').lower()
        if answer in ['s', 'n']:
            return answer
        else:
            print('Resposta inválida. Digite "S" para sim ou "N" para não.')

def SetPeopleData():
    global age_count
    person = {}
    person['Name'] = input('Digite o Nome: ')
    person['Gender'] = None
    while person['Gender'] not in ['M', 'F']:
        person['Gender'] = input('Qual o sexo [M/F]: ').upper()

    if person['Gender'] == 'F':
        colheres.append(person)

    person['Age'] = int(input('Digite a Idade: '))
    age_count += person["Age"]
    data.append(person)
    print()

while True:
    SetPeopleData()
    if Continue() == 'n':
        break

average = age_count / len(data)
for person in data:
    if person["Age"] > average:
        average_people.append(person)

print(f'{len(data)} Pessoas Foram Cadastradas')
print(f'{age_count}')
print(f'{colheres}')
print(f'a media de idade foi de {average:1f} e as pessoas acima da media foram {average_people}')