num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opção = 0

while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print(f'A soma dos números digitados é de {soma}.')
    elif opção == 2 :
        mult = num1 * num2
        print(f'A multiplicação dos números digitados é de {mult}.')
    elif opção == 3 :
        if num1 > num2 :
            maior = num1
        else:
            maior = num2
        print(f'O maior número digitado foi {maior}.')
    elif opção == 4 :
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5 :
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente: ')
    print('=-=' * 15)
print('Fim do programa.')

