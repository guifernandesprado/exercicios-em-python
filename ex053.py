total = 0

notas = int(input('Quantas notas vai digitar: '))

for c in range(notas):
    nota = float(input(f'Digite a {c+1}° nota: '))
    total += nota

media = total / notas

if media >= 6:
    print(f'Média de {media}. Aluno APROVADO!')
else:
    print(f'Média de {media}. Aluno REPROVADO!')
    