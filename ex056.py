quantidade = int(input('Quantas pessoas serão cadastradas: '))
menor = 0
adulto = 0
idoso = 0

for c in range(quantidade): 
    idade = int(input(f'Idade da {c+1}° pessoa: '))

    if idade < 12:
        menor += 1
    elif idade < 60:
        adulto += 1
    else:
        idodo += 1

print(f'{menor} pessoas são menores de idade.')
print(f'{adulto} pessoas são adultas.')
print(f'{idoso} pessoas são idosas.')