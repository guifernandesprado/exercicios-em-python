# exercício by Gemini
print('FECHAMENTO DE CAIXA')
total = maior = menor = 0
nome_maior = ''
nome_menor = ''
resp = 'S'
while resp in 'Ss':
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    total += valor
    if valor >= 0:
        maior = menor = valor
        if valor > maior:
            maior = valor
            nome_maior = nome
        if valor < menor:
            menor = valor
            nome_menor = nome

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]

print(f'O total da sua compra foi de {total:.2f}.')
print(f'O produto mais caro foi {nome_maior} R${maior} e o mais barato {nome_menor} R${menor}.')
print('Fim. VOLTE SEMPRE!')