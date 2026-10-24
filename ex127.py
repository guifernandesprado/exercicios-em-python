listanum = []
maior = menor = 0

for c in range(5):
    listanum.append(int(input(f'Digite um valor para a {c+1}º posição: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        elif listanum[c] < menor:
            menor = listanum [c]

print('-=' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitador foi {maior} nas posições ', end='')
for i,v in enumerate(listanum):
    if v ==maior:
        print(f'{i+1}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i+1}...', end='')
print()