# Exercício 70 CeV
print('>>>>>>>>>> Loja CeV <<<<<<<<<<')
print('')
total = maiormil = menor = cont = 0
nomebarato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000 :
        maiormil += 1
    if cont == 1 :
        menor = preco
        nomebarato = produto
    else:
        if preco < menor:
            menor = preco
            nomebarato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta =='N':
        break

print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maiormil} produtos custando mais que R$1000,00.')
print(f'O produto mais barato foi {nomebarato}, custando R${menor:.2f}')