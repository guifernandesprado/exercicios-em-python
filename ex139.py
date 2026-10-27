alunos = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resposta = ' '
    while resposta not in ['S','N']:
        resposta = input('Quer continuar? [S/N] ').upper().strip()
    if resposta == 'N':
        break
print('Nº  NOME           MÉDIA')
for i, aluno in enumerate(alunos):
    print(f'{i+1}   {aluno[0]:<10}   {aluno[2]:>5.1f}')
while True:
    opcao = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opcao == 999:
        break
    if 1 <= opcao <= len(alunos):
        print(f'As notas de {alunos[opcao - 1][0]} são: {alunos[opcao - 1][1]}')
    else:
        print('Aluno não encontrado.')


