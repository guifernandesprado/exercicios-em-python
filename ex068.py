km = int(input('Qual a distância da viagem? '))

if km >= 200:
    valor = 0.45
else:
    valor = 0.5

passagem = km * valor

print(f'Você vai viajar {km}Km e sua passagem custará R${passagem:.2f}.')