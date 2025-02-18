#faca um programa que leia o nome e a media de um aluno.
#guardando tambem a situacao em um dicionario 
#no final mostre o conteudo da estrutura

dados = {}
def student_situation():
    dados['Nome'] = str(input('Qual o Nome do Aluno: '))
    dados['Media'] = float(input(f'Qual foi a media de {dados["Nome"]}: '))
    if dados['Media'] > 7:
        dados['Situacao'] = 'Aprovado'
    elif dados['Media'] < 7:
        dados['Situacao'] = 'Recuperacao'
    else:
        dados['Situacao'] = 'Reprovado'
student_situation()
for k, i in dados.items():
    print(f'{k} e igual a {i}')



