                                                            #Exercício 3
                                                            #Peça 5 números e mostre:
                                                            #o maior número
                                                            #o menor número
                                                            #a diferença entre eles

maior = 0
menor = 0

for c in range (5):
    num = int(input(f'Digite o {c+1}° número: '))
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
dif = maior - menor
print(f'O maior número digitado foi {maior}.')
print(f'O menor número digitado foi {menor}.')
print(f'A diferença entre eles é de {dif}.')