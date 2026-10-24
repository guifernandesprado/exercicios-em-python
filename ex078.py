valor = float(input('Qual o valor gasto na loja? R$'))
print()
print('[1] - À vista (dinheiro/cheque)')
print('[2] - À vista (no cartão)')
print('[3] - Parcelado em 2 vezes')
print('[4] - Parcelado em 3 ou mais vezes')
print()
pagamento = int(input('E qual vai ser a forma de pagamento? '))

final = 0
forma = 0

if pagamento == 1:
    final = valor - (valor / 100 * 10)
    forma = ('à vista no dinheiro/cheque')
elif pagamento == 2:
    final = valor - (valor / 100 * 5)
    forma = ('à vista no cartão')
elif pagamento == 3:
    final = valor
    forma = ('parcelada em 2x')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas? '))
    forma = (f'parcelada em {parcelas} parcelas')
    final = valor + (valor / 100 * 20)

print(f'Sua compra de R${valor}, paga {forma} ficou no total de R${final:.2f}.')


