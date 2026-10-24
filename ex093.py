                                            #Exercício 4
                                            #Peça 5 números e mostre:
                                            #quantos são maiores que 10
                                            #a soma dos números maiores que 10
maior = 0
soma = 0
for c in range (5):
    num = int(input(f'Digite o {c+1}° número: '))
    if num > 10:
        maior += 1
        soma += num

print(f'No total, {maior} números digitados são maiores que 10.')
print(f'A soma desses número é de {soma}.')
