valores = []
acima = []
soma = cont = 0

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    soma += num
    cont += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

media = soma/cont
for indice in valores:
    if indice > media:
        acima.append(indice)

print(f'Os números digitados: {valores}')
print(f'Total de números: {cont}')
print(f'Média dos valores digitados: {media:.2f}')
print(f'Valores acima da média: {acima}')