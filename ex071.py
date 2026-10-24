from time import sleep
salario = int(input('Qual o valor do salário:  R$'))

if salario > 1250 :
    aumento = salario + (10 * salario / 100)
else:
    aumento = salario + (15 * salario / 100)

print('=-'*30)    
print(f'Calculando seu aumento...')
sleep(2)
print()
print(f'Seu salário era de R${salario:.2f} e agora é de R${aumento:.2f}.')
print()

