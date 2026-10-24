maior = menor = pos_maior = pos_menor = 0
numeros = []
for c in range(5):
    num = int(input(f'Digite um valor para a posição {c} : '))
    numeros.append(num)
    if c == 0 :
        maior = menor = num
        pos_maior = pos_menor = c
    else:
        if num > maior:
            maior = num
            pos_maior = c
        elif num < menor:
            menor = num
            pos_menor = c
print(f'Você digitou os valores {numeros}')
print(f'O maior número foi o {maior}, nas posições ',end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...',end='')
print(f'O menor número foi o {menor}, nas posições ',end='')
for i,v in enumerate(numeros):
    if v == menor:
        print(f'{i}...',end='')
