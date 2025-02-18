#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e 
#permita que o usuário possa mostrar as notas de cada aluno individualmente.

students_data = []

def get_students():
    global student
    while True:
        student = input('Inserir aluno: ').upper()
        if student.isalpha(): #verifica se possui somente letras
            break
        else:
            print('Valor digitado INVALIDO! ')
def get_grade():
    global math, english
    while True:
        try:
            math = float(input('Nota em matematica: '))
            english = float(input('Nota em English: '))
            break
        except ValueError:
            print('Valor digitado INVALIDO')
def save_date():
    global avarage
    avarage = (math + english) / 2
    students_data.append([student, [math, english],avarage])
def continue_loop():
    while True:
        continuation = input('Deseja continuar? [S/N]: ').upper()
        while continuation not in ['S','N']:
            continuation = input('Deseja continuar? [S/N]: ').upper()

        if continuation == 'S':
            get_students()
            get_grade()
            save_date()
        if continuation == 'N':
            break
def find_student():
    while True:
        find = int(input('''Qual aluno deseja Buscar?: [999 para parar]
            [000 para adicionar mais alunos]: '''))
        if find == 000:
            continue_loop()
        if find == 999:
            print('Finalizando...')
            break
        if find <= len(students_data) - 1:
            print(f'Notas de {students_data[find][0]} sao {students_data[find] [1]}')
continue_loop()

print('--'*10)
print(f' {"No.": <4}{"NOME": <10}{"MEDIA" : >8} ' )
for i, a in enumerate(students_data):
    print(f'{i:<4}{a[0]:<10}{a[2]::>8.1f}')
print('--'*10)

find_student()
