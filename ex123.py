numeros = []
maior = menor = multi = 0

for c in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 3 == 0:
        multi += 1
    if c == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

print(f'A lista de todos os números: {numeros}')
print(f'O maior número digitado: {maior}')
print(f'O menor número digitado: {menor}')
print(f'A soma de todos o números: {sum(numeros)}')
print(f'Total de números múltiplos de 3: {multi}')