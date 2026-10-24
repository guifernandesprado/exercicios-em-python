pessoas = []
dados = []
maior_peso = menor_peso = 0
nome_pesado = nome_leve = ''
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
        nome_pesado = nome_leve = dados[0]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
            nome_pesado = dados[0]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]
            nome_leve = dados[0]
    pessoas.append(dados[:])
    dados.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()

    if resposta == 'N':
        break


print(pessoas)
print(f'Total de pessoas = {len(pessoas)}')
print(f'O maior peso foi de {maior_peso}. Peso de {nome_pesado}')
print(f'O menor peso foi de {menor_peso}. Peso de {nome_leve}')


