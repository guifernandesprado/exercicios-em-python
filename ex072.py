print('=-'*30)
print('SIMULAÇÃO DE FINANCIAMENTO')
print('=-'*30)
print()

casa = float(input('Qual o valor da casa para compra? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos vai ser o financiamento? '))

print()

prestação = casa / (anos * 12)
limite = salario * 30 / 100

if prestação <= salario * 30 / 100:
    print(f'EMPRÉSTIMO APRAVADO! O valor da mensalidade está dentro do orçamento permitido.')
else:
    print(f'EMPRÉSTIMO NEGADO! O valor da mensalidade é maior que 30% do salário.')

print(f'A casa de R${casa:.2f} dividida em {anos} anos, ficará com a parcela de R${prestação:.2f} ',end='')
print(f'e seu limite atual é de R${limite:.2f}.')
print()
