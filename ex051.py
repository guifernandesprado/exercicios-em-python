nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
aumento = float(input('Digite a porcentagem de aumento: '))

reajuste = salario/100 * aumento
novo_salario = salario + reajuste

print(f'{nome}, seu salário atual é de R${salario}.')
print(f'Com o aumento de {aumento}%, você passará a receber R${novo_salario:.2f}.')