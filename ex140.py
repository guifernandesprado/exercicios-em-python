#Dicionários em Python = aula 90 CeV

alunos = {}

alunos['nome'] = str(input('Nome: '))
alunos['média']= float(input(f'Média de {alunos['nome']}: '))
if alunos['média'] < 5:
    alunos['situação'] = 'Reprovado'
elif alunos['média'] < 7 :
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Aprovado'

for k, v in alunos.items():
    print(f'{k} é igual {v}')