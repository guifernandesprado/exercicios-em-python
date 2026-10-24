numeros = []
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso!')
    else: print('Valor duplicado. Não vou adicionar.')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=' *30)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
