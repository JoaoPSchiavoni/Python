#  Faça um programa que tenha uma função notas() 
# que pode receber várias notas de alunos e vai retornar um dicionário 
# com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def SchoolGrade(*num, situation = False):

    result = {
    'maior nota' : max(num),
    'menor nota' : min(num),
    'quantidade de notas' : len(num),
    'media da turma' : sum(num) / len(num)
    }


    if situation:
        if result['media da turma'] >=7:
            result['Situacao'] = 'Aprovado'
        elif result['media da turma'] <=5:
            result['Situacao'] = 'Recuperacao'
        else:
            result['Situacao'] = 'Reprovado'
        
    return result

print(SchoolGrade(8.5, 7.3, 6.7, 5.4, 9.1, situation=True))