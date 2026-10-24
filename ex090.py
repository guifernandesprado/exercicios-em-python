soma = 0

for c in range (5):
    num = int(input(f'Digite o {c+1}° número: '))
    soma += num
media = soma/5
print(f'A soma de todos os números é de {soma}.')
print(f'a média dos números é de {media}.')