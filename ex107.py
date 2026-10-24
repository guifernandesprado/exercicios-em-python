print('')
print('Sistema de análise de voo e passageiros')
print('')

total = total_idade = peso_maior = mulher25 = bagagem23 = 0 
nome_bagagem = ''

resposta = 'S'

while resposta in 'Ss':
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MmFf':
            sexo = str(input('Opção inválida. Tente novamente: [M/F] ')).upper().strip()[0]
    peso_bagagem = float(input('Peso da bagagem: '))
    total += 1
    total_idade += idade
    if sexo in 'Ff' and idade < 25:
          mulher25 += 1

    if peso_bagagem > 23:
          bagagem23 += 1
    
    if total == 1:
           peso_maior = peso_bagagem
           nome_bagagem = nome
    else:
        if peso_bagagem > peso_maior:
              peso_maior = peso_bagagem
              nome_bagagem = nome
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SsNn':
            resposta = str(input('Opção inválida. Tente novamente: [S/N] ')).upper().strip()[0]
porcentagem = (bagagem23 / total) * 100
    
media_idade = total_idade / total
print('')
print(f'Total de passageiros: {total}')
print(f'Média de idade dos passageiros: {media_idade:.1f}')
print(f'A bagagem mais pesada é de {nome_bagagem}, com {peso_maior}kg.')
print(f'Ao todo, {mulher25} mulheres com menos de 25 anos.')
print(f'{bagagem23} passageiros pagaram taxa por excesso de peso, representando {porcentagem:.1f}% dos passageiros.')
print('')
print('Fim. Boa viagem.')
print('')
