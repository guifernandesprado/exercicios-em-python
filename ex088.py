soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulher = 0
for c in range (1,5):
    print(f'{c}ª PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    print('-' *30)
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome 
    if sexo in 'Mm'and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho se chama {nome} e tem {maior_idade_homem} anos.')
print(f'Ao todo, {mulher} mulheres tem menos que 20 anos.')