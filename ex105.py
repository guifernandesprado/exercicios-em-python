print('     NOTAS DA ESCOLA')
print('')

total = cont =maior = menor = media = 0
nome_maior = nome_menor = ''

resposta = 'S'

while resposta in 'Ss':
    nome = str(input('Nome: '))
    nota = float(input('Nota: '))
    cont += 1
    total += nota

    if cont == 1:
        maior = menor = nota
        nome_maior = nome_menor = nome
    else:
        if nota > maior:
            maior = nota
            nome_maior = nome
        if nota < menor:
            menor = nota
            nome_menor = nome
    resposta = str(input('Quer continuar? [S/N]: '))
media = total/cont

print(f'A média das notas da turma foi de {media}.')
print(f'Ao todo, {cont} alunos fizeram a prova.')
print(f'O aluno com a maior nota foi {nome_maior} com a nota {maior}.')
print(f'Já o aluno com a menor nota foi {nome_menor}, com a nota {menor}.')
