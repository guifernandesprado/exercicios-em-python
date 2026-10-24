numeros = []

while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado!Não vou adicionar...')
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'Você cadastrou {len(numeros)} valores únicos.')
print(f'Os números digitados foram: {numeros}')