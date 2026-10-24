numeros = []

while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        print('Valor adicionado com sucesso...')
        numeros.append(num)
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
