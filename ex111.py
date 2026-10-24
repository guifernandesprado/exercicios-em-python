# exercício CeV 69

tot18 = 0
mascu = 0
femin = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]')).upper().strip()[0]
    while sexo not in 'FfMm':
        sexo = str(input('Opção inválida. tente outra vez: [M/F] '))
    if idade >= 18:
        tot18 += 1
    if sexo in 'Mm':
        mascu += 1
    if sexo in 'Ff' and idade < 20:
        femin += 1
    print('')
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Opção inválida. Tente outra vez: [S/N] '))
    print('-=' * 30)
    if resposta in 'Nn':
        break

print(f'Total de pessoas cadastradas com mais de 18 anos: {tot18}')
print(f'Ao todo, temos {mascu} homem cadastrados.')
print(f'E temos {femin} mulher com menos de 20 anos.')
