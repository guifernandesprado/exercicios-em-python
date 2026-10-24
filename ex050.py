acima = 0
abaixo = 0
soma = 0
numeros = []

for c in range(5):
    num = int(input('Digite um número: '))
    numeros.append(num)
    soma += num

media = soma / 5

for num in numeros:
    if num > media:
        acima += 1
    elif num < media:
        abaixo += 1

print(f'A média total é de {media}. {acima} números estão acima da média e {abaixo} abaixo da média.')
