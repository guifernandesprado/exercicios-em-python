num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2 :
    maior = num1
    menor = num2
    print(f'O maior número é o {maior} e o menor é o número {menor}')
elif num2 > num1:
    maior = num2
    menor = num1
    print(f'O maior número é o {maior} e o menor é o número {menor}')
else:
    print('Os dois números são iguais.')

