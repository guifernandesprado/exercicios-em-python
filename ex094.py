                                            #Exercício 5
                                            #Peça 5 números e mostre:
                                            #quantos são positivos
                                            #quantos são negativos
                                            #quantos são zero

positivo = 0
negativo = 0
zero = 0
for c in range (5):
    num = int(input(f'Digite o {c+1}° número: '))
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    elif num == 0:
        zero += 1

print(f'No total, {positivo} números são positivos, {negativo} são negativos e {zero} números são 0.')